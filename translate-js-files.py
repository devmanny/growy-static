#!/usr/bin/env python3
"""
Script to translate remaining English content in JavaScript files
"""

import os
from pathlib import Path

# Same translation dictionary
FINAL_TRANSLATIONS = {
    # Age ranges
    "1-2 years": "1-2 años",
    "1-2 years.": "1-2 años.",

    # Headers
    "Your Child's New Journey?": "¿El Nuevo Viaje de tu Hijo?",
    "Welcome & Learning": "Bienvenida y Aprendizaje",
    "Head Teacher": "Maestro Principal",
    "Physical Education Teacher": "Maestro de Educación Física",

    # Call to action
    "Enroll now": "Inscríbete ahora",

    # Programs descriptions - Full sentences
    "Every moment in your child's early years are crucial for their growth and development.":
        "Cada momento en los primeros años de tu hijo es crucial para su crecimiento y desarrollo.",

    "Every moment in your child's early years is crucial. Our programs are designed to inspire curiosity, and build essential skills that will last a lifetime.":
        "Cada momento en los primeros años de tu hijo es crucial. Nuestros programas están diseñados para inspirar curiosidad y desarrollar habilidades esenciales que durarán toda la vida.",

    "Our Pequeños Program offers a warm and engaging environment where young children begin to explore and make sense of the world around them. Through sensory play, music, movement, and interactive storytelling, toddlers develop early cognitive and motor skills while building strong emotional connections with peers and caregivers.":
        "Nuestro Programa Pequeños ofrece un ambiente cálido y atractivo donde los niños pequeños comienzan a explorar y comprender el mundo que los rodea. A través del juego sensorial, música, movimiento y narrativa interactiva, los niños desarrollan habilidades cognitivas y motoras tempranas mientras construyen fuertes conexiones emocionales con compañeros y cuidadores.",

    "Our Preescolar Program focuses on providing a nurturing environment where young children can begin exploring the world around them. Through sensory play, storytelling, and guided activities, toddlers are encouraged to develop motor skills, language, and early social interaction":
        "Nuestro Programa Preescolar se enfoca en proporcionar un ambiente enriquecedor donde los niños pequeños pueden comenzar a explorar el mundo que los rodea. A través del juego sensorial, cuentacuentos y actividades guiadas, se anima a los niños a desarrollar habilidades motoras, lenguaje e interacción social temprana",

    "In our Programa Jardín de Infantes, we focus on fostering independence and cognitive development through playful learning experiences. By blending academic readiness with social and emotional skills, children are well-prepared for the next steps in their educational journey.":
        "En nuestro Programa Jardín de Infantes, nos enfocamos en fomentar la independencia y el desarrollo cognitivo a través de experiencias de aprendizaje lúdicas. Al combinar la preparación académica con habilidades sociales y emocionales, los niños están bien preparados para los próximos pasos en su viaje educativo.",

    "Our Pre-K Program prepares children for a smooth transition to elementary school. With a focus on building foundational academic skills and social development, children are encouraged to explore, ask questions, and engage in group learning activities.":
        "Nuestro Programa Pre-K prepara a los niños para una transición fluida a la escuela primaria. Con un enfoque en construir habilidades académicas fundamentales y desarrollo social, se alienta a los niños a explorar, hacer preguntas y participar en actividades de aprendizaje grupal.",

    # Key features
    "Engaging activities that promote learning through play.":
        "Actividades atractivas que promueven el aprendizaje a través del juego.",

    "Development of essential social and emotional skills.":
        "Desarrollo de habilidades sociales y emocionales esenciales.",

    "Activities that nurture social and emotional growth through peer interaction.":
        "Actividades que nutren el crecimiento social y emocional a través de la interacción con compañeros.",

    "Social and emotional growth through group play and interaction.":
        "Crecimiento social y emocional a través del juego e interacción grupal.",

    "Play-based learning that stimulates critical thinking and curiosity.":
        "Aprendizaje basado en el juego que estimula el pensamiento crítico y la curiosidad.",

    # Admission process
    "Once you've gathered all the necessary information, the next step is submitting an application. Our easy-to-follow application form helps us understand your child's needs and start the enrollment process.":
        "Una vez que hayas reunido toda la información necesaria, el siguiente paso es enviar una solicitud. Nuestro formulario de solicitud fácil de seguir nos ayuda a comprender las necesidades de tu hijo y comenzar el proceso de inscripción.",

    # Parent resources
    "Stay informed about all of our school's policies, procedures, and guidelines with our comprehensive Manual para Padres.":
        "Mantente informado sobre todas las políticas, procedimientos y pautas de nuestra escuela con nuestro completo Manual para Padres.",

    # About us - Staff
    "Brandon ensures that all learning programs are designed to foster growth.":
        "Brandon asegura que todos los programas de aprendizaje estén diseñados para fomentar el crecimiento.",

    "Supporting students' emotional and social development, providing guidance":
        "Apoyando el desarrollo emocional y social de los estudiantes, brindando orientación",

    # History
    "The kindergarten opened its doors, starting with a small group of 30 children. The mission was to create a creative learning space for young minds.":
        "El jardín de infantes abrió sus puertas, comenzando con un pequeño grupo de 30 niños. La misión era crear un espacio de aprendizaje creativo para mentes jóvenes.",

    # Privacy policy
    "For students under the age of 13, we will obtain verifiable parental consent before collecting personal information, in accordance with applicable privacy laws such as COPPA (Children's Online Privacy Protection Act).":
        "Para estudiantes menores de 13 años, obtendremos el consentimiento parental verificable antes de recopilar información personal, de acuerdo con las leyes de privacidad aplicables como COPPA (Ley de Protección de la Privacidad en Línea de los Niños).",

    "Communication:</strong> To inform parents/guardians about their child":
        "Comunicación:</strong> Para informar a los padres/tutores sobre su hijo",
}

def translate_js_file(filepath, translations):
    """Apply translations to a JavaScript file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes = 0

        # Sort translations by length (longest first) to avoid partial replacements
        sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)

        for eng, esp in sorted_translations:
            if eng in content:
                # Count occurrences
                count = content.count(eng)
                content = content.replace(eng, esp)
                changes += count

        # Only write if there were changes
        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes

        return 0
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

def main():
    print("🔄 Traduciendo archivos JavaScript...\n")

    total_changes = 0
    files_modified = 0

    # Process all .mjs files
    js_dir = Path('assets/sites/49pSfmDl3bVFoyDoGQdiD9')
    if js_dir.exists():
        for js_file in js_dir.glob('*.mjs'):
            changes = translate_js_file(js_file, FINAL_TRANSLATIONS)
            if changes > 0:
                total_changes += changes
                files_modified += 1
                print(f"✅ {js_file.name}: {changes} traducciones aplicadas")

    print(f"\n📊 Resumen:")
    print(f"   Archivos JS modificados: {files_modified}")
    print(f"   Traducciones aplicadas: {total_changes}")
    print(f"\n✅ ¡Traducciones de JavaScript completadas!")

if __name__ == '__main__':
    main()
