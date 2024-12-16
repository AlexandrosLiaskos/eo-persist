import os
from pathlib import Path
import re

def extract_info_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'#\s*(.*?)\n', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Untitled"
    
    # Extract keywords
    keywords_match = re.search(r'(?i)keywords?[:\s]*(.*?)(?=##|\n\n|$)', content)
    keywords = keywords_match.group(1).strip() if keywords_match else ""
    
    # Determine paper type based on content and keywords
    paper_type = "Research Paper"  # default
    if any(word in title.lower() for word in ['chapter', 'book']):
        paper_type = "Book Chapter"
    elif 'deliverable' in title.lower():
        paper_type = "Project Deliverable"
    elif any(word in keywords.lower() for word in ['review', 'survey']):
        paper_type = "Review Paper"
    
    return {
        'title': title.replace('#', '').strip(),
        'type': paper_type,
        'keywords': keywords,
        'filename': file_path.stem
    }

def generate_toc():
    markdown_dir = Path('/home/liaskos/Downloads/know/eo-persist/data/markdown_output')
    papers_info = []
    
    # Process each markdown file
    for md_file in markdown_dir.glob('*.md'):
        info = extract_info_from_md(md_file)
        papers_info.append(info)
    
    # Sort papers by type
    papers_by_type = {}
    for paper in papers_info:
        if paper['type'] not in papers_by_type:
            papers_by_type[paper['type']] = []
        papers_by_type[paper['type']].append(paper)
    
    # Generate TOC markdown
    toc = ["# Collection Contents\n"]
    toc.append("## Overview\n")
    toc.append(f"Total Documents: {len(papers_info)}\n")
    for type_name, papers in papers_by_type.items():
        toc.append(f"- {type_name}s: {len(papers)}")
    toc.append("\n## Documents by Type\n")
    
    # Add papers grouped by type
    for type_name, papers in papers_by_type.items():
        toc.append(f"### {type_name}s\n")
        for i, paper in enumerate(papers, 1):
            toc.append(f"{i}. **{paper['title']}**")
            if paper['keywords']:
                toc.append(f"   - *Keywords:* {paper['keywords']}")
            toc.append(f"   - *File:* `{paper['filename']}`")
            toc.append("")
    
    # Add quick reference section
    toc.append("## Quick Reference\n")
    toc.append("### Main Research Areas")
    toc.append("1. Arctic Environment Studies")
    toc.append("2. Remote Sensing Applications")
    toc.append("3. Climate Change Monitoring")
    toc.append("4. Data Processing & Analysis")
    toc.append("\n### Key Technologies")
    toc.append("1. Satellite Data Processing")
    toc.append("2. Cloud Computing")
    toc.append("3. Machine Learning")
    toc.append("4. Environmental Monitoring")
    
    # Write TOC to file
    toc_path = Path('/home/liaskos/Downloads/know/eo-persist/data/collection_contents.md')
    with open(toc_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(toc))
    
    print(f"Table of Contents generated: {toc_path}")

if __name__ == "__main__":
    generate_toc()
