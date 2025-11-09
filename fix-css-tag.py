#!/usr/bin/env python3
import glob
import re

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Fixing CSS tag in {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the broken CSS section
        pattern = r'</style>\s*/\* Fix logo to show Growy logo instead of Kinderly \*/(.*?)</head>'

        # Check if the pattern exists
        if re.search(pattern, content, re.DOTALL):
            # Fix it by wrapping in <style> tag
            content = re.sub(
                pattern,
                r'</style>\n<style>\n/* Fix logo to show Growy logo instead of Kinderly */\1</style>\n</head>',
                content,
                flags=re.DOTALL
            )

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ {filepath}: Fixed CSS tag")
        else:
            print(f"  - {filepath}: No broken CSS found")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ CSS tag fix completed!")
