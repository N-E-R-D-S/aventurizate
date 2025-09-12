# Contribuyendo a Aventurízate

¡Gracias por tu interés en contribuir a **Aventurízate**! 🎉  
Este proyecto promueve el turismo sostenible y el aviturismo en Nicaragua a través de la tecnología. Todas las contribuciones, grandes o pequeñas, son bienvenidas.

## 📌 Requisitos Previos

Antes de contribuir, asegúrate de tener:

- **Git** instalado.
- **Extensión de Git Flow** instalada:
  ```bash
  sudo apt install git-flow        # Linux (Debian/Ubuntu)
  brew install git-flow-avh        # macOS
  choco install git-flow-avh       # Windows (Chocolatey)
  ```

## 🌿 Estrategia de Ramas con Git Flow

Seguimos el modelo de **Git Flow**:

- `main` → Siempre lista para producción.
- `develop` → Rama de integración donde se fusionan las funcionalidades.
- `feature/*` → Nuevas funcionalidades o mejoras.
- `release/*` → Versiones preliminares para pruebas.
- `hotfix/*` → Correcciones rápidas en producción.

## 🚀 Cómo Contribuir

### 1. Clonar el Repositorio

```bash
git clone <url_del_repositorio>
cd aventurizate
```

### 2. Inicializar Git Flow

```bash
git flow init
```

- Usa los valores predeterminados (`main` como rama de producción, `develop` como rama de integración).

### 3. Crear una Nueva Funcionalidad

```bash
git flow feature start <nombre-funcionalidad>
```

- Trabaja en tu funcionalidad dentro de esta rama.

### 4. Finalizar una Funcionalidad

```bash
git flow feature finish <nombre-funcionalidad>
```

- Fusiona tu funcionalidad en `develop`.

### 5. Crear una Versión de Prueba (Release)

```bash
git flow release start <version>
git flow release finish <version>
```

### 6. Hotfix (Corrección Rápida)

```bash
git flow hotfix start <nombre-correcion>
git flow hotfix finish <nombre-correcion>
```

## ✅ Pull Requests

- Crea **pull requests hacia la rama `develop` solamente**.
- Asegúrate de que tu rama esté **actualizada con `develop`** antes de abrir un PR.
- Incluye una **descripción de los cambios** y referencia cualquier issue relacionado.
- Solicita revisión de al menos **un miembro del equipo**.

## 💡 Directrices Adicionales

- Mantén las funcionalidades **pequeñas y enfocadas**.
- Escribe **documentación clara** para nuevas funcionalidades.
- Agrega o actualiza **pruebas** si es necesario.
- Sigue **PEP 8** para el código Python.
- Sé **respetuoso y constructivo** en las discusiones (ver [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)).
