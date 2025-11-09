#!/usr/bin/env python3
import glob
import re

# Updated CSS to tint footer logo white
updated_css = """<style>
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

/* Tint footer logo white */
footer [data-framer-name="Logo"] .svgContainer,
footer [data-framer-name="Logo"] img {
    filter: brightness(0) invert(1) !important;
}
</style>
"""

# Translation for the footer text
old_text = "Every moment in your child's early years are crucial for their growth and development."
new_text = "Cada momento en los primeros años de tu hijo es crucial para su crecimiento y desarrollo."

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Updating footer logo and text in {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Update CSS
        if 'Fix logo to show Growy logo' in content and 'Tint footer logo white' not in content:
            # Replace old CSS with updated CSS
            content = re.sub(
                r'<style>\s*/\* Fix logo to show Growy logo.*?</style>',
                updated_css,
                content,
                flags=re.DOTALL
            )
            changed = True

        # Translate footer text
        if old_text in content:
            content = content.replace(old_text, new_text)
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath}: Updated")
        else:
            print(f"  - {filepath}: No changes needed")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ Footer logo and text update completed!")
