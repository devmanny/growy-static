# 📋 GROWY ACADEMY - LISTA DE PENDIENTES

> **Última actualización:** 8 de Noviembre, 2025
> **Estado del proyecto:** MVP Base Completado - Fase de Configuración

---

## 🎯 PRIORIDAD ALTA - Hacer HOY

### 1. ⚙️ Configurar Calendly
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 10 minutos
**Archivo afectado:** `agendar.html` (línea 242)

**Pasos:**
1. Ir a https://calendly.com
2. Crear cuenta gratuita (o iniciar sesión)
3. Crear nuevo evento:
   - **Nombre:** "Diagnóstico Gratuito Growy"
   - **Duración:** 45 minutos
   - **Tipo:** Presencial
   - **Ubicación:** Brasilia 2876, Local 18, Colomos Providencia, 44620 Guadalajara, Jal.
   - **Descripción:** "Evaluación personalizada sin costo para identificar las necesidades de tu hijo"
4. Copiar la URL del evento (ej: `calendly.com/growy-academy/diagnostico-growy`)
5. Actualizar en `agendar.html` línea 242:
   ```html
   data-url="https://calendly.com/TU_USUARIO/diagnostico-growy?hide_gdpr_banner=1&primary_color=00d2e0"
   ```
   Reemplazar `TU_USUARIO` con tu usuario real

**Resultado esperado:** Calendario funcional donde los padres pueden agendar citas

---

### 2. 📸 Actualizar Imágenes Reales
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 30 minutos
**Archivos afectados:** `index-nuevo.html`

**Imágenes necesarias:**
- [ ] **Hero principal:** Foto del espacio Growy o niño aprendiendo (600x400px mínimo)
- [ ] **Logo Growy:** Si tienes logo propio (SVG preferido)
- [ ] **Casos de éxito:** Fotos genéricas de niños (con permisos) o ilustraciones

**Ubicación actual (línea 499 en index-nuevo.html):**
```html
<img src="https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600"
     alt="Niño aprendiendo con confianza en Growy">
```

**Cómo actualizar:**
1. Guardar tu foto en: `assets/images/hero-growy.jpg`
2. Cambiar la línea 499 a:
   ```html
   <img src="assets/images/hero-growy.jpg" alt="Niño aprendiendo en Growy Academy">
   ```

---

### 3. 🔗 Actualizar Enlaces de Redes Sociales
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 5 minutos
**Archivo afectado:** `index-nuevo.html` (líneas 635-637)

**Ubicación actual (footer):**
```html
<a href="#">Facebook</a>
<a href="#">Instagram</a>
<a href="#">TikTok</a>
```

**Actualizar con tus URLs reales:**
```html
<a href="https://facebook.com/TU_PAGINA" target="_blank">Facebook</a>
<a href="https://instagram.com/TU_PERFIL" target="_blank">Instagram</a>
<a href="https://tiktok.com/@TU_USUARIO" target="_blank">TikTok</a>
```

---

## 🚀 PRIORIDAD MEDIA - Esta Semana

### 4. 🗺️ Añadir Google Maps
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 15 minutos
**Beneficio:** Los padres pueden ver ubicación exacta y obtener direcciones

**Implementación:**
1. Ir a https://www.google.com/maps
2. Buscar: "Brasilia 2876, Colomos Providencia, Guadalajara"
3. Click en "Compartir" → "Insertar un mapa"
4. Copiar el código `<iframe>`
5. Añadir en `index-nuevo.html` en el footer o crear sección "Cómo llegar"

**Código ejemplo:**
```html
<section class="location" id="ubicacion">
    <div class="container">
        <h2>Encuéntranos</h2>
        <div style="max-width: 800px; margin: 0 auto;">
            <iframe
                src="https://www.google.com/maps/embed?pb=TU_CODIGO_AQUI"
                width="100%"
                height="450"
                style="border:0; border-radius: 15px;"
                allowfullscreen=""
                loading="lazy">
            </iframe>
        </div>
    </div>
</section>
```

---

### 5. 📊 Configurar Google Analytics
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 20 minutos
**Beneficio:** Trackear visitas, conversiones, y comportamiento de usuarios

**Pasos:**
1. Ir a https://analytics.google.com
2. Crear cuenta/propiedad para "Growy Academy"
3. Obtener el ID de medición (formato: G-XXXXXXXXXX)
4. Añadir ANTES de `</head>` en ambos archivos HTML:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');

  // Track eventos personalizados
  function trackEvent(category, action, label) {
    gtag('event', action, {
      'event_category': category,
      'event_label': label
    });
  }
</script>
```

**Eventos a trackear:**
- Click en "Agendar Diagnóstico"
- Click en WhatsApp
- Tiempo en página
- Scroll hasta casos de éxito

---

### 6. 📱 Configurar Meta Pixel (Facebook)
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 15 minutos
**Beneficio:** Remarketing en Facebook/Instagram

**Pasos:**
1. Ir a https://business.facebook.com/events_manager
2. Crear Pixel para "Growy Academy"
3. Copiar el código base
4. Añadir DESPUÉS de `<head>` en ambos HTML:

```html
<!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'TU_PIXEL_ID');
  fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" style="display:none"
       src="https://www.facebook.com/tr?id=TU_PIXEL_ID&ev=PageView&noscript=1"/>
</noscript>
<!-- End Meta Pixel Code -->
```

**Eventos a trackear:**
- PageView (automático)
- Lead (cuando llenan formulario)
- Schedule (cuando agendaran en Calendly)

---

### 7. 📄 Crear Página "Nuestra Historia"
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 45 minutos
**Archivo a crear:** `historia.html`

**Contenido necesario:**
- [ ] Timeline 2020-2025 (¿cuándo empezaste?)
- [ ] TU historia personal (por qué creaste Growy)
- [ ] Fotos del espacio
- [ ] Foto tuya o del equipo
- [ ] Misión y Visión (ya las tienes):
  ```
  MISIÓN: Ayudamos a cada niño a aprender con confianza y alegría,
  ofreciendo clases personalizadas que se adaptan a su ritmo y necesidades.

  VISIÓN: Ser una academia reconocida por transformar el aprendizaje en
  una experiencia positiva e inclusiva.
  ```
- [ ] Valores (inclusión, personalización, amor por aprender, etc.)

**Estructura sugerida:**
1. Hero con foto tuya/del equipo
2. "Por qué existe Growy" (tu historia personal)
3. Timeline visual (2020-2025)
4. Misión y Visión
5. Equipo (si aplica)
6. CTA: "Conoce cómo podemos ayudarte"

---

### 8. 📝 Crear Página "Casos de Éxito" Completa
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 1 hora
**Archivo a crear:** `casos-exito.html`

**Contenido necesario para cada caso:**
- [ ] Edad del niño (sin nombre)
- [ ] Problema inicial
- [ ] Proceso (cuánto tiempo, qué hicieron)
- [ ] Resultado específico (antes/después académico)
- [ ] Testimonio de mamá/papá (EN VIDEO si es posible - ORO PURO)
- [ ] Foto genérica (sin rostros identificables)

**Estructura:**
```
Caso #1: Niña de 7 años con dificultad lectora
├── Situación inicial: "No podía leer una oración completa"
├── Diagnóstico Growy: Dislexia leve
├── Plan personalizado: 12 semanas, 2 sesiones/semana
├── Resultado: Ahora lee libros completos y es la mejor de su clase
└── Testimonio mamá: [VIDEO 30 seg o texto]
```

**Mínimo 4 casos, ideal 6-8**

---

## 🎨 PRIORIDAD BAJA - Próximas 2 Semanas

### 9. 📱 Menu Hamburguesa para Mobile
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 30 minutos
**Beneficio:** Navegación mobile más usable

Actualmente el menú desaparece en mobile. Necesita:
- Icono hamburguesa (☰)
- Menu slide-in
- Animación suave

---

### 10. 🎥 Sección de Video
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 1 hora (incluyendo grabación)
**Beneficio:** MÁXIMO IMPACTO - Video de 60 segundos tuyo

**Contenido del video:**
- "Hola, soy Zahira de Growy Academy"
- Por qué haces lo que haces (historia personal - 20 seg)
- Qué hace Growy diferente (personalización - 20 seg)
- Llamado a acción (agenda tu diagnóstico - 10 seg)

**Dónde agregarlo:** Justo después del Hero en `index-nuevo.html`

**Tips:**
- Luz natural
- Fondo del espacio Growy
- Audio claro (usar micrófono de audífonos)
- Ser AUTÉNTICA (no actuar, ser tú)

---

### 11. 📰 Blog/Recursos (Content Marketing)
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 2-3 horas por post
**Beneficio:** SEO + autoridad + lead magnet

**Primeros 3 posts sugeridos:**

**POST 1:** "5 Señales de que tu Hijo Necesita Apoyo en Lectura"
- Target keyword: "problemas lectura niños guadalajara"
- 800-1000 palabras
- Lista numerada
- Incluir CTA: "Diagnóstico gratuito"

**POST 2:** "Autismo y Educación: Guía para Padres Primerizos"
- Target keyword: "educación autismo guadalajara"
- 1200 palabras
- Empatía + información práctica
- Casos reales (sin nombres)

**POST 3:** "Cómo Hablar con tu Hijo sobre sus Dificultades de Aprendizaje"
- Target keyword: "dificultades aprendizaje niños"
- 1000 palabras
- Tips accionables
- Lenguaje empático

---

### 12. 🎁 Lead Magnet
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 3 horas
**Beneficio:** Captar emails para newsletter

**Crear PDF descargable:**
"10 Juegos para Mejorar la Lectura en Casa"

**Contenido:**
- Portada diseñada
- 10 juegos prácticos (con instrucciones)
- Materiales necesarios (cosas que ya tienen en casa)
- Tips de implementación
- CTA final: "¿Necesitas más apoyo? Agenda diagnóstico"

**Implementación:**
- Popup en home (después de 30 segundos)
- Formulario simple: Nombre + Email
- Envío automático del PDF por email
- Agregar a lista de MailChimp/Brevo

---

### 13. 🌟 Programa de Referidos
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 4 horas (con diseño)
**Beneficio:** Mamá feliz trae mamá

**Mecánica:**
- Mamá actual refiere a nueva mamá
- Nueva mamá agenda diagnóstico y menciona quién la refirió
- Mamá que refirió recibe: ¿1 clase gratis? ¿Descuento? ¿Regalo?
- Nueva mamá también recibe beneficio (ej: 10% descuento primer mes)

**Necesita:**
- Página explicativa
- Sistema de tracking (puede ser manual al inicio)
- Códigos de referido únicos
- Material gráfico para compartir en WhatsApp

---

### 14. 🎯 Landing Pages Específicas (SEO Local)
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 2 horas cada una
**Beneficio:** Captar búsquedas específicas en Google

**Páginas a crear:**

1. **"Clases para Niños con Autismo en Guadalajara"**
   - URL: `/autismo-guadalajara`
   - Keyword: "clases autismo guadalajara"
   - Contenido: Enfoque en TEA, métodos especializados, casos

2. **"Apoyo Escolar Personalizado Guadalajara"**
   - URL: `/apoyo-escolar-guadalajara`
   - Keyword: "regularización personalizada guadalajara"
   - Contenido: 1-a-1, planes personalizados

3. **"Dificultades de Aprendizaje Guadalajara"**
   - URL: `/dificultades-aprendizaje-guadalajara`
   - Keyword: "dificultades aprendizaje niños guadalajara"
   - Contenido: Dislexia, disgrafía, discalculia

**Estructura de cada landing:**
- Hero específico al problema
- Beneficios
- Proceso
- Casos de éxito relacionados
- CTA: Diagnóstico gratuito

---

### 15. 📧 Email Automation
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 4 horas
**Beneficio:** Nutrir leads automáticamente

**Secuencia post-agendar (7 emails):**

**Email 1** (inmediato): Confirmación de cita
**Email 2** (1 día antes): Recordatorio + qué llevar
**Email 3** (después de diagnóstico): Resumen + siguiente paso
**Email 4** (+3 días): Caso de éxito similar
**Email 5** (+7 días): FAQ sobre el programa
**Email 6** (+14 días): Oferta especial (si no se inscribió)
**Email 7** (+30 días): "¿Cómo está tu hijo? Te extrañamos"

**Herramienta:** MailChimp (gratis hasta 500 contactos) o Brevo

---

### 16. 🔍 SEO Técnico
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 2 horas
**Beneficio:** Mejor posicionamiento en Google

**Checklist:**

- [ ] **Sitemap.xml** generado y subido
- [ ] **Robots.txt** configurado
- [ ] **Google Search Console** verificado
- [ ] **Meta descriptions** en todas las páginas (150-160 caracteres)
- [ ] **Schema markup** para negocio local:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "Growy Academy",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Brasilia 2876, Local 18",
      "addressLocality": "Guadalajara",
      "addressRegion": "Jalisco",
      "postalCode": "44620"
    },
    "telephone": "+52-33-4369-0524",
    "url": "https://growy.mx"
  }
  ```
- [ ] **Open Graph tags** para compartir en redes
- [ ] **Velocidad de carga** optimizada (comprimir imágenes)
- [ ] **HTTPS** configurado (certificado SSL)

---

### 17. 🎨 Certificaciones/Credenciales Visibles
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 30 minutos
**Beneficio:** Aumenta confianza

**Añadir sección en Home:**
- Certificaciones tuyas (educación especial, etc.)
- Años de experiencia
- Instituciones donde has trabajado
- Metodologías que usas (Montessori, ABA, etc.)

**Diseño:** Logos pequeños con tooltips explicativos

---

### 18. 💬 Chat en Vivo (opcional pero poderoso)
**Estado:** ⏳ PENDIENTE
**Tiempo estimado:** 1 hora setup
**Beneficio:** Respuesta inmediata = más conversión

**Opciones:**

**OPCIÓN A - WhatsApp Business API (gratis):**
- Widget de chat que abre WhatsApp
- Mensajes pre-configurados
- Herramienta: https://elfsight.com/whatsapp-chat-widget/

**OPCIÓN B - Tidio/Tawk.to (gratis):**
- Chat real en el sitio
- Respuestas automáticas
- Historial de conversaciones
- App móvil para responder

---

## 🎯 MÉTRICAS A TRACKEAR (cuando Analytics esté activo)

### KPIs Semanales:
- [ ] **Visitas totales** (meta: +20% mes a mes)
- [ ] **Tasa de conversión Home → Agendar** (meta: 15-25%)
- [ ] **Tiempo promedio en Home** (meta: >2 min)
- [ ] **Porcentaje que llega a "Agendar"** (meta: >40%)
- [ ] **Bounce rate** (meta: <50%)
- [ ] **Clicks en WhatsApp** (trackear todo)
- [ ] **Diagnósticos agendados/semana** (meta: 5-10)
- [ ] **Conversión diagnóstico → inscripción** (meta: >60%)

### Reportes Mensuales:
- Fuentes de tráfico (Google, Facebook, directo, etc.)
- Páginas más visitadas
- Palabras clave que traen tráfico
- Dispositivos (mobile vs desktop)
- Horarios de mayor tráfico

---

## 📱 SOCIAL MEDIA (contenido recomendado)

### Publicar 3x por semana:

**Lunes:** Tip educativo
- "¿Sabías que...?"
- Dato sobre aprendizaje infantil
- Consejo rápido para papás

**Miércoles:** Caso de éxito (sin nombres)
- Antes/después
- Celebrar logros
- Humanizar el proceso

**Viernes:** Behind the scenes
- Foto del espacio
- Materiales que usan
- Equipo trabajando
- Momentos reales

**Formato:**
- Carrusel (mejor alcance que foto sola)
- Reels cortos (30-60 seg)
- Historias diarias

---

## 🚨 BUGS/FIXES TÉCNICOS

### Detectados:
1. [ ] Menu desaparece en mobile (index-nuevo.html)
2. [ ] Link "Ver Más Casos de Éxito" apunta a # (necesita href correcto)
3. [ ] Falta favicon en algunos navegadores
4. [ ] Calendly widget puede verse cortado en algunos mobile

### Por revisar:
- [ ] Compatibilidad Safari iOS
- [ ] Compatibilidad Internet Explorer (¿importa?)
- [ ] Velocidad de carga en 3G/4G
- [ ] Accesibilidad (contraste colores, screen readers)

---

## 📞 CONTACTOS/SERVICIOS NECESARIOS

### Pendientes de contratar/configurar:
- [ ] **Dominio:** growy.mx o growy.academy (GoDaddy/Namecheap)
- [ ] **Hosting:** Vercel (gratis) o Netlify (gratis) o DigitalOcean ($5/mes)
- [ ] **Email profesional:** hola@growy.mx (Google Workspace $6/mes)
- [ ] **Número comercial:** ¿Separar personal de comercial?
- [ ] **CRM:** HubSpot (gratis) para organizar leads
- [ ] **Email marketing:** MailChimp (gratis hasta 500) o Brevo
- [ ] **Calendly:** Plan gratis OK por ahora, Pro ($12/mes) después
- [ ] **Almacenamiento fotos:** Google Photos o Cloudinary

---

## 💰 PRESUPUESTO ESTIMADO (mensual)

### Mínimo viable:
- Dominio: $15/año = $1.25/mes
- Hosting: $0 (Vercel/Netlify gratis)
- Calendly: $0 (gratis)
- Email marketing: $0 (MailChimp gratis)
- **TOTAL: ~$2/mes** ✅

### Recomendado:
- Dominio: $15/año = $1.25/mes
- Hosting: $0 (Vercel)
- Email profesional: $6/mes
- Calendly Pro: $12/mes
- Meta Ads: $100/mes (cuando estés lista)
- **TOTAL: ~$120/mes**

---

## ✅ COMPLETADOS (para referencia)

- [x] Sitio traducido 100% al español
- [x] Datos de contacto reales integrados
- [x] WhatsApp: 33 4369 0524
- [x] Email: zahira.romo8@gmail.com
- [x] Dirección: Brasilia 2876, Local 18, Guadalajara
- [x] Hero con copy emocional
- [x] Casos de éxito (4 casos base)
- [x] Proceso de 6 pasos
- [x] Página de agendar con Calendly embed
- [x] WhatsApp flotante
- [x] Diseño responsive
- [x] CTAs estratégicos
- [x] Social proof

---

## 📝 NOTAS IMPORTANTES

### Filosofía del proyecto:
> "No vendas clases. Vende transformación.
> No ofrezcas apoyo académico. Ofrece el momento en que una mamá
> ve a su hijo sonreír mientras lee por primera vez."

### Recordatorios:
- **Mobile-first:** 70% de mamás buscan desde celular
- **Velocidad:** Cada segundo de carga = -7% conversión
- **Autenticidad > Perfección:** Fotos reales > stock photos
- **Trackear TODO:** Lo que no se mide, no se puede mejorar

---

## 🎯 ROADMAP SUGERIDO

### Semana 1 (AHORA):
1. Configurar Calendly ⭐⭐⭐
2. Actualizar imágenes reales ⭐⭐
3. Links redes sociales ⭐
4. Google Analytics ⭐⭐

### Semana 2:
1. Página "Nuestra Historia"
2. Google Maps
3. Menu mobile
4. Meta Pixel

### Semana 3:
1. Blog (primer post)
2. Lead magnet PDF
3. SEO técnico básico

### Semana 4:
1. Casos de éxito completos
2. Video personal
3. Email automation básica

### Mes 2:
1. Landing pages específicas
2. Programa de referidos
3. Chat en vivo
4. A/B testing de CTAs

---

## 🆘 AYUDA/RECURSOS

### Si necesitas ayuda con:
- **Diseño gráfico:** Canva (gratis) - plantillas profesionales
- **Fotos:** Unsplash/Pexels (gratis) - mientras consigues las tuyas
- **Videos:** CapCut (gratis) - edición fácil para reels
- **Copiar texto:** ChatGPT - pero personaliza con tu voz
- **Analytics:** Google Skillshop - cursos gratis
- **SEO:** Moz Beginner's Guide - guía completa gratis

### Comunidades útiles:
- Grupo de Facebook de emprendedores edu-tech México
- /r/entrepreneur en Reddit
- LinkedIn grupos de educación especial

---

## 📧 CONTACTO DEL PROYECTO

**Desarrollador:** [Tu nombre/contacto]
**Cliente:** Growy Academy (Zahira)
**Inicio:** Noviembre 2025
**Repositorio:** `/Users/manny/Projects/growy/growy-static`

---

> **Última actualización:** 8 Nov 2025, 8:45 PM
> **Versión:** 1.0
> **Estado:** En progreso - MVP funcional

**¿Preguntas? ¿Prioridades diferentes? Actualiza este doc. 📝**