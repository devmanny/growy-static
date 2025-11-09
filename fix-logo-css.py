#!/usr/bin/env python3
import glob

# CSS to fix the logo - hide SVG paths and show background image instead
css_fix = """
<style>
/* Fix logo to show Growy logo instead of Kinderly */
[data-framer-name="Logo"] svg path {
    display: none !important;
}

[data-framer-name="Logo"] .svgContainer {
    background-image: url('assets/images/growy logo.svg') !important;
    background-size: contain !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
}

[data-framer-name="Logo"] svg {
    opacity: 0 !important;
}
</style>
"""

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Adding CSS fix to {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if fix already exists
        if 'Fix logo to show Growy logo' in content:
            print(f"  - {filepath}: CSS fix already present")
            continue

        # Add CSS fix before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', f'{css_fix}</head>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ {filepath}: CSS fix added")
        else:
            print(f"  ✗ {filepath}: No </head> tag found")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ CSS logo fix completed!")
print("The logo should now display correctly without modification to JS files.")
