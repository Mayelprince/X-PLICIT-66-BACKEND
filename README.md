```md
# X-PLICIT-66-BACKEND (FastAPI + MongoDB)

Quick start:

1. Create a Python virtualenv and install requirements:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Copy .env.example -> .env and fill values (MONGO_URI, SECRET_KEY, CLOUDINARY_*, etc).

3. Run locally:
   uvicorn app:app --reload --host 0.0.0.0 --port 8000

Useful endpoints (skeleton):
- GET  /           -> health
- POST /api/auth/register
- POST /api/auth/login
- POST /api/deposits/upload   -> upload screenshot
- POST /api/deposits          -> create deposit request
- GET  /api/admin/deposits    -> admin list pending
- PUT  /api/admin/deposits/{id}/approve
- PUT  /api/admin/deposits/{id}/reject
- GET  /api/transactions
```
