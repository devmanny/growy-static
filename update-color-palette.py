#!/usr/bin/env python3
import glob
import re

# Nueva paleta de colores
color_palette_css = """<style>
:root {
  /* Azul principal - Ese morado-azul magnético del header */
  --primary-blue: #5B6FFF;
  --primary-blue-dark: #4A5CE6;

  /* Amarillo - Puro optimismo en forma de color */
  --accent-yellow: #FFB649;
  --accent-yellow-light: #FFC966;

  /* Rosa/Magenta - Energía pura */
  --accent-pink: #FF3B8F;
  --accent-pink-light: #FF5CA5;

  /* Turquesa/Cyan - Ese toque fresco y moderno */
  --accent-cyan: #00D4B5;
  --accent-cyan-light: #1FDFCA;

  /* Neutrales que mantienen la composición */
  --text-dark: #2D3436;
  --text-light: #636E72;
  --background-light: #F8F9FA;
  --white: #FFFFFF;
}
</style>
"""

# Mapeo de colores antiguos a nuevos
color_mappings = [
    # Verde principal -> Cyan (botones y acentos)
    ('rgb(0, 186, 89)', 'var(--accent-cyan)'),
    ('#00BA59', 'var(--accent-cyan)'),
    ('rgb(3, 156, 77)', 'var(--accent-cyan-light)'),

    # Amarillo -> Amarillo nuevo
    ('rgb(255, 207, 85)', 'var(--accent-yellow)'),
    ('#FFCF55', 'var(--accent-yellow)'),
    ('rgb(255, 100, 100)', 'var(--accent-pink)'),
    ('#FF6464', 'var(--accent-pink)'),
    ('rgb(255, 84, 84)', 'var(--accent-pink-light)'),
    ('rgb(253, 89, 89)', 'var(--accent-pink-light)'),

    # Azul oscuro -> Texto oscuro
    ('rgb(8, 22, 70)', 'var(--text-dark)'),
    ('#081646', 'var(--text-dark)'),

    # Grises
    ('rgb(51, 55, 91)', 'var(--text-dark)'),
    ('rgb(89, 91, 112)', 'var(--text-light)'),

    # Beige/Crema -> Background claro
    ('rgb(251, 249, 240)', 'var(--background-light)'),
    ('#FBF9F0', 'var(--background-light)'),
]

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Updating color palette in {len(html_files)} HTML files...")

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add color palette CSS variables if not present
        if ':root {' not in content:
            # Add after existing <style> tag or before </head>
            if '<style>' in content:
                # Find the first <style> tag and add palette after it
                content = content.replace('<style>', '<style>' + color_palette_css, 1)
            elif '</head>' in content:
                content = content.replace('</head>', color_palette_css + '</head>', 1)

        # Replace color values
        changes_made = 0
        for old_color, new_color in color_mappings:
            old_count = content.count(old_color)
            if old_count > 0:
                content = content.replace(old_color, new_color)
                changes_made += old_count

        if changes_made > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath}: {changes_made} color replacements")
        else:
            print(f"  - {filepath}: No color changes needed")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print("\n✓ Color palette update completed!")
print("\nUpdating JavaScript files...")

# Update JS files
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
js_changes = 0

for filepath in js_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changes_made = 0
        for old_color, new_color in color_mappings:
            # In JS files, we need to keep rgb() format but change values
            # Let's just update the rgb values
            if old_color in content:
                # For JS, we'll replace with the actual color value, not CSS var
                # since Framer's JS might not support CSS variables
                js_color_map = {
                    'rgb(0, 186, 89)': 'rgb(0, 212, 181)',  # cyan
                    'rgb(3, 156, 77)': 'rgb(31, 223, 202)',  # cyan light
                    'rgb(255, 207, 85)': 'rgb(255, 182, 73)',  # yellow
                    'rgb(255, 100, 100)': 'rgb(255, 59, 143)',  # pink
                    'rgb(255, 84, 84)': 'rgb(255, 92, 165)',  # pink light
                    'rgb(253, 89, 89)': 'rgb(255, 92, 165)',  # pink light
                    'rgb(8, 22, 70)': 'rgb(45, 52, 54)',  # text dark
                    'rgb(51, 55, 91)': 'rgb(45, 52, 54)',  # text dark
                    'rgb(89, 91, 112)': 'rgb(99, 110, 114)',  # text light
                    'rgb(251, 249, 240)': 'rgb(248, 249, 250)',  # background light
                }

                if old_color in js_color_map:
                    new_js_color = js_color_map[old_color]
                    old_count = content.count(old_color)
                    if old_count > 0:
                        content = content.replace(old_color, new_js_color)
                        changes_made += old_count

        if changes_made > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath.split('/')[-1]}: {changes_made} color replacements")
            js_changes += changes_made

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print(f"\n✓ JavaScript color update completed! ({js_changes} total changes)")
