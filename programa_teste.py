from fastapi import FastAPI

# importa os recursos diretamente da LIB instalada pelo pip
from libgenerica.util.database import init_db, get_session
from libgenerica.controller.endereco import router as endereco_router
from libgenerica.controller.pessoa import router as pessoa_router

app = FastAPI(title="Teste da libgenerica")

# inicializa o banco da lib
init_db()

# inclui os routers fornecidos pela lib
app.include_router(endereco_router)
app.include_router(pessoa_router)

@app.get("/")
def health():
    return {"status": "ok", "lib": "libgenerica funcionando"}
