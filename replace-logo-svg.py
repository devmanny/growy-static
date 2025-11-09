#!/usr/bin/env python3
import os
import glob

# Current IMG tag with PNG logo
old_logo_png = '<img src="assets/images/growy logo.png" alt="Growy" style="width:100%;height:100%;object-fit:contain"/>'

# New IMG tag with SVG logo (better quality, scales perfectly)
new_logo_svg = '<img src="assets/images/growy logo.svg" alt="Growy" style="width:100%;height:100%;object-fit:contain"/>'

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Replacing PNG logo with SVG logo in {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count replacements
        count = content.count(old_logo_png)

        if count > 0:
            # Replace the PNG with SVG
            new_content = content.replace(old_logo_png, new_logo_svg)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ {filepath}: {count} replacements")
        else:
            print(f"  - {filepath}: No changes needed")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ Logo replacement completed! Now using SVG for better quality.")
