#!/usr/bin/env python3
import glob
import json

# Cargar diccionario de traducciones
with open('translation-dictionary.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

print("="*70)
print("APLICANDO TRADUCCIONES COMPLETAS")
print("="*70)
print(f"\nCargadas {len(translations)} traducciones del diccionario\n")

# Función para traducir contenido
def translate_content(content, translations):
    """Aplica todas las traducciones al contenido"""
    result = content

    # Ordenar por longitud (más largo primero) para evitar reemplazos parciales
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)

    changes = 0
    for eng, esp in sorted_translations:
        if eng in result:
            result = result.replace(eng, esp)
            changes += 1

    return result, changes

# PASO 1: Traducir archivos HTML
print("📄 Traduciendo archivos HTML...\n")
html_files = glob.glob('*.html') + glob.glob('blog/*.html')
html_total_changes = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        translated, changes = translate_content(content, translations)

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(translated)
            print(f"  ✓ {filepath}: {changes} traducciones")
            html_total_changes += changes
        else:
            print(f"  - {filepath}: Sin cambios")

    except Exception as e:
        print(f"  ✗ Error en {filepath}: {e}")

print(f"\n✓ HTML traducido: {html_total_changes} cambios totales\n")

# PASO 2: Traducir archivos JavaScript
print("📄 Traduciendo archivos JavaScript (.mjs)...\n")
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
js_total_changes = 0

for filepath in js_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        translated, changes = translate_content(content, translations)

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(translated)
            filename = filepath.split('/')[-1]
            print(f"  ✓ {filename}: {changes} traducciones")
            js_total_changes += changes

    except Exception as e:
        print(f"  ✗ Error en {filepath}: {e}")

print(f"\n✓ JavaScript traducido: {js_total_changes} cambios totales")

# RESUMEN FINAL
print("\n" + "="*70)
print("RESUMEN FINAL")
print("="*70)
print(f"• Archivos HTML procesados: {len(html_files)}")
print(f"• Archivos JS procesados: {len(js_files)}")
print(f"• Cambios en HTML: {html_total_changes}")
print(f"• Cambios en JS: {js_total_changes}")
print(f"• TOTAL DE TRADUCCIONES APLICADAS: {html_total_changes + js_total_changes}")
print("="*70)
print("\n✅ ¡Traducción completa aplicada exitosamente!")
