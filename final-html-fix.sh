#!/bin/bash

# Fix all remaining English content in HTML files

for file in *.html; do
  echo "Processing $file..."

  # Main phrases with regular apostrophe (not curly quote)
  sed -i.backup \
    -e "s/Every moment in your child's early years is crucial\. Our programs are designed to inspire curiosity, and build essential skills that will last a lifetime\./Cada momento en los primeros años de tu hijo es crucial. Nuestros programas están diseñados para inspirar curiosidad y desarrollar habilidades esenciales que durarán toda la vida./g" \
    -e "s/Every moment in your child's early years are crucial for their growth and development\./Cada momento en los primeros años de tu hijo es crucial para su crecimiento y desarrollo./g" \
    -e "s/Your Child's New Journey?/¿El Nuevo Viaje de tu Hijo?/g" \
    -e "s/Welcome & Learning/Bienvenida y Aprendizaje/g" \
    -e "s/Head Teacher/Maestro Principal/g" \
    -e "s/Physical Education Teacher/Maestro de Educación Física/g" \
    -e "s/Enroll now/Inscríbete ahora/g" \
    -e "s/1-2 years\./1-2 años./g" \
    -e "s/>1-2 years</>1-2 años</g" \
    "$file"
done

echo "✅ All HTML files processed"

# Clean up backup files
rm *.backup 2>/dev/null
rm *.bak 2>/dev/null
rm *.bak2 2>/dev/null

echo "✅ Backup files cleaned"
