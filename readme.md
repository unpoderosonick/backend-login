Backend Login - Reutilizable para Proyectos con Firebase y Frontend

Este proyecto es un backend genérico diseñado para gestionar el login y la autenticación utilizando Django, Django REST Framework y Firebase. Está pensado para conectarse con cualquier frontend (React, Vue, Nuxt, etc.) y manejar la validación de usuarios a través de tokens de Firebase.

Características

Validación de tokens de Firebase.

Gestión segura de usuarios con integración a Firebase.

Totalmente compatible con cualquier frontend que utilice Firebase Authentication.

Configuración modular para entornos de desarrollo y producción.

Fácil despliegue y configuración.

Requisitos Previos

Python 3.8 o superior.

Firebase Admin SDK configurado.

Un frontend que se conecte a este backend utilizando llamadas API.

Configuración

1. Clonar el repositorio

git clone https://github.com/unpoderosonick/backend-login.git
cd backend-login

2. Crear un entorno virtual

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instalar las dependencias

pip install -r requirements.txt

4. Configurar variables de entorno

Crea un archivo .env en el directorio raíz y agrega lo siguiente:

SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
FIREBASE_CREDENTIALS=/ruta/a/tu/firebase-adminsdk.json

SECRET_KEY: Una clave secreta para tu proyecto Django.

FIREBASE_CREDENTIALS: La ruta al archivo de credenciales descargado desde Firebase.

5. Aplicar las migraciones

python manage.py migrate

6. Ejecutar el servidor

python manage.py runserver

Endpoints Disponibles

1. Validación de Token de Firebase

URL: /api/auth/validate-token/

Método: POST

Descripción: Valida un token de Firebase enviado por el frontend y devuelve información del usuario.

Ejemplo de Solicitud:

{
  "token": "tu_token_de_firebase"
}

Respuesta de Éxito:

{
  "message": "Token válido",
  "user_id": "12345",
  "email": "usuario@correo.com",
  "additional_info": "John Doe"
}

Cómo Conectar con el Frontend

Configura Firebase en tu frontend:

Asegúrate de que el frontend use Firebase Authentication para autenticar usuarios.

Obtén el token de Firebase en el frontend:
Usa el SDK de Firebase para autenticar al usuario y obtener el token:

const user = firebase.auth().currentUser;
const token = await user.getIdToken();

Envía el token al backend:
Usa una librería como Axios para enviar el token al backend:

import axios from 'axios';

const response = await axios.post('http://127.0.0.1:8000/api/auth/validate-token/', {
  token: userToken,
});

console.log(response.data);

Estructura del Proyecto

backend-login/
├── backend/                  # Configuración principal del proyecto
│   ├── settings/             # Configuración modular (base, dev, prod)
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuración WSGI
├── auth_app/                 # Aplicación para la autenticación
│   ├── views.py              # Lógica de validación de tokens
│   ├── urls.py               # Rutas de la app
│   ├── models.py             # Modelos (si se requieren)
├── manage.py                 # Script principal de Django
├── requirements.txt          # Dependencias del proyecto
├── .env                      # Variables de entorno (no incluido en el repositorio)
└── README.md                 # Documentación del proyecto

Contribuciones

Si deseas contribuir al proyecto:

Haz un fork del repositorio.

Crea una rama nueva (git checkout -b mi-nueva-rama).

Realiza los cambios y confirma los commits.

Envía un pull request.

Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
