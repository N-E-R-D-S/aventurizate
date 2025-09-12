# 🌎 Aventurízate

**Plataforma de Aviturismo de Nicaragua**
_Hackathon Nicaragua 2025 - Reto Turismo_

**Aventurízate** es una plataforma web innovadora diseñada para potenciar el **aviturismo** en Nicaragua, integrando **conservación**, **turismo sostenible** y **desarrollo económico local**.

Conecta a turistas nacionales e internacionales con guías locales, facilita la exploración de reservas naturales protegidas y ofrece un catálogo digital completo de aves endémicas y migratorias, con información detallada, fotografías y mapas de distribución.

Además, permite gestionar reservas de tours especializados, promueve buenas prácticas de observación y contribuye a la educación ambiental, posicionándose como la herramienta definitiva para amantes de la naturaleza y profesionales del ecoturismo.

## 🚀 Objetivos

- Promover el **turismo sostenible** y la **conservación de la biodiversidad**.
- Facilitar la **observación de aves** y actividades ecoturísticas.
- Crear un espacio digital inclusivo para turistas, guías y operadores locales.

## ✨ Funcionalidades del MVP

### 1. Gestión de usuarios

- Registro e inicio de sesión para turistas y guías.
- Perfiles con datos personales, idiomas y país de origen.
- Roles definidos: **Turista** y **Guía**.

### 2. Catálogo de aves

- Listado de especies con nombre común, científico, descripción y fotografías.
- Información taxonómica (orden, familia, género).
- Clasificación por categoría de la Lista Roja UICN.

### 3. Reservas naturales

- Visualización de reservas con ubicación y descripción.
- Aves observables en cada reserva.

### 4. Tours y visitas guiadas

- Guías pueden publicar tours indicando fecha, cupo y precio.
- Turistas pueden explorar y reservar tours disponibles.
- Confirmación visual de reservas.

### 5. Reservas de tours

- Sistema de confirmación de participación para turistas.
- Visualización de participantes por tour (para guías).
- Historial de reservas para cada usuario.

## 🛠️ Tecnologías

- **Backend:** Django (Python)
- **Base de datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Frontend:** HTML, CSS, JavaScript (AlpineJS)
- **Otros:** Django Admin, manejo de imágenes, SlugField, mapas (por integrar)

## 🔗 Relaciones Clave entre Apps

- `User` ↔ `TouristProfile` / `GuideProfile`
- `Species` ↔ `Reserve` (ManyToMany)
- `GuideProfile` ↔ `Tour`
- `Tour` ↔ `TourReservation` ↔ `TouristProfile`

## ⚡ Cómo Ejecutar Localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/N-E-R-D-S/aventurizate.git
cd aveturizate
```

### 2. Crear y activar entorno virtual

```bash
python -m venv .env
source .env/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Inicializar datos base (idiomas, países, grupos)

```bash
python manage.py init_accounts
```

### 6. Cargar especies de aves desde GBIF (opcional)

```bash
python manage.py load_species
```

### 7. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar servidor local

```bash
python manage.py runserver
```

👉 Accede en tu navegador a: [http://localhost:8000](http://localhost:8000)

## 👥 Equipo

- **Deybis Meléndez** – Líder, Desarrollador FullStack
- **Junieth Soza** – Marketing y Comunicación
- **Ileana Ruiz** – Diseño Gráfico y UX
- **Nelson Córdoba** – Desarrollador Frontend

## 🚀 Sobre el Hackathon

Este proyecto fue desarrollado como parte del Hackathon Nicaragua, el evento de innovación tecnológica más grande del país que reúne a desarrolladores, diseñadores y emprendedores para crear soluciones digitales que respondan a desafíos reales de Nicaragua en un tiempo limitado.
El objetivo del hackathon es fomentar la creatividad, el trabajo colaborativo y el desarrollo de propuestas con impacto social, económico y ambiental.

## 🦜 ¿Por qué elegimos el reto de Aviturismo?

Nicaragua cuenta con una enorme riqueza natural y biodiversidad, especialmente en aves, que representan una oportunidad única para impulsar el ecoturismo y el desarrollo local. Sin embargo, esta potencialidad muchas veces no está articulada digitalmente, lo que limita su visibilidad y acceso.

Decidimos abordar el reto de "Plataforma de aviturismo" porque:

🌿 Queremos promocionar las áreas protegidas y la observación de aves como un producto turístico sostenible y atractivo.

📲 Buscamos centralizar en una plataforma amigable la información sobre especies, reservas, guías y tours, facilitando la planificación de experiencias para turistas nacionales e internacionales.

💼 Apoyamos la economía local al conectar directamente a guías certificados y operadores de turismo con visitantes interesados.

Con Aventurízate, no solo construimos una herramienta tecnológica, sino que contribuimos a posicionar a Nicaragua como un destino de naturaleza de clase mundial —potenciando el turismo responsable y el orgullo por nuestra biodiversidad.

## 📌 Próximos Pasos

- [ ] Integrar mapas de distribución por especie.
- [ ] Módulo educativo y de eventos (festivales, conteos).
- [ ] Implementar filtros avanzados en catálogos.
- [ ] Soporte multilenguaje básico.
- [ ] Sistema de valoraciones y comentarios para tours y guías.
