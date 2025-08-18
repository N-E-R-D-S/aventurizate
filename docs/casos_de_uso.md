# 📑 Casos de Uso – Aventurízate (MVP)

## 👤 Actor: Turista

1. **Registrarse / Iniciar sesión**

   - El turista crea una cuenta o accede con credenciales.
   - Precondición: no estar registrado.
   - Resultado: tiene acceso personalizado a la plataforma.

2. **Consultar catálogo de aves**

   - El turista accede a una lista de aves con nombre, foto y descripción.
   - Puede seleccionar una ave específica para ver más información.

3. **Ver detalle de un ave**

   - El turista selecciona un ave del catálogo.
   - Sistema muestra descripción, foto, y en qué reservas puede observarse.

4. **Ver reservas naturales**

   - El turista consulta la lista de reservas.
   - Puede acceder a detalles básicos (nombre, ubicación, descripción).

5. **Consultar detalle de reserva**

   - El turista selecciona una reserva.
   - Sistema muestra: descripción, ubicación, aves disponibles, guías asociados.

6. **Consultar disponibilidad de guía**

   - El turista selecciona un guía en la reserva.
   - Sistema muestra fechas y disponibilidad.

7. **Hacer una reserva**

   - El turista elige: reserva + guía + fecha.
   - El sistema registra la solicitud de reserva con estado “pendiente”.

---

## 👤 Actor: Guía

1. **Registrarse / Iniciar sesión**

   - El guía crea su cuenta o accede con credenciales.
   - Define su rol como guía.

2. **Administrar perfil de guía**

   - El guía actualiza datos como: experiencia, idiomas, tarifas.
   - Aparece en el listado de guías disponibles en las reservas.

3. **Aceptar / Rechazar reserva**

   - El guía recibe notificación de una solicitud de reserva.
   - Puede aceptar (reserva confirmada) o rechazar (reserva cancelada).

---

## 👤 Actor: Operador

1. **Registrarse / Iniciar sesión**

   - El operador accede con rol de administrador de reservas.

2. **Registrar reserva natural**

   - El operador da de alta una nueva reserva en el sistema.
   - Define: nombre, ubicación, descripción, actividades.

3. **Publicar evento / temporada**

   - El operador registra un evento (ej. festival, conteo ciudadano).
   - Relaciona el evento con una reserva natural.
