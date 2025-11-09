#!/usr/bin/env python3
"""
Fix remaining English content in ALL HTML files
"""

import os
import glob

# Define translations - NOTE: Using ' (Unicode 2019) for curly apostrophe
TRANSLATIONS = {
    "Every moment in your child's early years is crucial. Our programs are designed to inspire curiosity, and build essential skills that will last a lifetime.":
        "Cada momento en los primeros años de tu hijo es crucial. Nuestros programas están diseñados para inspirar curiosidad y desarrollar habilidades esenciales que durarán toda la vida.",

    "Every moment in your child's early years are crucial for their growth and development.":
        "Cada momento en los primeros años de tu hijo es crucial para su crecimiento y desarrollo.",

    "Your Child's New Journey?":
        "¿El Nuevo Viaje de tu Hijo?",
}

# Process all HTML files
for html_file in glob.glob('*.html'):
    print(f"Processing {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply translations
    modified = False
    for eng, esp in TRANSLATIONS.items():
        if eng in content:
            content = content.replace(eng, esp)
            modified = True
            print(f"  ✓ Translated: {eng[:50]}...")

    # Write back if modified
    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {html_file} updated\n")
    else:
        print(f"  ⏭️  No changes needed\n")

print("✅ Done!")
