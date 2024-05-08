# restapi-fastapi

En local...
    
    uvicorn main:app --reload

Luego...
    
    http://127.0.0.1:8000


Para ingresar a la documentación
    
    http://127.0.0.1:8000/docs


## Access postgres database
To access the database run this command:
```bash
docker exec -it postgres-db psql -U rest-api -W store-db
```

### Create a new table revision by running
```bash
alembic revision --autogenerate -m'revision name'
```

### Manually upgrade db with
```bash
alembic upgrade head
```