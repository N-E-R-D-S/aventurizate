# 🌎 Aventurízate

**Plataforma de Aviturismo y Reservas Naturales de Nicaragua**  
_Hackathon Nicaragua 2025 - Reto Turismo_

**Aventurízate** es un proyecto que busca impulsar el **aviturismo** como motor económico sostenible y herramienta de conservación en Nicaragua.

La aplicación permitirá **promocionar reservas naturales**, **centralizar información de especies de aves**, y **conectar a turistas con guías locales certificados**, fomentando el ecoturismo responsable.

El proyecto busca impulsar el **aviturismo** como motor económico sostenible y herramienta de conservación en Nicaragua.

---

## 🚀 Objetivos

- Promover el **turismo sostenible** y la **conservación de la biodiversidad** en Nicaragua.
- Facilitar la **observación de aves** y actividades ecoturísticas a turistas nacionales e internacionales.
- Brindar un **espacio digital accesible** para operadores locales, investigadores y aficionados al aviturismo.

---

## ✨ Funcionalidades Principales (TODO)

1. **Registro de usuario** (turistas, guías locales, operadores).
2. **Catálogo digital de aves** endémicas y migratorias con fotografías, descripciones y mapas de distribución.
3. **Información de reservas naturales** habilitadas para actividades de ecoturismo.
4. **Calendario de temporadas y eventos**: avistamiento de aves, festivales y conteos ciudadanos.
5. **Sistema de reservas en línea** para contratar guías locales certificados y servicios complementarios.
6. **Módulo educativo** con recursos de conservación y buenas prácticas ambientales.

---

## 🛠️ Tecnologías

- **Backend:** Django (Python)
- **Base de datos:** SQLite (modo desarrollo), PostgreSQL (modo producción)
- **Frontend:** HTML, CSS, JavaScript/AlpineJS
- **Otros:** Librerías de geolocalización y mapas para distribución de especies (Pendiente escoger)

---

## 📌 Próximos Pasos

- [ ] Definir modelos iniciales (Usuarios, Aves, Reservas, Eventos, Guías).
- [ ] Implementar autenticación y registro de usuarios.
- [ ] Diseñar catálogo inicial de aves en base de datos.
- [ ] Configurar vistas y primeras plantillas.
- [ ] Preparar prototipo funcional para pruebas en el hackathon.

---

## 👥 Equipo

- **Deybis Melendez** – Líder, Desarrollador
- **Junieth Soza** – Marketing y Comunicación
- **Ileana Ruiz** – Diseño Gráfico
- **Nelson Córdoba** – Desarrollador

---

## 🤝 Equipo & Comunidad

Este proyecto forma parte del **Hackathon Nicaragua 2025**, en la categoría de **Turismo**.  
Buscamos que esta plataforma sea un aporte al **desarrollo sostenible**, la **conservación ambiental** y el **fortalecimiento de la economía local** a través del aviturismo.

## 📂 Descripción de Apps y Modelos (En Desarrollo)

### 1. `accounts/`

🔑 Manejo de usuarios y roles.
**Modelos:**

- `User` (extiende `AbstractUser`, con roles: tourist, guide, operator).
- `Profile` (información adicional de cada usuario).

---

### 2. `birds/`

🐦 Catálogo digital de aves.
**Modelos:**

- `Bird` → common_name, scientific_name, description, photo, category, distribution.

---

### 3. `reserves/`

🌳 Reservas naturales habilitadas para el aviturismo.
**Modelos:**

- `Reserve` → name, location, description, activities, photos.

---

### 4. `events/`

📅 Temporadas y eventos especiales.
**Modelos:**

- `Event` → title, date, location, type (festival, citizen_count, season), description.

---

### 5. `bookings/`

🎟️ Sistema de reservas (turistas ↔ guías).
**Modelos:**

- `Booking` → user (turista), guide, reserve, date, status.

---

### 6. `education/`

📘 Módulo educativo sobre conservación.
**Modelos:**

- `Article` → title, content, category, image, published_date.

---

## 🔗 Relaciones entre Apps

- `accounts.User` ↔ `bookings.Booking` (turista hace una reserva).
- `accounts.User` (guide) ↔ `bookings.Booking` (guía asignado).
- `birds.Bird` ↔ `reserves.Reserve` (aves observables en una reserva).
- `events.Event` ↔ `reserves.Reserve` (dónde ocurre el evento).

---

## ⚡ Cómo Ejecutar Localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/deybismelendez/aveturizate.git
cd aveturizate
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Inicializar grupos, idiomas y países por default.

```bash
python manage.py init_accounts
```

### 6. Generar catálogo de aves con GBIF API (Opcional).

```bash
python manage.py load_species
```

### 7. Crear un superusuario (opcional, para entrar al admin)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el servidor local

```bash
python manage.py runserver
```

👉 Accede en tu navegador a: http://localhost:8000
