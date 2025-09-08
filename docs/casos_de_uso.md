# Casos de Uso del MVP Aventurízate

## 1. Gestión de usuarios

### Caso de Uso 1.1: Registro de usuario

**Actor:** Turista / Guía  
**Descripción:** Permite a un usuario registrarse con nombre, email, contraseña y rol.  
**Precondición:** El email no debe estar registrado.  
**Flujo principal:**

1. Usuario ingresa datos en el formulario de registro.
2. Sistema valida la información.
3. Sistema guarda los datos en la base de datos.
4. Usuario recibe confirmación de registro.  
   **Flujo alternativo:** Email ya registrado → sistema muestra error.

### Caso de Uso 1.2: Inicio de sesión

**Actor:** Turista / Guía  
**Descripción:** Permite a los usuarios autenticarse con email y contraseña.  
**Precondición:** El usuario debe estar registrado.  
**Flujo principal:**

1. Usuario ingresa email y contraseña.
2. Sistema valida credenciales.
3. Acceso concedido según rol (turista o guía).  
   **Flujo alternativo:** Contraseña incorrecta → sistema muestra error.

## 2. Exploración de aves

### Caso de Uso 2.1: Listar aves

**Actor:** Turista  
**Descripción:** Visualizar el listado de aves con foto, nombre común y científico.  
**Flujo principal:**

1. Usuario accede a la sección de aves.
2. Sistema muestra listado con información básica de cada ave.

### Caso de Uso 2.2: Consultar detalle de un ave

**Actor:** Turista  
**Descripción:** Visualizar información completa de un ave seleccionada.  
**Flujo principal:**

1. Usuario selecciona un ave del listado.
2. Sistema muestra detalles: foto, nombres y descripción.

## 3. Exploración de reservas naturales

### Caso de Uso 3.1: Listar reservas naturales

**Actor:** Turista  
**Descripción:** Visualizar reservas naturales con nombre, ubicación y breve descripción.  
**Flujo principal:**

1. Usuario accede a la sección de reservas.
2. Sistema muestra listado de reservas.

### Caso de Uso 3.2: Consultar aves de una reserva

**Actor:** Turista  
**Descripción:** Visualizar aves que pueden observarse en una reserva específica.  
**Flujo principal:**

1. Usuario selecciona una reserva.
2. Sistema muestra listado de aves asociadas.

## 4. Gestión de tours y visitas guiadas

### Caso de Uso 4.1: Crear tour

**Actor:** Guía  
**Descripción:** Permite a los guías crear un tour indicando nombre, reserva, fecha, hora, cupo y precio.  
**Flujo principal:**

1. Guía completa el formulario de creación de tour.
2. Sistema valida la información y guarda el tour.
3. Tour aparece publicado para turistas.

### Caso de Uso 4.2: Listar tours

**Actor:** Turista  
**Descripción:** Permite a los turistas explorar los tours disponibles.  
**Flujo principal:**

1. Usuario accede a la sección de tours.
2. Sistema muestra listado con nombre, guía, fecha, reserva y cupo disponible.

## 5. Reservas de tours

### Caso de Uso 5.1: Reservar tour

**Actor:** Turista  
**Descripción:** Permite a los turistas reservar un tour.  
**Precondición:** Debe existir cupo disponible.  
**Flujo principal:**

1. Turista selecciona un tour.
2. Sistema verifica disponibilidad de cupo.
3. Reserva se registra en la base de datos.
4. Sistema muestra confirmación visual.

### Caso de Uso 5.2: Ver reservas realizadas

**Actor:** Turista  
**Descripción:** Permite al turista visualizar sus reservas realizadas.  
**Flujo principal:**

1. Usuario accede a su perfil.
2. Sistema muestra listado de reservas activas y confirmadas.

### Caso de Uso 5.3: Ver participantes de un tour

**Actor:** Guía  
**Descripción:** Permite al guía visualizar los participantes de un tour publicado.  
**Flujo principal:**

1. Guía accede a sus tours publicados.
2. Sistema muestra listado de participantes por tour.

## 6. Perfil de usuario

### Caso de Uso 6.1: Ver perfil

**Actor:** Turista / Guía  
**Descripción:** Visualizar datos básicos de usuario y su actividad.  
**Flujo principal:**

1. Usuario accede a su perfil.
2. Sistema muestra nombre, email, rol y tours o reservas correspondientes.

## 7. Extras futuros (opcional)

- Calendario de eventos y tours.
- Gestión de pagos online.
- Módulo educativo sobre aves y conservación.
- Búsqueda avanzada por aves, reservas y tours.
- Comentarios o reseñas de turistas sobre tours y guías.
