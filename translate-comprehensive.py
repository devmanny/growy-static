#!/usr/bin/env python3
import re
import sys

# Diccionario completo de traducciones
translations = {
    # Nombre del proyecto
    "Kinderly": "Growy",
    "Kinderly School": "Growy",

    # Hero section
    "Encouraging": "Alentador",
    "Exploration": "Exploración",
    "One Step at a Time": "Un Paso a la Vez",
    "We love to inspire children to explore and discover through play and learning": "Nos encanta inspirar a los niños a explorar y descubrir a través del juego y el aprendizaje",

    # Admissions
    "LIMITED SEAT AVAILABLE": "CUPOS LIMITADOS DISPONIBLES",
    "ADMISSION OPEN FOR 2024-2025": "ADMISIÓN ABIERTA PARA 2024-2025",
    "LIMITED SEATS AVAILABLE": "CUPOS LIMITADOS DISPONIBLES",

    # Titles and headings
    "Welcome to Kinderly School !!": "¡¡Bienvenido a Growy!!",
    "Welcome to": "Bienvenido a",
    "Early Learning Center": "Centro de Aprendizaje Temprano",
    "Our Services": "Nuestros Servicios",
    "What We Offer": "Lo Que Ofrecemos",
    "Why Choose Us": "Por Qué Elegirnos",
    "Our Mission": "Nuestra Misión",
    "Our Vision": "Nuestra Visión",
    "Meet Our Team": "Conoce a Nuestro Equipo",
    "Parent Testimonials": "Testimonios de Padres",

    # Navigation
    "About Us": "Nosotros",
    "Our Programs": "Nuestros Programas",
    "Programs": "Programas",
    "Testimonials": "Testimonios",
    "Contact": "Contacto",
    "Gallery": "Galería",
    "Blog": "Blog",
    "Admission": "Admisión",
    "Parent Resources": "Recursos para Padres",
    "Book a Tour": "Reserva un Tour",
    "Privacy Policy": "Política de Privacidad",
    "Fees Breakdown": "Desglose de Tarifas",
    "Home": "Inicio",

    # Buttons and CTAs
    "Read More": "Leer Más",
    "Learn More": "Aprender Más",
    "Get Started": "Comenzar",
    "Contact Us": "Contáctanos",
    "Enroll Now": "Inscríbete Ahora",
    "Schedule a Visit": "Programa una Visita",
    "Apply Now": "Aplicar Ahora",
    "Download": "Descargar",
    "View All": "Ver Todo",

    # Activities/Filters
    "All Activities": "Todas las Actividades",
    "Music": "Música",
    "Arts & Crafts": "Artes y Manualidades",
    "Physical Activities": "Actividades Físicas",
    "Party": "Fiesta",
    "Outdoor Play": "Juego al Aire Libre",
    "Science": "Ciencia",
    "Math": "Matemáticas",
    "Reading": "Lectura",

    # Program names
    "Infant Program": "Programa de Infantes",
    "Toddler Program": "Programa de Pequeños",
    "Preschool Program": "Programa Preescolar",
    "Pre-K Program": "Programa Pre-Kinder",
    "After School Program": "Programa Después de la Escuela",
    "Summer Camp": "Campamento de Verano",

    # Common UI elements
    "Age": "Edad",
    "Price": "Precio",
    "Seats": "Cupos",
    "Submit": "Enviar",
    "Send": "Enviar",
    "Message": "Mensaje",
    "Name": "Nombre",
    "Email": "Correo Electrónico",
    "Phone": "Teléfono",
    "Address": "Dirección",
    "Date": "Fecha",
    "Time": "Hora",

    # FAQ and descriptions
    "Question": "Pregunta",
    "Answer": "Respuesta",
    "Description": "Descripción",
    "Details": "Detalles",

    # Time and schedule
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
    "Hours": "Horario",
    "Open": "Abierto",
    "Closed": "Cerrado",

    # Footer and legal
    "All Rights Reserved": "Todos los Derechos Reservados",
    "Copyright": "Derechos de Autor",
    "Terms of Service": "Términos de Servicio",
    "Privacy": "Privacidad",

    # Social media
    "Follow Us": "Síguenos",
    "Share": "Compartir",

    # Program details
    "Full-Time": "Tiempo Completo",
    "Part-Time": "Medio Tiempo",
    "Half-Day": "Medio Día",
    "Full-Day": "Día Completo",

    # Status and availability
    "Available": "Disponible",
    "Full": "Lleno",
    "Waitlist": "Lista de Espera",
    "Enrolling": "Inscribiendo",
}

def translate_js_strings(content):
    """Traduce strings literales en JavaScript minificado"""
    result = content

    # Sort by length (longest first) to avoid partial replacements
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)

    for eng, esp in sorted_translations:
        # Match the string in various quote contexts
        # This handles strings in minified code
        patterns = [
            # Double quotes
            (f'"{eng}"', f'"{esp}"'),
            # Single quotes
            (f"'{eng}'", f"'{esp}'"),
            # In text with spaces around
            (f' {eng} ', f' {esp} '),
            # At start of string
            (f'"{eng} ', f'"{esp} '),
            (f"'{eng} ", f"'{esp} "),
            # At end of string
            (f' {eng}"', f' {esp}"'),
            (f" {eng}'", f" {esp}'"),
        ]

        for old_pattern, new_pattern in patterns:
            result = result.replace(old_pattern, new_pattern)

    return result

def main():
    filepath = "assets/sites/49pSfmDl3bVFoyDoGQdiD9/vqxsczQeX6MXIyRtdI0uIRiGX1Ut0eztkA-j9RWnxuo.HJPSP4RQ.mjs"

    print(f"Restaurando desde backup...")
    # First restore from backup
    import shutil
    backup_path = "assets/sites/49pSfmDl3bVFoyDoGQdiD9/backups/vqxsczQeX6MXIyRtdI0uIRiGX1Ut0eztkA-j9RWnxuo.HJPSP4RQ.mjs"
    shutil.copy(backup_path, filepath)
    print(f"  ✓ Archivo restaurado")

    print(f"Traduciendo archivo principal de la página...")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        translated = translate_js_strings(content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(translated)

        print(f"  ✓ Traducción completada")

        # Show some stats
        changes = sum(1 for eng in translations.keys() if eng in content)
        print(f"\nSe encontraron {changes} términos a traducir")

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
