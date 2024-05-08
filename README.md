# coral-talk
Proyecto de intercambio de idioma con la finalidad de mejorar la confianza del usuario con el idioma que está aprendiendo.

# Indicaciones
Deben instalar sus entorno virtual y instalar los paquetes del requirements.txt

my_project/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── home.py  # Rutas para la página de inicio
│   │   ├── auth.py  # Rutas para la autenticación (login, registro, etc.)
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── base.html  # Plantilla base para todas las páginas
│   │   ├── index.html  # Página de inicio
│   │   ├── login.html  # Página de inicio de sesión
│   │   ├── register.html  # Página de registro de usuario
│   │   └── error.html  # Página de error
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css  # Archivos CSS personalizados
│   │   │   └── ...
│   │   ├── js/
│   │   │   ├── script.js  # Archivos JavaScript personalizados
│   │   │   └── ...
│   │   └── img/  # Imágenes y otros archivos estáticos
│   │
│   └── models/  # Definición de modelos de datos (si es necesario)
│       ├── __init__.py
│       ├── user.py  # Modelo de usuario
│       └── ...
│
├── env/  # Entorno virtual para las dependencias del proyecto
│   └── ...
│
├── requirements.txt  # Lista de dependencias del proyecto (generada con pip freeze)
├── config.py  # Archivo de configuración del proyecto
└── run.py  # Archivo principal para ejecutar la aplicación Flask
