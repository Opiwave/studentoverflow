# Q&A Platform

Este es un programa básico de plataforma de preguntas y respuestas, donde los usuarios pueden registrarse, iniciar sesión, hacer preguntas y responderlas. Si no has iniciado sesión, no podrás ver las preguntas.

## Funcionalidades

- Registro de usuario con nombre de usuario y contraseña.
- Inicio de sesión.
- Creación de preguntas.
- Respuestas a las preguntas.
- Acceso restringido: Solo los usuarios autenticados pueden ver las preguntas.

## Instalación

1. Clona este repositorio:


   git clone https://github.com/Opiwave/studentoverflow.git
   cd tu_repositorio

2. Crea un entorno virtual y actívalo:

  python -m venv venv
  source venv/bin/activate  # Para Linux/Mac
  .\venv\Scripts\activate    # Para Windows

3. Instala las dependencias:

  pip install -r requirements.txt

4. Inicializa la base de datos:

  flask db init
  flask db migrate
  flask db upgrade

5.Ejecuta la aplicación:

  flask run

### USO

Abre tu navegador y ve a http://127.0.0.1:5000/.

Regístrate con un nuevo usuario.

Inicia sesión con tus credenciales.

Crea preguntas y responde a las preguntas de otros usuarios.

### TECNOLOGIAS UTILIZADAS
Python

Flask

HTML

SQLite

### CONTRIBUCIONES
Las contribuciones son bienvenidas. Por favor, envía un pull request con tus cambios y asegúrate de que las pruebas pasen correctamente.

### LICENCIA
Este proyecto no cuenta con una licencia. Sientete libre de usarlo.
