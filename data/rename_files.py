import os
from pathlib import Path
import re
import shutil

def clean_filename(title):
    # Remove special characters and replace spaces with underscores
    clean = re.sub(r'[^\w\s-]', '', title)
    clean = re.sub(r'[-\s]+', '_', clean)
    # Limit length and remove trailing underscores
    clean = clean[:100].strip('_')
    return clean.lower()

def extract_title_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try different patterns to find the title
    patterns = [
        r'#\s*(.*?)\n',
        r'^Title:\s*(.*?)(?=\n)',
        r'^\s*(.*?)\n.*?(?:Abstract|Introduction)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
        if match:
            title = match.group(1).strip()
            if len(title) > 10:  # Reasonable title length
                return title
    
    return None

def rename_files():
    base_dir = Path('/home/liaskos/Downloads/know/eo-persist/data')
    markdown_dir = base_dir / 'markdown_output'
    summaries_dir = base_dir / 'paper_summaries'
    
    # Dictionary to store original filename to new filename mappings
    filename_mappings = {}
    
    # First, extract titles from markdown files
    for md_file in markdown_dir.glob('*.md'):
        title = extract_title_from_md(md_file)
        if title:
            new_name = clean_filename(title)
            filename_mappings[md_file.stem] = new_name
    
    # Rename files in all directories
    for original_stem, new_name in filename_mappings.items():
        # Rename PDF
        pdf_path = base_dir / f"{original_stem}.pdf"
        if pdf_path.exists():
            new_pdf_path = base_dir / f"{new_name}.pdf"
            print(f"Renaming PDF: {pdf_path.name} -> {new_pdf_path.name}")
            shutil.move(str(pdf_path), str(new_pdf_path))
        
        # Rename Markdown
        md_path = markdown_dir / f"{original_stem}.md"
        if md_path.exists():
            new_md_path = markdown_dir / f"{new_name}.md"
            print(f"Renaming Markdown: {md_path.name} -> {new_md_path.name}")
            shutil.move(str(md_path), str(new_md_path))
        
        # Rename Summary
        summary_path = summaries_dir / f"{original_stem}_summary.md"
        if summary_path.exists():
            new_summary_path = summaries_dir / f"{new_name}_summary.md"
            print(f"Renaming Summary: {summary_path.name} -> {new_summary_path.name}")
            shutil.move(str(summary_path), str(new_summary_path))

if __name__ == "__main__":
    rename_files()
