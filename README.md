# Alke Wallet Final

Proyecto desarrollado con Django como parte del módulo 7, enfocado en la construcción de una aplicación web con operaciones CRUD, uso de modelos relacionales, autenticación, panel de administración, archivos estáticos y buenas prácticas básicas de desarrollo con Git y GitHub.

## Objetivo del proyecto

Desarrollar una aplicación web tipo billetera digital que permita gestionar clientes, cuentas y transacciones, utilizando Django como framework principal, SQLite en desarrollo y una estructura preparada para PostgreSQL en producción.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Git
- GitHub

## Estructura general del proyecto

```text
alke_wallet/
│── manage.py
│── requirements.txt
│── .gitignore
│
├── alke_wallet_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── gestion/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── gestion/
│   └── registration/
│
└── static/
    └── css/
        └── styles.css
```

## Funcionalidades implementadas

La aplicación incluye las siguientes funcionalidades:

- Creación de modelos relacionales con Django ORM
- Gestión de clientes
- Gestión de cuentas
- Gestión de transacciones
- Visualización de datos en listados web
- Formularios para crear registros
- Vista de detalle de cuenta
- Edición de cuentas
- Eliminación de cuentas
- Integración con panel de administración de Django
- Autenticación con login y logout
- Uso de archivos estáticos
- Navegación entre vistas
- Versionado con Git y trabajo en ramas

## Modelos del sistema

### Cliente

Representa a un cliente del sistema y está relacionado uno a uno con el modelo `User` de Django.

Campos principales:

- `user`
- `telefono`
- `direccion`
- `creado_en`

### Cuenta

Representa una cuenta asociada a un cliente.

Campos principales:

- `cliente`
- `numero_cuenta`
- `tipo_cuenta`
- `saldo`
- `activa`
- `creada_en`

### Transaccion

Representa una operación realizada sobre una cuenta.

Campos principales:

- `cuenta`
- `tipo`
- `monto`
- `descripcion`
- `fecha`

## Relaciones entre modelos

- Un `Cliente` tiene una relación `OneToOne` con `User`
- Un `Cliente` puede tener muchas `Cuenta`
- Una `Cuenta` puede tener muchas `Transaccion`

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3
- pip
- Git

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Octaviochamblas/Alke-wallet-final.git
cd Alke-wallet-final
```

### 2. Crear entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

En Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Migraciones

Para crear la base de datos y aplicar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear superusuario

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

## Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Rutas principales

### Aplicación

- `/`
- `/cuentas/`
- `/cuentas/nueva/`
- `/cuentas/<id>/`
- `/cuentas/<id>/editar/`
- `/cuentas/<id>/eliminar/`
- `/transacciones/`
- `/transacciones/nueva/`

### Autenticación

- `/accounts/login/`
- `/accounts/logout/`

### Administración

- `/admin/`

## Uso de autenticación

El proyecto incorpora autenticación utilizando el sistema nativo de Django:

- Login
- Logout
- Protección de vistas con autenticación
- Integración con el modelo `User`

## Uso del panel de administración

Se registraron los modelos en el panel admin de Django para facilitar la gestión de datos:

- `Cliente`
- `Cuenta`
- `Transaccion`

Esto permite:

- crear registros
- editarlos
- eliminarlos
- filtrarlos
- buscarlos desde el administrador

## Base de datos

Durante el desarrollo se utilizó SQLite por su simplicidad y rápida configuración.

Configuración actual de desarrollo:

- Motor: `sqlite3`

El proyecto además deja preparada una referencia para futura configuración con PostgreSQL en producción.

## PostgreSQL en producción

En `settings.py` se dejó documentada una estructura base para reemplazar SQLite por PostgreSQL en un entorno de producción.

Esto permite escalar el proyecto a un entorno más robusto si fuera necesario.

## Consultas realizadas

Durante el desarrollo se trabajó con:

- operaciones CRUD desde la shell
- filtros con ORM
- consultas relacionadas entre modelos
- consultas agregadas como `annotate()`
- ejemplo de consulta SQL personalizada con `raw()`

## Archivos estáticos

Se incorporó una hoja de estilos CSS para mejorar la presentación básica de la aplicación.

Ruta utilizada:

```text
static/css/styles.css
```

## Control de versiones

El proyecto fue desarrollado utilizando Git y GitHub, con commits progresivos y trabajo mediante ramas.

Ejemplo de flujo utilizado:

- inicialización del proyecto
- creación de app
- definición de modelos
- migraciones
- vistas y templates
- CRUD web
- autenticación
- mejoras visuales
- documentación final

## Posibles mejoras futuras

- Mejorar diseño visual con Bootstrap
- Asociar automáticamente cuentas al usuario autenticado
- Agregar validaciones más avanzadas en formularios
- Incorporar búsqueda y filtros en los listados
- Agregar paginación
- Mejorar permisos por tipo de usuario
- Implementar reportes de movimientos

## Autor

Proyecto desarrollado por Octavio Chamblas Navarrete.

## Estado del proyecto

Proyecto funcional en entorno de desarrollo, con CRUD web, autenticación, administración y estructura preparada para continuar escalando.