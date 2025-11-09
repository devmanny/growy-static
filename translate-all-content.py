#!/usr/bin/env python3
import re
import glob

# Diccionario completo de traducciones
translations = {
    # Títulos y headers
    "Exploration, Un Paso a la Vez": "Exploración, Paso a Paso",
    "Exploration": "Exploración",
    "Where we believe in nurturing young minds and fostering a love for learning from an early age": "Donde creemos en nutrir mentes jóvenes y fomentar el amor por el aprendizaje desde temprana edad",
    "En Growy, estamos dedicados": "En Growy, estamos dedicados",
    "to providing a safe, supportive, and stimulating environment where children can grow": "a proporcionar un ambiente seguro, de apoyo y estimulante donde los niños puedan crecer",

    # Secciones principales
    "Our Learning Paths": "Nuestras Rutas de Aprendizaje",
    "Our Activities": "Nuestras Actividades",
    "Parents Testimonios": "Testimonios de Padres",
    "Frequently Asked Questions": "Preguntas Frecuentes",

    # Programas
    "Toddler": "Pequeños",
    "(1.5 - 3 years)": "(1.5 - 3 años)",
    "In this program, we focus on nurturing a safe, secure, and stimulating environment where young children can explore their world": "En este programa, nos enfocamos en nutrir un ambiente seguro, protegido y estimulante donde los niños pequeños puedan explorar su mundo",

    "Pre-School": "Preescolar",
    "(2 - 3 years)": "(2 - 3 años)",
    "Our Pre-School program blends play-based learning with structured activities to help children develop foundational skills": "Nuestro programa Preescolar combina el aprendizaje basado en el juego con actividades estructuradas para ayudar a los niños a desarrollar habilidades fundamentales",

    "Kindergarten": "Jardín de Infantes",
    "(3 - 4 years)": "(3 - 4 años)",
    "In Kindergarten, we provide a balanced approach to learning, combining academic readiness with social and emotional development": "En Jardín de Infantes, proporcionamos un enfoque equilibrado para el aprendizaje, combinando la preparación académica con el desarrollo social y emocional",

    "(4 - 5 years)": "(4 - 5 años)",
    "this program is designed to prepare children for a smooth transition into elementary school. We focus on enhancing skills of the children": "este programa está diseñado para preparar a los niños para una transición suave a la escuela primaria. Nos enfocamos en mejorar las habilidades de los niños",

    # Actividades
    "Music Classes": "Clases de Música",
    "Discover the joy of music through interactive lessons, and creative expression": "Descubre la alegría de la música a través de lecciones interactivas y expresión creativa",

    "Spring Party": "Fiesta de Primavera",
    "Get ready for a mix of games that promote both fitness and cooperation": "Prepárate para una mezcla de juegos que promueven tanto la aptitud física como la cooperación",

    "Rock Climbing": "Escalada en Roca",
    "Challenge yourself on our indoor rock climbing walls &building strength": "Desafíate en nuestras paredes de escalada interior y desarrolla fuerza",

    "Halloween Party": "Fiesta de Halloween",
    "Celebrate with spooky costumes, games, and treats in a safe and fun environment": "Celebra con disfraces espeluznantes, juegos y golosinas en un ambiente seguro y divertido",

    "Indoor Games": "Juegos de Interior",
    "Enjoy interactive indoor games that help the mind and encourage collaboration": "Disfruta juegos interactivos de interior que ayudan la mente y fomentan la colaboración",

    "Outdoor Games": "Juegos al Aire Libre",
    "Engage in fun and active games promote teamwork & physical fitness": "Participa en juegos divertidos y activos que promueven el trabajo en equipo y la aptitud física",

    # CTA y footer
    "Ready to Begin Your Child's New Journey?": "¿Listo para Comenzar el Nuevo Viaje de tu Hijo?",
    "Every moment in your child's early years is crucial. Our programs are designed to inspire curiosity, and build essential skills that will last a lifetime": "Cada momento en los primeros años de tu hijo es crucial. Nuestros programas están diseñados para inspirar curiosidad y desarrollar habilidades esenciales que durarán toda la vida",

    "Other Services": "Otros Servicios",
    "All rights reserved": "Todos los derechos reservados",
    "Designed & Developed by": "Diseñado y Desarrollado por",
    "Powered by": "Impulsado por",

    # Estadísticas
    "Total Courses": "Cursos Totales",
    "Students Enrolled": "Estudiantes Inscritos",

    # Días de la semana (en caso de que no estén traducidos)
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
}

# Traducciones para JavaScript
def translate_content(content):
    """Traduce el contenido reemplazando todas las frases"""
    result = content

    # Ordenar por longitud (más largo primero) para evitar reemplazos parciales
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)

    for eng, esp in sorted_translations:
        # Reemplazar en varios contextos posibles
        patterns = [
            (eng, esp),  # Directo
            (f'"{eng}"', f'"{esp}"'),  # Entre comillas dobles
            (f"'{eng}'", f"'{esp}'"),  # Entre comillas simples
            (f'>{eng}<', f'>{esp}<'),  # Entre tags HTML
        ]

        for old, new in patterns:
            if old in result:
                result = result.replace(old, new)

    return result

# Traducir archivos HTML
html_files = glob.glob('*.html') + glob.glob('blog/*.html')
print(f"Traduciendo {len(html_files)} archivos HTML...")

html_changes = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        content = translate_content(content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            changes = sum(1 for eng in translations.keys() if eng in original)
            html_changes += changes
            print(f"  ✓ {filepath}: {changes} traducciones")
        else:
            print(f"  - {filepath}: Sin cambios")

    except Exception as e:
        print(f"  ✗ Error en {filepath}: {e}")

print(f"\n✓ HTML traducido: {html_changes} cambios totales\n")

# Traducir archivos JavaScript
js_files = glob.glob('assets/sites/49pSfmDl3bVFoyDoGQdiD9/*.mjs')
print(f"Traduciendo {len(js_files)} archivos JavaScript...")

js_changes = 0
for filepath in js_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        content = translate_content(content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            changes = sum(1 for eng in translations.keys() if eng in original)
            js_changes += changes
            if changes > 0:
                print(f"  ✓ {filepath.split('/')[-1]}: {changes} traducciones")

    except Exception as e:
        print(f"  ✗ Error en {filepath}: {e}")

print(f"\n✓ JavaScript traducido: {js_changes} cambios totales")
print(f"\n✓ TOTAL: {html_changes + js_changes} traducciones completadas!")
