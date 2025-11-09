#!/usr/bin/env python3
import os
import glob
import re

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Removing old Kinderly SVG logo definition from {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the old Kinderly logo SVG definition
        # It's the SVG with id="svg-117104609_5241"
        pattern = r'<svg width="124" height="32"[^>]*id="svg-117104609_5241"[^>]*>.*?</svg>'

        # Count matches
        matches = re.findall(pattern, content, re.DOTALL)
        count = len(matches)

        if count > 0:
            # Remove the SVG definition
            new_content = re.sub(pattern, '', content, flags=re.DOTALL)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ {filepath}: removed {count} old SVG logo definition(s)")
        else:
            print(f"  - {filepath}: No old SVG logo found")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ Old SVG logo definitions removed!")
print("The site will now use the new Growy logo image file.")
