#!/usr/bin/env python3
import re
import sys
import glob

# Diccionario de traducciones
translations = {
    # Nombres de páginas/navegación
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

    # Nombre del proyecto
    "Kinderly": "Growy",

    # Frases comunes
    "Home": "Inicio",
    "Read More": "Leer Más",
    "Learn More": "Aprender Más",
    "Get Started": "Comenzar",
    "Contact Us": "Contáctanos",

    # Activities/Filters
    "All Activities": "Todas las Actividades",
    "Music": "Música",
    "Arts & Crafts": "Artes y Manualidades",
    "Physical Activities": "Actividades Físicas",
    "Party": "Fiesta",

    # Common UI elements
    "Age": "Edad",
    "Price": "Precio",
    "Seats": "Cupos",
    "Submit": "Enviar",
    "Send": "Enviar",
    "Message": "Mensaje",

    # Description texts
    "Description": "Descripción",
    "Description text": "Texto descriptivo",
}

def translate_js_strings(content):
    """Traduce solo strings literales en JavaScript, preservando el código"""

    # Función para reemplazar dentro de strings entre comillas dobles
    def replace_in_double_quotes(match):
        original = match.group(0)
        quote_char = original[0]  # " o '
        string_content = original[1:-1]  # contenido sin comillas

        # Aplicar traducciones
        translated = string_content
        for eng, esp in translations.items():
            # Solo reemplazar coincidencias exactas o con espacios alrededor
            translated = re.sub(r'\b' + re.escape(eng) + r'\b', esp, translated)

        return f'{quote_char}{translated}{quote_char}'

    # Reemplazar strings entre comillas dobles y simples
    # Patrón que captura strings, evitando comillas escapadas
    result = re.sub(r'"([^"\\]|\\.)*"', replace_in_double_quotes, content)
    result = re.sub(r"'([^'\\]|\\.)*'", replace_in_double_quotes, result)

    return result

def main():
    mjs_files = [
        "chunk-DKPJAV5M.mjs",
        "chunk-BMO3KVA7.mjs",
        "vqxsczQeX6MXIyRtdI0uIRiGX1Ut0eztkA-j9RWnxuo.HJPSP4RQ.mjs",
        "chunk-XYLTFKJS.mjs",
        "5_jUWyBT10pRobeh8_pTWDzSUPptXX-QCBxqaiSNowo.HKRL4ATT.mjs",
        "3Kfl4CE5nRltxq0UHghWbg-oNO82JW7EeEJGVPZOgak.3UE6NX3J.mjs",
        "9zwVDf3HtiMG5OkCEjhCRwr6vWkbiXN17LCRfGLonSQ.6RKATQNK.mjs",
        "DHCnHN9z9grJdZplR5O2z5ZVo-f3VmCIEOLgIhPdIvs.KKAT7767.mjs",
        "chunk-LW5JN4M3.mjs",
        "chunk-PI2M6FZL.mjs",
    ]

    base_path = "assets/sites/49pSfmDl3bVFoyDoGQdiD9/"

    for filename in mjs_files:
        filepath = base_path + filename
        print(f"Traduciendo: {filename}")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            translated = translate_js_strings(content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(translated)

            print(f"  ✓ Completado")
        except Exception as e:
            print(f"  ✗ Error: {e}")

if __name__ == "__main__":
    main()
