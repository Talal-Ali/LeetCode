#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_problem_info(readme_path):
    """
    Extract problem number, title, and difficulty from README.md
    """
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
        
        # Extract problem number and title from h2 tag
        title_match = re.search(r'<h2>.*?<a href="[^"]+">([^<]+)</a></h2>', content)
        title = title_match.group(1) if title_match else "Unknown"
        
        # Extract problem number from title or folder name
        number_match = re.search(r'^(\d+)', title)
        problem_num = number_match.group(1) if number_match else "0"
        
        # Extract difficulty
        difficulty_match = re.search(r"Difficulty-([^-]+)-", content)
        difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
        
        return {
            'number': int(problem_num),
            'title': title.strip(),
            'difficulty': difficulty.strip()
        }
    except Exception as e:
        print(f"Error parsing {readme_path}: {e}")
        return None

def categorize_problem(title):
    """
    Categorize problem based on title keywords
    """
    title_lower = title.lower()
    
    # Define category keywords
    categories = {
        'Array / String': ['array', 'string', 'substring', 'concatenation', 'shuffle', 'consecutive'],
        'Linked List': ['linked', 'list', 'node'],
        'Tree': ['tree', 'binary', 'traversal', 'inorder'],
        'Backtracking / Recursion': ['permutation', 'combination', 'generate', 'queens', 'parenthes'],
        'Dynamic Programming': ['game', 'nim', 'divisor', 'dp'],
        'Game Theory': ['game', 'winning', 'player', 'optimal'],
        'Graph': ['graph', 'path'],
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
    problem_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d+-', d)]
    
    for problem_dir in problem_dirs:
        readme_path = os.path.join(problem_dir, 'README.md')
        if os.path.exists(readme_path):
            info = extract_problem_info(readme_path)
            if info:
                category = categorize_problem(info['title'])
                difficulty = info['difficulty']
                problems[category][difficulty].append({
                    'number': info['number'],
                    'title': info['title'],
                    'folder': problem_dir
                })
    
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
                probs = sorted(problems[category][difficulty], key=lambda x: x['number'])
                readme_content += f"#### {difficulty}\n"
                for prob in probs:
                    readme_content += f"- **{prob['number']}** - [{prob['title']}](./{prob['folder']}/) \n"
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

*This repository is managed by [LeetPush extension](https://github.com/LeetPushExtension/LeetPush)*
*README automatically generated by GitHub Actions*
"""
    
    # Write README
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("README.md generated successfully!")
    print(f"Total problems: {total_all}")
    print(f"Easy: {total_easy}, Medium: {total_medium}, Hard: {total_hard}")

if __name__ == '__main__':
    generate_readme()
