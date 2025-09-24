# Funcionalidades específicas del MVP Aventurízate

## 1. Gestión de usuarios

- Registro básico de turistas y guías con nombre, email, contraseña y rol.
- Inicio de sesión para turistas y guías.
- Validación de credenciales y manejo de errores (email duplicado, contraseña incorrecta).
- Roles:
  - Turista: puede explorar aves, reservas y tours.
  - Guía: puede crear y gestionar tours.

## 2. Catálogo de aves

- Listado de aves con:
  - Foto (si está disponible).
  - Nombre común y científico.
  - Breve descripción.
- Posibilidad de consultar detalle de cada ave.

## 3. Reservas naturales

- Listado de reservas naturales con:
  - Nombre.
  - Ubicación.
  - Breve descripción.
  - Aves que pueden observarse en cada reserva.

## 4. Tours / visitas guiadas

- Guías pueden:
  - Crear un tour con nombre, reserva asociada, fechas disponibles, cupo máximo y precio (opcional).
  - Publicar el tour para que los turistas lo vean.
  - Visualizar sus tours publicados y número de participantes.
- Turistas pueden:
  - Explorar los tours disponibles.
  - Seleccionar un tour y confirmar participación.
  - Ver confirmación de reserva en pantalla.

## 5. Interfaz y navegación

- Menú principal: Inicio | Aves | Reservas Naturales | Tours | Ingresar.
- Flujo intuitivo y minimalista.
- Diseño demo-friendly con HTML + CSS (o Tailwind/Bootstrap).

## 6. Extras opcionales (si hay tiempo)

- Relación de aves con al menos una reserva natural.
- Calendario de eventos o festivales de aves.
- Módulo educativo con un artículo de prueba.
