# ✅ Requisitos para el MVP de **Aventurízate**

## 1. **Usuarios y Autenticación**

- Registro e inicio de sesión.
- Diferenciación mínima de roles:

  - **Turista**: puede consultar aves, reservas y hacer una reserva.
  - **Guía**: aparece como opción para ser contratado.

- Perfil básico: nombre, email, rol, contraseña.

---

## 2. **Catálogo de Aves (Birds App)**

- Lista de aves con:

  - Nombre común.
  - Nombre científico.
  - Foto.
  - Descripción (markdown!?).

- Página de detalle con información básica.
- Relación con al menos una **reserva natural** (ej. “se observa en X reserva”).

---

## 3. **Reservas Naturales (Reserves App)**

- Lista de reservas con:

  - Nombre.
  - Ubicación.
  - Descripción.

- Relación con aves (qué especies se pueden ver allí).

---

## 4. **Sistema de Reservas (Bookings App)**

- Turista puede:

  - Seleccionar una reserva.
  - Elegir un guía disponible.
  - Escoger fecha y confirmar reserva.

- El sistema guarda la reserva en la BD con estado “pendiente”.
- Guía puede aceptar o rechazar la reserva (opcional pero ideal).

---

## 5. **Interfaz Básica**

- Página principal con navegación:

  - Aves | Reservas | Reservar | Ingresar/Registrarse.

- Estilo simple pero claro (HTML + CSS + un poco de Alpine.js).
- No tiene que ser el diseño final, solo que se vea organizado y usable.

---

# 🎯 Extras “si queda tiempo”

- Calendario de eventos.
- Perfiles detallados de guías.
- Artículos educativos (mínimo un ejemplo).

---

# 🚀 Justificación del MVP

1. Hay **usuarios y roles** (turista/guía).
2. Hay un **catálogo de aves**.
3. Hay **información de reservas naturales**.
4. Existe un **sistema básico de reservas**.
