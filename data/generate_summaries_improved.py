import os
from pathlib import Path
import re

def clean_text(text):
    # Remove special characters and extra whitespace
    text = re.sub(r'[\n\r\t]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_main_sections(text):
    # Try to find different title patterns
    title_patterns = [
        r'#\s*(.*?)\n',
        r'^Title:\s*(.*?)(?=\n)',
        r'^\s*(.*?)\n.*?(?:Abstract|Introduction)',
    ]
    
    title = "Untitled"
    for pattern in title_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            title = clean_text(match.group(1))
            if len(title) > 10:  # Reasonable title length
                break
    
    # Find abstract with multiple patterns
    abstract_patterns = [
        r'(?i)abstract[:\s]*(.*?)(?=##|\n\n(?:[A-Z]|$))',
        r'(?i)summary[:\s]*(.*?)(?=##|\n\n(?:[A-Z]|$))',
    ]
    
    abstract = ""
    for pattern in abstract_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            abstract = clean_text(match.group(1))
            if len(abstract) > 100:  # Reasonable abstract length
                break
    
    # Find keywords if they exist
    keywords_match = re.search(r'(?i)keywords?[:\s]*(.*?)(?=##|\n\n|$)', text)
    keywords = clean_text(keywords_match.group(1)) if keywords_match else ""
    
    # Construct the summary
    summary = []
    
    if title and title != "Untitled":
        summary.append(f"# {title}")
        summary.append("")
    
    if abstract:
        summary.append("## Abstract")
        # Limit abstract to ~1000 characters while keeping complete sentences
        if len(abstract) > 1000:
            sentences = re.split(r'(?<=[.!?])\s+', abstract[:1000])
            abstract = ' '.join(sentences[:-1]) + '...'
        summary.append(abstract)
        summary.append("")
    
    if keywords:
        summary.append("## Keywords")
        summary.append(keywords)
        summary.append("")
    
    return '\n'.join(summary)

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
