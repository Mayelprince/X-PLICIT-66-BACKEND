from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, deposits, admin

app = FastAPI(title="XPLICIT66 Savings API (backend scaffold)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "XPLICIT66 backend running. Add routes in app/routes."}

app.include_router(auth.router, prefix="/api/auth")
app.include_router(deposits.router, prefix="/api/deposits")
app.include_router(admin.router, prefix="/api/admin")
