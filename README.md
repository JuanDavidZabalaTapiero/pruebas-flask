# Proyecto Flask (prueba) 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-orange)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://www.docker.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Repositorio de ejemplo de un proyecto Flask que integra varias tecnologías:

- **Backend:** Flask, Flask-WTF, Flask-Babel, SQLAlchemy, Flask-Migrate  
- **Base de datos:** MySQL (Docker)  
- **Frontend:** Bootstrap 5, SCSS, Gulp  
- **Contenedores:** Docker y Docker Compose  
- **Tests:** Pytest y Pytest-Flask  
- **Internacionalización:** Español e Inglés

---

## 📦 Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/JuanDavidZabalaTapiero/pruebas-flask.git
cd pruebas-flask
```

2. Configurar variables de entorno en .env
```
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db
DB_PORT=3306
DB_NAME=db_name
SECRET_KEY=mi_llave_secreta
FLASK_ENV=development
DATABASE_URL=mysql://db_user:db_password@db:3306/db_name
```

3. Levantar los contenedores:
```bash
docker compose up --build
```

4. Migraciones de base de datos (primera vez):
```bash
docker compose exec web flask db init
docker compose exec web flask db migrate
docker compose exec web flask db upgrade
```

5. Acceder a la app: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Tests 🧪
```bash
pytest
```
