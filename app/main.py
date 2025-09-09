from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Meu Lembrete (Starter)")

@app.get("/health")
def health():
    return {"ok": True, "service": "meu-lembrete", "version": "0.1.0"}

@app.get("/")
def root():
    return JSONResponse({"message": "Meu Lembrete API - Starter. Veja /docs para testar."})
