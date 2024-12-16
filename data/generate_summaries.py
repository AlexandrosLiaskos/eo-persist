import os
from pathlib import Path
import re

def clean_text(text):
    # Remove special characters and extra whitespace
    text = re.sub(r'[\n\r\t]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_main_sections(text, max_chars=500):
    # Try to find title, abstract, and introduction
    title_match = re.search(r'#\s*(.*?)\n', text)
    abstract_match = re.search(r'(?i)abstract[:\s]*(.*?)(?=##|\n\n|$)', text)
    intro_match = re.search(r'(?i)(?:introduction|background)[:\s]*(.*?)(?=##|\n\n|$)', text)
    
    title = clean_text(title_match.group(1)) if title_match else "Untitled"
    abstract = clean_text(abstract_match.group(1)) if abstract_match else ""
    intro = clean_text(intro_match.group(1)) if intro_match else ""
    
    summary = f"Title: {title}\n\n"
    
    if abstract:
        summary += f"Abstract:\n{abstract[:max_chars]}...\n\n"
    if intro and len(intro) > 100:  # Only include intro if it's substantial
        summary += f"Introduction Excerpt:\n{intro[:max_chars]}...\n"
        
    return summary

def generate_summaries():
    markdown_dir = Path('/home/liaskos/Downloads/know/eo-persist/data/markdown_output')
    summaries_dir = Path('/home/liaskos/Downloads/know/eo-persist/data/paper_summaries')
    
    # Create summaries directory if it doesn't exist
    summaries_dir.mkdir(exist_ok=True)
    
    # Process each markdown file
    for md_file in markdown_dir.glob('*.md'):
        print(f"Generating summary for {md_file.name}")
        
        try:
            # Read the markdown file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Generate summary
            summary = extract_main_sections(content)
            
            # Write summary to file
            summary_file = summaries_dir / f"{md_file.stem}_summary.md"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary)
                
            print(f"Summary created: {summary_file.name}")
            
        except Exception as e:
            print(f"Error processing {md_file.name}: {str(e)}")
            
    print("\nAll summaries have been generated in the paper_summaries directory.")

if __name__ == "__main__":
    generate_summaries()
