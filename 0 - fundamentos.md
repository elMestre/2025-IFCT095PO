# Fundamentos

## 1) Fundamentos Web y de Sistemas

- **Estructura de directorios**
  - Rutas relativas vs absolutas; rutas de proyecto vs del sistema.
- **Arquitectura cliente‑servidor**
  - Request/response, **HTTP/1.1 vs HTTP/2**, stateless.
  - **IP, dominio, DNS**, y **URL** (esquema, host, puerto, ruta, query, fragmento).
- **HTTP esencial**
  - Métodos: **GET vs POST** (+ PUT, PATCH, DELETE opc.).
  - **Parámetros**: query string vs body (form‑urlencoded, JSON).
  - **Códigos de estado** (200, 201, 204, 301/302, 400, 401, 403, 404, 500…).
  - **Headers** y **MIME types**.
  - **Cookies, sesiones, CSRF, CORS** (visión general).
- **Estáticos vs dinámicos**
  - Archivos estáticos (CSS/JS/imagenes) vs respuesta generada en servidor.
- **Herramientas de inspección**
  - **Chrome DevTools**: pestañas Elements, Network, Sources, Application.

---

## 2) Terminal & Entorno de trabajo

- **Uso de Terminal** (Windows PowerShell/Bash): navegación, alias, redirecciones, permisos, variables de entorno.
- **VS Code**
  - Extensiones sugeridas: Python, Pylance, Black, isort, Prettier, Django, GitLens.
  - Debugger integrado y launch.json básico para Django.
- **Git** (imprescindible)
  - Flujo básico: `init/clone`, `status`, `add`, `commit`, `log`, `diff`, `restore`, `rm`, `.gitignore`.
  - **Branching** y **PRs** (GitHub): `branch`, `switch`, `merge`, `rebase` (opcional), **conventional commits**.
  - **Remotos**: GitHub; *opcional*: GitKraken como cliente visual.

---

## 3) Programación con Python (fundamentos)

- **Sintaxis y tipos**: números, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `None`.
- **Operadores y expresiones**; *truthiness*.
- **Control de flujo**: `if/elif/else`, `for`, `while`, comprensiones.
- **Funciones**: parámetros, valores por defecto, `*args/**kwargs`, **scope**.
- **Módulos y paquetes**: `import`, estructura de proyecto.
- **POO** (imprescindible para Django)
  - **Clases y objetos**, métodos, atributos.
  - **Herencia**, composición; `@property`.
  - **Dataclasses** (opcional para ejercicios).
- **Patrones básicos** (ligero): MVC/MVT (para encaje con Django), repositorio opcional.

---

## 4) Gestión de entornos y dependencias

- **`python -m venv`**: crear/activar entornos virtuales.
- **`pip`**: instalar, actualizar, desinstalar.
- **`requirements.txt`** y **bloqueo de versiones**; *opcional*: `pip-tools`/`poetry`.
- **Variables de entorno** y configuración con **`.env`** (python‑dotenv). Buenas prácticas (no secretos en Git).
- **Decoradores** (nivel medio): `@staticmethod`, `@classmethod`, funciones que retornan funciones; ejemplos breves.

---

## 5) Bases de datos

- **SQL** (mínimo viable): `CREATE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`.
- **Motores**: **SQLite** (desarrollo) → **PostgreSQL** (producción recomendado).
- **Modelado**
  - **Cardinalidades**: 1‑1, 1‑N, N‑N.
  - **Normalización** básica, claves primarias/foráneas, **constraints**.
  - **Índices**, **transacciones**, **migraciones** (visión general antes de Django ORM).

---

## 6) Frontend web básico

- **HTML5**: semántica, formularios, inputs.
- **CSS**: selectores, caja, layout moderno (Flexbox/Grid). *Opcional*: framework ligero (Tailwind/Bootstrap) para prototipos.
- **JavaScript esencial**: DOM, eventos; fetch API (para ver Network en DevTools). **Sólo lo necesario** para entender la parte cliente.

---
