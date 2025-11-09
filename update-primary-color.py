#!/usr/bin/env python3
import glob
import re

# New primary cyan color
new_cyan = "#00D2E0"
new_cyan_rgb = "rgb(0, 210, 224)"

# Old cyan colors to replace
old_colors = {
    # CSS variables
    '--accent-cyan: #00D4B5': f'--accent-cyan: {new_cyan}',
    '--accent-cyan-light: #1FDFCA': '--accent-cyan-light: #1FE5EE',

    # RGB values in JavaScript
    'rgb(0, 212, 181)': new_cyan_rgb,
    'rgb(31, 223, 202)': 'rgb(31, 229, 238)',
}

print(f"Updating primary color to {new_cyan}...\n")

# Update HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')
print(f"Updating {len(html_files)} HTML files...")

html_changes = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for old, new in old_colors.items():
            if old in content:
                content = content.replace(old, new)
                html_changes += content.count(new) - original.count(new)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath}")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print(f"\n✓ HTML updated: {html_changes} changes\n")

# Update JavaScript files
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
print(f"Updating {len(js_files)} JavaScript files...")

js_changes = 0
for filepath in js_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for old, new in old_colors.items():
            if 'rgb(' in old:  # Only replace RGB values in JS
                content = content.replace(old, new)

        if content != original:
            changes = sum(1 for old in old_colors.keys() if 'rgb(' in old and old in original)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            if changes > 0:
                print(f"  ✓ {filepath.split('/')[-1]}: {changes} changes")
                js_changes += changes

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print(f"\n✓ JavaScript updated: {js_changes} changes")
print(f"\n{'='*60}")
print(f"✓ Primary color updated to {new_cyan}!")
print(f"✓ Total changes: {html_changes + js_changes}")
print(f"{'='*60}")
