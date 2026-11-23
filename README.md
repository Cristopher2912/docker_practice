# Docker Practice

Servicio web mínimo en Python que muestra un saludo y una lista, ejecutado en un contenedor Docker.

## Ejecutar localmente

```bash
docker build -t hola-docker .
docker run -p 10000:10000 hola-docker
```

Abrir http://localhost:10000

## Despliegue en Render

New → Web Service → conectar este repositorio → Runtime: Docker → plan Free.
