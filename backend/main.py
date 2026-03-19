from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
import database

app = FastAPI(title="Encurtador de URL")

# Habilitar CORS para permitir que o React se comunique com a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: HttpUrl
    slug: str = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/shorten")
async def shorten_url(request: Request, url_req: URLRequest):
    import random
    import string
    
    slug = url_req.slug
    if not slug:
        slug = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    try:
        await database.create_short_url(str(url_req.url), slug)
        base_url = str(request.base_url)
        return {"slug": slug, "short_url": f"{base_url}{slug}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Slug já está em uso ou erro no banco de dados.")

from fastapi.responses import RedirectResponse

@app.get("/{slug}")
async def redirect_url(slug: str):
    url_data = await database.get_url_by_slug(slug)
    if not url_data:
        raise HTTPException(status_code=404, detail="URL não encontrada.")
    
    # Incrementar cliques em segundo plano
    await database.increment_clicks(slug, url_data.get("clicks", 0))
    
    # Redirecionamento 307 (Temporary Redirect)
    return RedirectResponse(url=url_data["original_url"])
