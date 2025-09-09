# Dockerfile mínimo para FastAPI (uvicorn)
FROM python:3.11-slim
WORKDIR /app
COPY ./app /app/app
RUN pip install --no-cache-dir fastapi uvicorn[standard]
ENV PORT=8080
CMD ["uvicorn", "app.main:app", "--host","0.0.0.0","--port","8080"]
