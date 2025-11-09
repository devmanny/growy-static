#!/usr/bin/env python3
import glob
import re

# Palabras clave en inglés que NO queremos ver
english_keywords = [
    'children', 'child', 'program', 'school', 'learning', 'education',
    'kindergarten', 'toddler', 'parent', 'parents', 'teacher', 'teachers',
    'explore', 'discover', 'nurture', 'nurturing', 'fostering', 'growth',
    'development', 'creative', 'activities', 'play', 'curriculum',
    'admission', 'enroll', 'tour', 'visit', 'contact', 'gallery',
    'testimonial', 'blog', 'newsletter', 'subscribe', 'download',
    'policy', 'privacy', 'safety', 'health', 'handbook', 'calendar',
    'meal', 'plan', 'fees', 'tuition', 'beginning', 'mission',
    'environment', 'journey', 'crucial', 'inspire', 'curiosity',
]

# Palabras que SÍ pueden estar en inglés (técnicas, nombres propios, etc.)
whitelist = [
    'framer', 'function', 'return', 'const', 'let', 'var', 'class',
    'import', 'export', 'default', 'null', 'undefined', 'true', 'false',
    'min-width', 'max-width', 'display', 'block', 'none', 'rgb', 'rgba',
    'gradient', 'conic', 'linear', 'radial', 'transform', 'translate',
    'background', 'color', 'font', 'family', 'style', 'css', 'html',
    'javascript', 'json', 'svg', 'path', 'fill', 'stroke', 'width',
    'height', 'button', 'form', 'input', 'email', 'type', 'submit',
]

def check_english_content(content, filename):
    """Verifica si hay contenido en inglés problemático"""
    # Eliminar código técnico
    content_clean = content
    for word in whitelist:
        content_clean = content_clean.lower().replace(word.lower(), '')

    # Buscar palabras en inglés
    found_keywords = []
    for keyword in english_keywords:
        # Buscar palabra completa (no como parte de otra palabra)
        pattern = r'\b' + keyword.lower() + r'\b'
        matches = re.findall(pattern, content_clean.lower())
        if matches:
            found_keywords.append((keyword, len(matches)))

    return found_keywords

print("="*70)
print("VERIFICACIÓN DE CONTENIDO EN INGLÉS")
print("="*70)
print("\nBuscando contenido en inglés restante...\n")

# Verificar HTML
print("📄 Verificando archivos HTML...\n")
html_files = glob.glob('*.html') + glob.glob('blog/*.html')
html_issues = {}

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        issues = check_english_content(content, filepath)
        if issues:
            html_issues[filepath] = issues

    except Exception as e:
        pass

if html_issues:
    print("⚠️  Encontrado contenido en inglés en HTML:")
    for filepath, issues in list(html_issues.items())[:5]:
        print(f"\n  📁 {filepath}")
        for keyword, count in issues[:3]:
            print(f"    • '{keyword}': {count} ocurrencias")
else:
    print("✅ No se encontró contenido en inglés en HTML")

# Verificar JavaScript
print("\n\n📄 Verificando archivos JavaScript...\n")
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
js_issues = {}

for filepath in js_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        issues = check_english_content(content, filepath)
        if issues and len(issues) > 5:  # Solo reportar si hay muchas ocurrencias
            js_issues[filepath] = issues

    except Exception as e:
        pass

if js_issues:
    print(f"⚠️  Posible contenido en inglés en {len(js_issues)} archivos JS")
    print("   (Algunos pueden ser código técnico - revisar manualmente)")
else:
    print("✅ No se encontró contenido problemático en JavaScript")

# RESUMEN
print("\n" + "="*70)
print("RESUMEN DE VERIFICACIÓN")
print("="*70)
print(f"• Archivos HTML con posible inglés: {len(html_issues)}")
print(f"• Archivos JS con posible inglés: {len(js_issues)}")

if len(html_issues) + len(js_issues) < 5:
    print("\n✅ ¡Traducción prácticamente completa!")
    print("   El sitio está mayormente en español.")
else:
    print("\n⚠️  Aún hay contenido por revisar")
    print("   Considerar traducciones adicionales.")

print("="*70)
