#!/usr/bin/env python3
"""
Script to find ALL remaining English content in the site
"""

import os
import re
import json
from pathlib import Path

# Keywords to identify English content
ENGLISH_PATTERNS = [
    r'\bchild(?:ren)?\b',
    r'\bprogram(?:s)?\b',
    r'\bschool\b',
    r'\blearning\b',
    r'\beducation\b',
    r'\bkindergarten\b',
    r'\btoddler(?:s)?\b',
    r'\bparent(?:s)?\b',
    r'\bteacher(?:s)?\b',
    r'\bdevelopment\b',
    r'\bgrowth\b',
    r'\byear(?:s)?\b',
    r'\bmoment(?:s)?\b',
    r'\bcrucial\b',
    r'\bearly\b',
    r'\bexplor(?:e|ing|ation)\b',
    r'\bplay\b',
    r'\bnurturing\b',
    r'\bbelieve\b',
    r'\bwhere\b',
    r'\bevery\b',
    r'\btheir\b',
    r'\bjourney\b',
    r'\bready\b',
    r'\bstart\b',
    r'\benroll(?:ment)?\b',
]

# Technical terms to ignore
WHITELIST = [
    'var', 'function', 'return', 'const', 'let', 'import', 'export',
    'class', 'extends', 'style', 'data', 'framer', 'react', 'component',
    'container', 'div', 'svg', 'html', 'css', 'javascript', 'node',
    'server', 'express', 'localhost', 'http', 'https', 'url', 'path',
    'width', 'height', 'color', 'background', 'border', 'margin', 'padding',
    'display', 'flex', 'grid', 'position', 'absolute', 'relative',
]

def find_english_in_file(filepath):
    """Find English content in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove technical/code content for better detection
        content_clean = content
        for word in WHITELIST:
            content_clean = re.sub(r'\b' + word + r'\b', '', content_clean, flags=re.IGNORECASE)

        matches = []
        for pattern in ENGLISH_PATTERNS:
            for match in re.finditer(pattern, content_clean, re.IGNORECASE):
                # Get context (50 chars before and after)
                start = max(0, match.start() - 50)
                end = min(len(content), match.end() + 50)
                context = content[start:end].strip()

                # Clean up context
                context = ' '.join(context.split())

                # Skip if it looks like code
                if any(x in context.lower() for x in ['function', 'var ', 'const ', 'let ', 'return', 'import']):
                    continue

                # Skip if it's in a comment
                if context.strip().startswith('//') or context.strip().startswith('/*'):
                    continue

                matches.append({
                    'pattern': pattern,
                    'context': context,
                    'position': match.start()
                })

        return matches
    except Exception as e:
        return []

def scan_directory():
    """Scan all HTML and JS files for English content"""
    results = {}

    # Scan HTML files
    for html_file in Path('.').glob('*.html'):
        matches = find_english_in_file(html_file)
        if matches:
            results[str(html_file)] = {
                'type': 'HTML',
                'matches': len(matches),
                'samples': matches[:5]  # First 5 matches
            }

    # Scan JS files in assets/js
    js_dir = Path('assets/js')
    if js_dir.exists():
        for js_file in js_dir.glob('**/*.mjs'):
            matches = find_english_in_file(js_file)
            if matches:
                results[str(js_file)] = {
                    'type': 'JavaScript',
                    'matches': len(matches),
                    'samples': matches[:5]
                }

    return results

def extract_full_english_strings():
    """Extract complete English sentences/phrases"""
    english_content = []

    # Check HTML files
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find content in <p> tags
            p_matches = re.findall(r'<p[^>]*>([^<]+)</p>', content)
            for match in p_matches:
                text = match.strip()
                # Check if it contains English words
                if any(re.search(pattern, text, re.IGNORECASE) for pattern in ENGLISH_PATTERNS):
                    if not any(word in text.lower() for word in WHITELIST):
                        english_content.append({
                            'file': str(html_file),
                            'tag': 'p',
                            'text': text
                        })

            # Find content in <h1>, <h2>, <h3> tags
            for tag in ['h1', 'h2', 'h3', 'h4']:
                h_matches = re.findall(rf'<{tag}[^>]*>([^<]+)</{tag}>', content)
                for match in h_matches:
                    text = match.strip()
                    if any(re.search(pattern, text, re.IGNORECASE) for pattern in ENGLISH_PATTERNS):
                        if not any(word in text.lower() for word in WHITELIST):
                            english_content.append({
                                'file': str(html_file),
                                'tag': tag,
                                'text': text
                            })

            # Find content in data attributes or JS strings
            string_matches = re.findall(r'["\']([^"\']{20,})["\']', content)
            for match in string_matches:
                text = match.strip()
                if any(re.search(pattern, text, re.IGNORECASE) for pattern in ENGLISH_PATTERNS):
                    if not any(word in text.lower() for word in WHITELIST[:10]):  # Only check most common code words
                        english_content.append({
                            'file': str(html_file),
                            'tag': 'string',
                            'text': text
                        })
        except Exception as e:
            continue

    return english_content

if __name__ == '__main__':
    print("🔍 Buscando contenido en inglés...\n")

    # Scan for patterns
    results = scan_directory()

    print(f"📊 Archivos con contenido en inglés: {len(results)}\n")

    for filepath, data in sorted(results.items()):
        print(f"\n📄 {filepath} ({data['type']})")
        print(f"   Coincidencias: {data['matches']}")
        if data['samples']:
            print("   Ejemplos:")
            for sample in data['samples'][:3]:
                print(f"   - {sample['context'][:100]}...")

    # Extract full strings
    print("\n\n🔤 Extrayendo frases completas en inglés...\n")
    english_strings = extract_full_english_strings()

    # Deduplicate
    unique_strings = {}
    for item in english_strings:
        if item['text'] not in unique_strings:
            unique_strings[item['text']] = item

    print(f"📝 Frases únicas en inglés encontradas: {len(unique_strings)}\n")

    for text, data in sorted(unique_strings.items())[:30]:  # Show first 30
        print(f"\n📍 {data['file']} (<{data['tag']}>)")
        print(f"   {text}")

    # Save to file
    with open('remaining-english.json', 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total_files': len(results),
                'total_unique_strings': len(unique_strings)
            },
            'files': results,
            'strings': list(unique_strings.values())
        }, f, indent=2, ensure_ascii=False)

    print(f"\n\n💾 Resultados guardados en: remaining-english.json")
    print(f"\n✅ Total de frases a traducir: {len(unique_strings)}")
