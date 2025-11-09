#!/usr/bin/env python3
import os
import glob

# SVG logo reference to replace
old_svg_reference = '<svg style="width:100%;height:100%" viewBox="0 0 124 32"><use href="#svg-117104609_5241"/></svg>'

# New IMG tag with Growy logo
new_logo_img = '<img src="assets/images/growy logo.png" alt="Growy" style="width:100%;height:100%;object-fit:contain"/>'

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Replacing logo in {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count replacements
        count = content.count(old_svg_reference)

        if count > 0:
            # Replace the SVG with IMG
            new_content = content.replace(old_svg_reference, new_logo_img)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ {filepath}: {count} replacements")
        else:
            print(f"  - {filepath}: No changes needed")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ Logo replacement completed!")
