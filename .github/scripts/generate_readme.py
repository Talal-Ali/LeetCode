#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path
from collections import defaultdict

def extract_problem_info(problem_dir):
    """
    Extract problem info from LeetSync metadata and README.md
    """
    try:
        readme_path = os.path.join(problem_dir, 'README.md')
        
        if not os.path.exists(readme_path):
            return None
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract problem number and title from h2 tag
        title_match = re.search(r'<h2>.*?<a href="[^"]+">([^<]+)</a></h2>', content)
        title = title_match.group(1) if title_match else "Unknown"
        
        # Extract problem number from folder name (format: XXXX-problem-name)
        folder_match = re.match(r'^(\d+)-', problem_dir)
        problem_num = int(folder_match.group(1)) if folder_match else 0
        
        # Extract difficulty
        difficulty_match = re.search(r"Difficulty-([^-]+)-", content)
        difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
        
        return {
            'number': problem_num,
            'title': title.strip(),
            'difficulty': difficulty.strip(),
            'folder': problem_dir
        }
    except Exception as e:
        print(f"Error parsing {problem_dir}: {e}")
        return None

def categorize_problem(title):
    """
    Categorize problem based on title keywords.
    Order matters - more specific categories first!
    """
    title_lower = title.lower()
    
    # Check Game Theory first (most specific)
    game_theory_keywords = ['nim', 'divisor', 'winning', 'player', 'coin', 'game']
    if any(keyword in title_lower for keyword in game_theory_keywords):
        # But exclude if it's a more specific category
        if not any(kw in title_lower for kw in ['binary', 'tree', 'search']):
            return 'Game Theory'
    
    # Define other categories
    categories = {
        'Array / String': ['array', 'string', 'substring', 'concatenation', 'shuffle', 'consecutive'],
        'Linked List': ['linked', 'list', 'node'],
        'Tree': ['tree', 'binary', 'traversal', 'inorder'],
        'Backtracking / Recursion': ['permutation', 'combination', 'generate', 'queens', 'parenthes'],
        'Dynamic Programming': ['dp', 'dynamic'],
        'Graph': ['graph', 'path', 'search'],
        'Hash Table': ['hash', 'map', 'duplicate'],
        'Stack / Queue': ['stack', 'queue'],
        'Math': ['math', 'number', 'sum']
    }
    
    for category, keywords in categories.items():
        if any(keyword in title_lower for keyword in keywords):
            return category
    
    return 'Miscellaneous'

def generate_readme():
    """
    Scan all problem folders and generate organized README
    """
    problems = defaultdict(lambda: defaultdict(list))
    
    # Find all problem folders (format: number-problem-name)
    problem_dirs = sorted([d for d in os.listdir('.') 
                          if os.path.isdir(d) and re.match(r'^\d+-', d)])
    
    for problem_dir in problem_dirs:
        info = extract_problem_info(problem_dir)
        if info:
            category = categorize_problem(info['title'])
            difficulty = info['difficulty']
            problems[category][difficulty].append(info)
    
    # Generate README.md content
    readme_content = """# LeetCode Solutions

This repository contains organized LeetCode problem solutions categorized by subject and sorted by difficulty level.

**Note:** Problems are automatically organized by category and difficulty whenever new solutions are pushed.

"""
    
    # Define emoji for categories
    category_emojis = {
        'Array / String': '📚',
        'Linked List': '🔗',
        'Tree': '🌳',
        'Backtracking / Recursion': '🎯',
        'Dynamic Programming': '⚙️',
        'Game Theory': '🎮',
        'Graph': '🕸️',
        'Hash Table': '🗂️',
        'Stack / Queue': '📦',
        'Math': '🔢',
        'Miscellaneous': '📝'
    }
    
    # Sort categories
    sorted_categories = sorted(problems.keys())
    
    for category in sorted_categories:
        emoji = category_emojis.get(category, '📋')
        readme_content += f"\n### {emoji} {category}\n\n"
        
        # Define difficulty order
        difficulty_order = ['Easy', 'Medium', 'Hard']
        
        for difficulty in difficulty_order:
            if difficulty in problems[category]:
                # Sort by problem number
                probs = sorted(problems[category][difficulty], key=lambda x: x['number'])
                readme_content += f"#### {difficulty}\n"
                
                # Add sequential numbering within each difficulty
                for idx, prob in enumerate(probs, 1):
                    readme_content += f"- {idx} - [{prob['title']}](./{prob['folder']}/) \n"
                readme_content += "\n"
        
        readme_content += "---\n"
    
    # Generate summary table
    readme_content += "\n## 📊 Summary\n\n"
    readme_content += "| Category | Easy | Medium | Hard | Total |\n"
    readme_content += "|----------|------|--------|------|-------|\n"
    
    total_easy = total_medium = total_hard = total_all = 0
    
    for category in sorted_categories:
        easy_count = len(problems[category].get('Easy', []))
        medium_count = len(problems[category].get('Medium', []))
        hard_count = len(problems[category].get('Hard', []))
        total = easy_count + medium_count + hard_count
        
        total_easy += easy_count
        total_medium += medium_count
        total_hard += hard_count
        total_all += total
        
        emoji = category_emojis.get(category, '📋')
        readme_content += f"| {emoji} {category} | {easy_count} | {medium_count} | {hard_count} | {total} |\n"
    
    readme_content += f"| **Total** | **{total_easy}** | **{total_medium}** | **{total_hard}** | **{total_all}** |\n\n"
    
    # Add footer
    readme_content += """## 📝 Languages Used

- C++ (76.2%)
- Python (23.8%)

---

*This repository is managed by [LeetSync extension](https://github.com/LeetPushExtension/LeetPush)*
*README automatically generated by GitHub Actions*
"""
    
    # Write README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md generated successfully!")
    print(f"Total problems: {total_all}")
    print(f"Easy: {total_easy}, Medium: {total_medium}, Hard: {total_hard}")

if __name__ == '__main__':
    generate_readme()
