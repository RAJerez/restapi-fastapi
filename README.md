# RestAPI CRUD with FastAPI

## Project Description

This project is a REST API built with ***FastAPI***, designed to perform CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database. It uses SQLAlchemy as the ORM (Object-Relational Mapping) for database interaction and Alembic for database migrations and versioning. The application is prepared for deployment using Docker, which facilitates its distribution and scalability.


## Project Setup

1. ### Clone the repository:
```bash
git clone git@github.com:RAJerez/restapi-fastapi.git
cd repository-name
```

2. ### Create and configure the .env file:
```bash
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=store-db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

CONNSTR=postgresql://rest-api:postgres_password@localhost:5432/store-db
```

2. ### Build and start the Docker containers:
```bash
docker-compose up --build
```

3. ### Apply database migrations with Alembic:
```bash
docker-compose exec app alembic upgrade head
```


## Usage

Once the containers are up and running, the API will be available at http://localhost:8000. You can access the automatically generated interactive documentation by FastAPI at http://localhost:8000/docs.