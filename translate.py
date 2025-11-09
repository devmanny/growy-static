#!/usr/bin/env python3
"""
Translate HTML files from English to Spanish
Translates meta tags and visible content while preserving structure
"""

import re
import sys
from pathlib import Path

# Translation dictionary for common terms and phrases
TRANSLATIONS = {
    # Meta and common terms
    "Kinderly": "Kinderly",  # Brand name - keep as is

    # Navigation
    "Home": "Inicio",
    "About Us": "Sobre Nosotros",
    "About": "Acerca de",
    "Programs": "Programas",
    "Admission": "Admisión",
    "Parent Resources": "Recursos para Padres",
    "Contact": "Contacto",
    "Testimonials": "Testimonios",
    "Book a Tour": "Reservar una Visita",
    "Book A Tour": "Reservar una Visita",
    "Gallery": "Galería",
    "Blog": "Blog",
    "Privacy Policy": "Política de Privacidad",
    "Fees Breakdown": "Desglose de Tarifas",
    "Fees": "Tarifas",

    # Common buttons and CTAs
    "Learn More": "Más Información",
    "Get Started": "Comenzar",
    "Enroll Now": "Inscríbete Ahora",
    "Contact Us": "Contáctanos",
    "Read More": "Leer Más",
    "View All": "Ver Todo",
    "Submit": "Enviar",
    "Send": "Enviar",
    "Send Message": "Enviar Mensaje",
    "Book Now": "Reservar Ahora",
    "Schedule Tour": "Programar Visita",
    "Apply Now": "Aplicar Ahora",
    "Download": "Descargar",
    "View Details": "Ver Detalles",

    # Meta descriptions and titles
    "Kinderly offers a nurturing and creative learning environment for young children, fostering growth, exploration, and early education.": "Kinderly ofrece un entorno de aprendizaje nutritivo y creativo para niños pequeños, fomentando el crecimiento, la exploración y la educación temprana.",

    # Common headings
    "Welcome to Kinderly": "Bienvenidos a Kinderly",
    "Our Programs": "Nuestros Programas",
    "Our Mission": "Nuestra Misión",
    "Our Vision": "Nuestra Visión",
    "Our Values": "Nuestros Valores",
    "Why Choose Us": "Por Qué Elegirnos",
    "Why Choose Kinderly": "Por Qué Elegir Kinderly",
    "What Parents Say": "Lo Que Dicen los Padres",
    "Get in Touch": "Ponte en Contacto",
    "Contact Information": "Información de Contacto",
    "Hours of Operation": "Horario de Operación",
    "Follow Us": "Síguenos",

    # Age groups
    "Infants": "Bebés",
    "Toddlers": "Niños Pequeños",
    "Preschool": "Preescolar",
    "Pre-K": "Pre-Kinder",
    "Kindergarten": "Kínder",

    # Days of the week
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo",

    # Months
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre",

    # Form fields
    "Name": "Nombre",
    "First Name": "Nombre",
    "Last Name": "Apellido",
    "Email": "Correo Electrónico",
    "Phone": "Teléfono",
    "Message": "Mensaje",
    "Subject": "Asunto",
    "Address": "Dirección",
    "City": "Ciudad",
    "State": "Estado",
    "Zip Code": "Código Postal",
    "Child's Name": "Nombre del Niño",
    "Child's Age": "Edad del Niño",
    "Date of Birth": "Fecha de Nacimiento",
    "Preferred Start Date": "Fecha de Inicio Preferida",
    "Select": "Seleccionar",
    "Choose": "Elegir",

    # Common phrases
    "All Rights Reserved": "Todos los Derechos Reservados",
    "Copyright": "Derechos de Autor",
    "Terms of Service": "Términos de Servicio",
    "Terms & Conditions": "Términos y Condiciones",
    "FAQ": "Preguntas Frecuentes",
    "Frequently Asked Questions": "Preguntas Frecuentes",
    "More": "Más",
    "Less": "Menos",
    "Yes": "Sí",
    "No": "No",
    "Close": "Cerrar",
    "Open": "Abrir",
    "Menu": "Menú",
    "Search": "Buscar",
    "Back": "Volver",
    "Next": "Siguiente",
    "Previous": "Anterior",
    "Continue": "Continuar",
    "Skip": "Saltar",
    "Save": "Guardar",
    "Cancel": "Cancelar",
    "Edit": "Editar",
    "Delete": "Eliminar",
    "Share": "Compartir",
    "Print": "Imprimir",
    "or": "o",
    "and": "y",
    "of": "de",
    "to": "a",
    "for": "para",
    "in": "en",
    "at": "en",
    "on": "en",

    # Education terms
    "Early Childhood Education": "Educación Infantil Temprana",
    "Learning": "Aprendizaje",
    "Development": "Desarrollo",
    "Curriculum": "Currículum",
    "Activities": "Actividades",
    "Play": "Juego",
    "Growth": "Crecimiento",
    "Exploration": "Exploración",
    "Creative": "Creativo",
    "Nurturing": "Nutritivo",
    "Safe": "Seguro",
    "Environment": "Entorno",
    "Care": "Cuidado",
    "Education": "Educación",
    "Teachers": "Maestros",
    "Staff": "Personal",
    "Parents": "Padres",
    "Children": "Niños",
    "Students": "Estudiantes",
    "Family": "Familia",
    "Families": "Familias",
    "Community": "Comunidad",

    # Time-related
    "Today": "Hoy",
    "Tomorrow": "Mañana",
    "Yesterday": "Ayer",
    "Now": "Ahora",
    "Soon": "Pronto",
    "Later": "Más Tarde",
    "Daily": "Diario",
    "Weekly": "Semanal",
    "Monthly": "Mensual",
    "Yearly": "Anual",
    "Morning": "Mañana",
    "Afternoon": "Tarde",
    "Evening": "Noche",
    "Night": "Noche",
}


def translate_text(text):
    """Translate text using the translation dictionary"""
    # Sort by length (descending) to match longer phrases first
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)

    result = text
    for english, spanish in sorted_translations:
        # Case-sensitive replacement for exact matches
        result = result.replace(english, spanish)
        # Also handle Title Case
        if english[0].isupper():
            result = result.replace(english.lower(), spanish.lower())

    return result


def translate_html_file(file_path):
    """Translate an HTML file from English to Spanish"""
    print(f"Translating {file_path}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Change lang attribute from "en" to "es"
    content = re.sub(r'<html lang="en"', '<html lang="es"', content)

    # 2. Translate meta tags
    # Title tag
    content = re.sub(
        r'<title>(.*?)</title>',
        lambda m: f'<title>{translate_text(m.group(1))}</title>',
        content
    )

    # Meta description
    content = re.sub(
        r'<meta name="description" content="(.*?)"',
        lambda m: f'<meta name="description" content="{translate_text(m.group(1))}"',
        content
    )

    # OG tags
    content = re.sub(
        r'<meta property="og:title" content="(.*?)"',
        lambda m: f'<meta property="og:title" content="{translate_text(m.group(1))}"',
        content
    )

    content = re.sub(
        r'<meta property="og:description" content="(.*?)"',
        lambda m: f'<meta property="og:description" content="{translate_text(m.group(1))}"',
        content
    )

    # Twitter tags
    content = re.sub(
        r'<meta name="twitter:title" content="(.*?)"',
        lambda m: f'<meta name="twitter:title" content="{translate_text(m.group(1))}"',
        content
    )

    content = re.sub(
        r'<meta name="twitter:description" content="(.*?)"',
        lambda m: f'<meta name="twitter:description" content="{translate_text(m.group(1))}"',
        content
    )

    # 3. Translate visible text content
    # This is tricky with large HTML files. We'll use a more conservative approach
    # to avoid breaking the HTML structure or JavaScript

    # Translate text within common HTML tags (avoiding script and style)
    # We'll do this by finding text between > and < that's not inside script/style tags

    def translate_content_between_tags(match):
        text = match.group(1)
        # Skip if it looks like code (contains {, }, ;, etc.)
        if any(char in text for char in ['{', '}', ';', 'function', 'var', 'const', 'let', '=>']):
            return match.group(0)
        # Skip if it's just whitespace or very short
        if len(text.strip()) < 2:
            return match.group(0)
        # Skip if it looks like a URL or path
        if any(text.strip().startswith(prefix) for prefix in ['http://', 'https://', '/', './', '../', 'assets/']):
            return match.group(0)
        # Skip if it's a number or single character
        if text.strip().isdigit() or len(text.strip()) == 1:
            return match.group(0)

        translated = translate_text(text)
        return f'>{translated}<'

    # Don't translate inside script or style tags
    # Split content to avoid script/style sections
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', content, flags=re.DOTALL | re.IGNORECASE)

    translated_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not a script/style tag
            # Translate text between tags
            part = re.sub(r'>([^<]+)<', translate_content_between_tags, part)
            # Translate placeholder and value attributes (for form inputs)
            part = re.sub(
                r'placeholder="([^"]*)"',
                lambda m: f'placeholder="{translate_text(m.group(1))}"' if m.group(1).strip() else m.group(0),
                part
            )
            part = re.sub(
                r'aria-label="([^"]*)"',
                lambda m: f'aria-label="{translate_text(m.group(1))}"' if m.group(1).strip() else m.group(0),
                part
            )
            part = re.sub(
                r'alt="([^"]*)"',
                lambda m: f'alt="{translate_text(m.group(1))}"' if m.group(1).strip() else m.group(0),
                part
            )
            part = re.sub(
                r'title="([^"]*)"',
                lambda m: f'title="{translate_text(m.group(1))}"' if m.group(1).strip() else m.group(0),
                part
            )
        translated_parts.append(part)

    content = ''.join(translated_parts)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Calculate changes
    changes = sum(1 for a, b in zip(original_content, content) if a != b)
    print(f"✓ Translated {file_path} ({changes} characters changed)")

    return True


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python translate.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"Error: File {file_path} not found")
        sys.exit(1)

    try:
        translate_html_file(file_path)
    except Exception as e:
        print(f"Error translating {file_path}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
