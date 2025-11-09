#!/usr/bin/env python3
import re

# Files that contain the old Kinderly logo
files_to_fix = [
    'assets/sites/49pSfmDl3bVFoyDoGQdiD9/chunk-BZNXSHPH.mjs',
    'assets/sites/49pSfmDl3bVFoyDoGQdiD9/chunk-XYLTFKJS.mjs'
]

# The Kinderly logo path starts with "M113.934 31.5" and ends before the next path or closing tag
# We'll replace the entire SVG element that contains this path

print("Fixing logo in JavaScript files...")

for filepath in files_to_fix:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Find and replace SVG elements containing the Kinderly logo
        # Pattern: <svg with Kinderly paths> -> <img with Growy logo>

        # Pattern 1: Replace SVG with width="124" height="32" containing M113.934
        pattern1 = r'<svg[^>]*width="124"[^>]*height="32"[^>]*>.*?M113\.934[^<]*</svg>'
        replacement1 = '<img src="assets/images/growy logo.svg" alt="Growy" style="width:100%;height:100%;object-fit:contain"/>'
        content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

        # Pattern 2: For React.createElement calls that create SVG
        # e.g., r("svg",{...},[r("path",{d:"M113.934..."})])
        # We need to be more surgical here

        # Replace createElement("svg") calls that have the Kinderly viewBox
        pattern2 = r'r\("svg",\{[^}]*viewBox:"0 0 124 32"[^}]*\},[^\]]*M113\.934[^\]]*\]?\)'
        replacement2 = 'r("img",{src:"assets/images/growy logo.svg",alt:"Growy",style:{width:"100%",height:"100%",objectFit:"contain"}})'
        content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

        # Pattern 3: For any remaining Kinderly logo paths
        # Replace the path data itself
        pattern3 = r'M113\.934 31\.5[^"]*fill:#081646'
        if pattern3 in content or re.search(r'M113\.934', content):
            # If we still find the Kinderly logo, replace more aggressively
            # Replace any path starting with M113.934
            pattern4 = r'"M113\.934[^"]*"'
            replacement4 = '""'
            content = re.sub(pattern4, replacement4, content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath}: Logo replaced")
        else:
            print(f"  - {filepath}: No changes made (pattern not found)")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ JavaScript logo fix completed!")
print("The logo should now display correctly without blinking.")
