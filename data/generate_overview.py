import os
from pathlib import Path
import re
from collections import defaultdict

def extract_info_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'#\s*(.*?)\n', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Untitled"
    
    # Extract abstract
    abstract_match = re.search(r'(?i)abstract[:\s]*(.*?)(?=##|\n\n(?:[A-Z]|$))', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    
    # Extract keywords
    keywords_match = re.search(r'(?i)keywords?[:\s]*(.*?)(?=##|\n\n|$)', content)
    keywords = keywords_match.group(1).strip() if keywords_match else ""
    
    # Extract main topics from title and abstract
    topics = set()
    topic_patterns = [
        r'arctic', r'remote sensing', r'climate', r'neural network', r'machine learning',
        r'monitoring', r'permafrost', r'snow', r'temperature', r'humidity',
        r'satellite', r'cloud', r'data', r'earth observation', r'environment'
    ]
    
    combined_text = f"{title} {abstract} {keywords}".lower()
    for pattern in topic_patterns:
        if re.search(pattern, combined_text, re.IGNORECASE):
            topics.add(pattern)
    
    return {
        'title': title,
        'abstract_preview': abstract[:200] + "..." if len(abstract) > 200 else abstract,
        'keywords': keywords,
        'topics': topics,
        'filename': file_path.stem
    }

def generate_overview():
    markdown_dir = Path('/home/liaskos/Downloads/know/eo-persist/data/markdown_output')
    papers_info = []
    topics_index = defaultdict(list)
    
    # Process each markdown file
    for md_file in markdown_dir.glob('*.md'):
        info = extract_info_from_md(md_file)
        papers_info.append(info)
        
        # Build topics index
        for topic in info['topics']:
            topics_index[topic].append(info['title'])
    
    # Generate overview markdown
    overview = ["# Papers Overview\n"]
    
    # Add paper summaries
    overview.append("## Paper Summaries\n")
    for i, paper in enumerate(papers_info, 1):
        overview.append(f"### {i}. {paper['title']}")
        overview.append(f"**File:** {paper['filename']}")
        overview.append(f"**Topics:** {', '.join(sorted(paper['topics']))}")
        if paper['keywords']:
            overview.append(f"**Keywords:** {paper['keywords']}")
        overview.append(f"**Abstract Preview:** {paper['abstract_preview']}\n")
    
    # Add topics index
    overview.append("## Topics Index\n")
    for topic, papers in sorted(topics_index.items()):
        overview.append(f"### {topic.title()}")
        for paper in papers:
            overview.append(f"- {paper}")
        overview.append("")
    
    # Write overview to file
    overview_path = Path('/home/liaskos/Downloads/know/eo-persist/data/papers_overview.md')
    with open(overview_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(overview))
    
    print(f"Overview generated: {overview_path}")

if __name__ == "__main__":
    generate_overview()
