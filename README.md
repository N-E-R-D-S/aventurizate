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

## 🧩 Módulos y Modelos

### `accounts/` - Usuarios y Perfiles

**Modelos:**

- `User` (hereda de `AbstractUser`) – Maneja credenciales, roles, idiomas y biografía.
- `TouristProfile` – Perfil con país de origen.
- `GuideProfile` – Perfil con teléfono, años de experiencia y calificación.
- `Language`, `Country` – Idiomas y países disponibles.

### `birds/` - Aves

**Modelos:**

- `IUCNRedListCategory` – Categoría de conservación.
- `Order`, `Family`, `Genus`, `Species` – Estructura taxonómica.
- `Photo` – Imágenes asociadas a aves.

### `reserves/` - Reservas Naturales

**Modelos:**

- `Reserve` – Nombre, descripción, ubicación, aves asociadas.
- `ReservePhoto` – Galería de imágenes por reserva.

### `tours/` - Tours y Reservas

**Modelos:**

- `Tour` – Guía, nombre, descripción, fecha, cupo, precio y publicación.
- `TourReservation` – Turista, tour, confirmación y fecha de reserva.

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

## 💡 Sobre el Proyecto

Este proyecto participa en el **Hackathon Nicaragua 2025**, bajo el reto de **Turismo**.
Buscamos aportar al **desarrollo sostenible**, la **conservación de ecosistemas** y el **fortalecimiento de economías locales** a través del aviturismo.

## 📌 Próximos Pasos

- [ ] Integrar mapas de distribución por especie.
- [ ] Módulo educativo y de eventos (festivales, conteos).
- [ ] Implementar filtros avanzados en catálogos.
- [ ] Soporte multilenguaje básico.
- [ ] Sistema de valoraciones y comentarios para tours y guías.
