#!/usr/bin/env python3
"""
Extract only the essential n8n documentation for builders/developers.
This creates a focused subset that's actually useful for Claude Projects.
"""

import os
from pathlib import Path
import re

def extract_essential_docs(input_dir, output_file='n8n_essential_docs.md'):
    """Extract only the most important docs for building with n8n."""
    
    input_path = Path(input_dir)
    
    # Define which sections are actually useful for builders
    essential_patterns = [
        # Core concepts
        '**/getting-started/**/*.md',
        '**/quick-start*.md',
        '**/key-concepts*.md',
        
        # Workflow basics
        '**/workflows/**/*.md',
        '**/workflow-*.md',
        '**/building-*.md',
        
        # Node documentation
        '**/nodes/creating-nodes/**/*.md',
        '**/nodes/node-basics/**/*.md',
        '**/code-node/**/*.md',
        '**/http-request/**/*.md',
        '**/webhook/**/*.md',
        
        # Expressions and code
        '**/code/**/*.md',
        '**/expressions/**/*.md',
        '**/data-transformation/**/*.md',
        
        # API reference
        '**/api/api-reference/**/*.md',
        '**/api-endpoints*.md',
        
        # Common integrations (top 10-15)
        '**/nodes/n8n-nodes-base.*.md',  # Core nodes
        
        # Development
        '**/development/**/*.md',
        '**/custom-nodes/**/*.md',
    ]
    
    # Files to definitely exclude
    exclude_patterns = [
        '**/changelog*.md',
        '**/release-notes*.md',
        '**/migration*.md',
        '**/troubleshooting*.md',
        '**/faq*.md',
    ]
    
    print("Extracting essential n8n documentation for builders...\n")
    
    # Collect matching files
    essential_files = []
    all_md_files = list(input_path.rglob('*.md'))
    
    for md_file in all_md_files:
        # Check if file should be excluded
        exclude = False
        for pattern in exclude_patterns:
            if md_file.match(pattern):
                exclude = True
                break
        
        if exclude:
            continue
            
        # Check if file matches essential patterns
        for pattern in essential_patterns:
            if md_file.match(pattern):
                essential_files.append(md_file)
                break
    
    # Also grab these specific files if they exist
    important_files = [
        'README.md',
        'index.md',
        'getting-started.md',
        'quickstart.md',
        'core-concepts.md',
        'workflow-basics.md',
        'expressions.md',
        'code-node.md',
    ]
    
    for filename in important_files:
        for md_file in all_md_files:
            if md_file.name.lower() == filename.lower():
                if md_file not in essential_files:
                    essential_files.append(md_file)
    
    essential_files.sort()
    print(f"Found {len(essential_files)} essential files (out of {len(all_md_files)} total)\n")
    
    # Build the combined document
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Header
        outfile.write("# n8n Essential Documentation for Builders\n\n")
        outfile.write("This is a curated subset of n8n documentation focused on building workflows and nodes.\n\n")
        outfile.write("## Quick Reference\n\n")
        outfile.write("- **Expressions**: Use `{{ }}` for JavaScript expressions\n")
        outfile.write("- **Variables**: `$json` (current node data), `$node['NodeName'].json` (other node data)\n")
        outfile.write("- **Code Node**: Write JavaScript or Python in workflows\n")
        outfile.write("- **HTTP Request**: Make API calls with built-in auth\n")
        outfile.write("- **Webhook**: Create endpoints to trigger workflows\n\n")
        outfile.write("---\n\n")
        
        # Table of Contents
        outfile.write("## Table of Contents\n\n")
        
        current_section = ""
        for md_file in essential_files:
            rel_path = md_file.relative_to(input_path)
            
            # Group by first directory
            section = rel_path.parts[0] if len(rel_path.parts) > 1 else "General"
            if section != current_section:
                current_section = section
                outfile.write(f"\n### {section.replace('-', ' ').title()}\n\n")
            
            title = rel_path.stem.replace('-', ' ').title()
            anchor = rel_path.stem.lower()
            outfile.write(f"- [{title}](#{anchor})\n")
        
        outfile.write("\n---\n\n")
        
        # Process files
        for i, md_file in enumerate(essential_files, 1):
            print(f"Processing ({i}/{len(essential_files)}): {md_file.name}")
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                rel_path = md_file.relative_to(input_path)
                title = rel_path.stem.replace('-', ' ').title()
                anchor = rel_path.stem.lower()
                
                # Section header
                outfile.write(f"\n\n## {title} {{#{anchor}}}\n\n")
                outfile.write(f"*Source: {rel_path}*\n\n")
                
                # Clean up content
                # Remove any metadata headers
                content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
                
                # Adjust heading levels
                content = re.sub(r'^#\s+', '### ', content, flags=re.MULTILINE)
                content = re.sub(r'^##\s+', '#### ', content, flags=re.MULTILINE)
                content = re.sub(r'^###\s+', '##### ', content, flags=re.MULTILINE)
                
                outfile.write(content)
                outfile.write("\n\n---\n\n")
                
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
    
    # Summary
    file_size_kb = Path(output_file).stat().st_size / 1024
    with open(output_file, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    
    print(f"\n✅ Success! Created {output_file}")
    print(f"📊 File size: {file_size_kb:.1f} KB (vs several MB for full docs)")
    print(f"📄 Line count: {line_count:,} lines (much more manageable!)")
    print(f"📁 Files included: {len(essential_files)}")
    
    return output_file

def create_even_smaller_version(input_file, output_file='n8n_core_reference.md'):
    """Create an even more condensed version with just core reference."""
    
    print("\nCreating ultra-condensed reference version...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract only the most important sections using regex
    sections_to_keep = [
        r'## Quick Reference.*?(?=##|\Z)',
        r'## Expressions.*?(?=##|\Z)',
        r'## Code Node.*?(?=##|\Z)',
        r'## Workflow.*?(?=##|\Z)',
        r'## HTTP Request.*?(?=##|\Z)',
        r'## Webhook.*?(?=##|\Z)',
    ]
    
    condensed_content = ["# n8n Core Reference (Ultra-Condensed)\n\n"]
    
    for pattern in sections_to_keep:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            condensed_content.append(match.group(0))
            condensed_content.append("\n---\n\n")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(condensed_content))
    
    file_size_kb = Path(output_file).stat().st_size / 1024
    with open(output_file, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    
    print(f"✅ Created {output_file}")
    print(f"📊 File size: {file_size_kb:.1f} KB")
    print(f"📄 Line count: {line_count:,} lines")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <n8n-docs-directory>")
        print("Example: python script.py n8n-docs")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    
    # Create essential docs
    essential_file = extract_essential_docs(input_dir)
    
    # Offer to create even smaller version
    print("\n" + "="*50)
    response = input("Create an ultra-condensed version too? (y/n): ")
    if response.lower() == 'y':
        create_even_smaller_version(essential_file)