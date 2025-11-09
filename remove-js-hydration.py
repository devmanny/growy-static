#!/usr/bin/env python3
import glob
import re

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('blog/*.html')

print(f"Removing JavaScript hydration from {len(html_files)} HTML files...")
print("Converting to pure static HTML/CSS...\n")

total_changes = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_in_file = 0

        # 1. Remove all <script> tags that load Framer/React JavaScript
        script_pattern = r'<script[^>]*src=["\'][^"\']*\.mjs["\'][^>]*></script>'
        scripts_removed = len(re.findall(script_pattern, content))
        content = re.sub(script_pattern, '', content)
        changes_in_file += scripts_removed

        # 2. Remove inline scripts with Framer code
        inline_script_pattern = r'<script[^>]*>.*?framer.*?</script>'
        inline_removed = len(re.findall(inline_script_pattern, content, re.DOTALL | re.IGNORECASE))
        content = re.sub(inline_script_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        changes_in_file += inline_removed

        # 3. Remove data-framer-hydrate-v2 attribute
        hydrate_pattern = r'\s+data-framer-hydrate-v2="[^"]*"'
        hydrate_removed = len(re.findall(hydrate_pattern, content))
        content = re.sub(hydrate_pattern, '', content)
        changes_in_file += hydrate_removed

        # 4. Remove data-framer-component-type attribute
        component_pattern = r'\s+data-framer-component-type="[^"]*"'
        component_removed = len(re.findall(component_pattern, content))
        content = re.sub(component_pattern, '', content)
        changes_in_file += component_removed

        # 5. Remove data-framer-name but keep it for CSS selectors (optional)
        # We'll keep data-framer-name since our CSS uses it for styling

        # 6. Remove any remaining Framer hydration scripts
        hydrate_script_pattern = r'<script[^>]*>.*?__framer.*?</script>'
        hydrate_script_removed = len(re.findall(hydrate_script_pattern, content, re.DOTALL | re.IGNORECASE))
        content = re.sub(hydrate_script_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        changes_in_file += hydrate_script_removed

        # Write the modified content back
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ {filepath}:")
            if scripts_removed > 0:
                print(f"    - Removed {scripts_removed} external script tag(s)")
            if inline_removed > 0:
                print(f"    - Removed {inline_removed} inline Framer script(s)")
            if hydrate_removed > 0:
                print(f"    - Removed {hydrate_removed} hydrate attribute(s)")
            if component_removed > 0:
                print(f"    - Removed {component_removed} component-type attribute(s)")
            if hydrate_script_removed > 0:
                print(f"    - Removed {hydrate_script_removed} hydration script(s)")

            total_changes += changes_in_file
        else:
            print(f"  - {filepath}: No JavaScript to remove")

    except Exception as e:
        print(f"  ✗ Error in {filepath}: {e}")

print(f"\n{'='*60}")
print(f"✓ JavaScript hydration removal completed!")
print(f"✓ Total changes: {total_changes}")
print(f"\nThe site is now pure static HTML/CSS.")
print(f"All Spanish content should remain without JavaScript interference.")
print(f"{'='*60}")
