# 🔑 Rol del Registro de Usuarios

El **registro de usuarios** es el eje que conecta las funcionalidades:

- **Turistas (user role = tourist)**

  - Acceden al catálogo de aves y reservas.
  - Consultan el calendario de eventos.
  - Hacen reservas con guías locales.
  - Guardan sus avistamientos favoritos.

- **Guías locales (user role = guide)**

  - Crean y administran su perfil (experiencia, idiomas, precios).
  - Reciben solicitudes de reservas de turistas.
  - Publican reportes de avistamientos o notas educativas.

- **Operadores / administradores de reservas (user role = operator)**

  - Registran reservas naturales y actividades disponibles.
  - Publican eventos en el calendario (festivales, conteos).
  - Validan perfiles de guías locales.

Así, el registro de usuario no es solo un “login”, sino un **punto de personalización**: cada usuario ve la plataforma según su rol.

---

# 🔗 Flujo de Relación entre Funcionalidades

1. **Catálogo de aves**

   - Público (cualquiera lo puede consultar).
   - Se conecta con reservas: “Dónde ver esta especie”.
   - Se conecta con calendario: “Cuándo ver esta especie (temporada)”.

2. **Reservas naturales**

   - Listado accesible a todos.
   - Relacionadas con aves (qué especies hay en cada reserva).
   - Relacionadas con guías (qué guías trabajan allí).
   - Relacionadas con eventos (qué actividades pasan allí).

3. **Calendario de temporadas y eventos**

   - Turistas ven próximos festivales y temporadas.
   - Operadores crean eventos.
   - Guías se asocian a eventos para ofrecer tours.

4. **Sistema de reservas**

   - Turista selecciona: reserva + guía + fecha.
   - El sistema genera un `Booking`.
   - El guía acepta/rechaza.
   - Operador recibe notificación si es dentro de su reserva.

5. **Módulo educativo**

   - Artículos y buenas prácticas.
   - Se enlaza con catálogo de aves (“conservación de esta especie”) y con reservas (“qué hacer y qué no en esta zona”).
   - Turistas lo consultan antes de reservar.
   - Guías pueden aportar artículos o experiencias.

---

# 🔄 Ejemplo de Flujo Completo (Caso de Uso)

1. Un **turista** entra → se registra.
2. Consulta el **catálogo de aves** y ve que el quetzal se observa en la Reserva Indio Maíz en marzo.
3. Revisa la **reserva natural** y ve qué actividades hay.
4. Consulta el **calendario** y descubre que hay un festival de aves ese mismo mes.
5. Va al **sistema de reservas** y contrata un **guía local certificado** para una fecha dentro del festival.
6. Antes del viaje, lee el **módulo educativo** con recomendaciones de conservación.
7. Después, deja una reseña en el perfil del guía.

---

# 🎯 Conclusión

El **registro de usuarios** permite diferenciar roles y personalizar la experiencia:

- Turistas → reservan y aprenden.
- Guías → ofrecen servicios y educan.
- Operadores → administran información y eventos.

Cada funcionalidad está enlazada: **Aves ↔ Reservas ↔ Eventos ↔ Guías ↔ Reservas de usuarios**, con la educación como eje transversal.
