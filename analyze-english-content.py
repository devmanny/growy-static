#!/usr/bin/env python3
import glob
import re
import json

# Palabras comunes en inglés que indican contenido a traducir
english_keywords = [
    'the', 'and', 'our', 'your', 'for', 'with', 'from', 'this', 'that',
    'about', 'learn', 'more', 'explore', 'discover', 'offers', 'offering',
    'children', 'child', 'kids', 'young', 'early', 'education', 'learning',
    'school', 'kindergarten', 'preschool', 'toddler', 'program', 'programs',
    'parent', 'parents', 'family', 'read', 'download', 'subscribe',
    'newsletter', 'contact', 'welcome', 'hello', 'nurturing', 'fostering',
    'growth', 'development', 'safe', 'environment', 'activities', 'play',
    'creative', 'curriculum', 'teaching', 'teachers', 'staff', 'resources',
    'handbook', 'calendar', 'meal', 'plan', 'health', 'safety', 'guidelines',
    'admission', 'enroll', 'enrollment', 'fees', 'tuition', 'tour', 'visit',
    'testimonials', 'gallery', 'blog', 'privacy', 'policy', 'terms'
]

def extract_strings_from_js(content):
    """Extract string literals from JavaScript"""
    # Match strings in quotes (single and double)
    pattern = r'["\']([^"\']{3,})["\']'
    matches = re.findall(pattern, content)
    return [m for m in matches if any(keyword.lower() in m.lower() for keyword in english_keywords)]

def extract_text_from_html(content):
    """Extract visible text from HTML"""
    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)

    # Extract text between HTML tags
    pattern = r'>([^<]{3,})<'
    matches = re.findall(pattern, content)

    # Also extract meta descriptions and titles
    meta_pattern = r'content=["\']([^"\']{10,})["\']'
    meta_matches = re.findall(meta_pattern, content)

    all_matches = matches + meta_matches

    # Filter for English content
    english_content = []
    for text in all_matches:
        text = text.strip()
        if text and any(keyword.lower() in text.lower() for keyword in english_keywords):
            english_content.append(text)

    return english_content

print("="*70)
print("ANÁLISIS DE CONTENIDO EN INGLÉS")
print("="*70)

# Analyze JavaScript files
print("\n📄 Analizando archivos JavaScript (.mjs)...\n")
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
js_content = {}

for filepath in js_files[:10]:  # Analizar los primeros 10 archivos más importantes
    filename = filepath.split('/')[-1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        strings = extract_strings_from_js(content)
        if strings:
            # Limitar a strings únicos y relevantes
            unique_strings = list(set([s for s in strings if len(s) > 5 and len(s) < 200]))
            if unique_strings:
                js_content[filename] = unique_strings[:20]  # Top 20 por archivo

    except Exception as e:
        pass

print(f"Archivos JS con contenido en inglés: {len(js_content)}")
for filename, strings in list(js_content.items())[:5]:
    print(f"\n  📁 {filename}")
    for s in strings[:5]:
        print(f"    • {s[:80]}...")

# Analyze HTML files
print("\n\n📄 Analizando archivos HTML...\n")
html_files = glob.glob('*.html') + glob.glob('blog/*.html')
html_content = {}

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        text = extract_text_from_html(content)
        if text:
            unique_text = list(set(text))
            if unique_text:
                html_content[filepath] = unique_text[:10]

    except Exception as e:
        pass

print(f"Archivos HTML con contenido en inglés: {len(html_content)}")
for filepath, texts in list(html_content.items())[:3]:
    print(f"\n  📁 {filepath}")
    for t in texts[:3]:
        print(f"    • {t[:80]}...")

# Summary
print("\n\n" + "="*70)
print("RESUMEN")
print("="*70)
print(f"• Archivos JS con inglés: {len(js_content)}")
print(f"• Archivos HTML con inglés: {len(html_content)}")

total_js_strings = sum(len(strings) for strings in js_content.values())
total_html_strings = sum(len(texts) for texts in html_content.values())

print(f"• Total strings en JS: ~{total_js_strings}")
print(f"• Total textos en HTML: ~{total_html_strings}")
print(f"• TOTAL ESTIMADO: ~{total_js_strings + total_html_strings} elementos a traducir")
print("="*70)

# Save detailed report
report = {
    'javascript': js_content,
    'html': html_content,
    'summary': {
        'js_files': len(js_content),
        'html_files': len(html_content),
        'total_js_strings': total_js_strings,
        'total_html_strings': total_html_strings
    }
}

with open('translation-analysis.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("\n✓ Reporte detallado guardado en: translation-analysis.json")
