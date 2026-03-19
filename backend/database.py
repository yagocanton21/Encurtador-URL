import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

async def create_short_url(original_url: str, slug: str):
    url = f"{SUPABASE_URL}/rest/v1/urls"
    data = {
        "original_url": original_url,
        "slug": slug
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response

async def get_url_by_slug(slug: str):
    url = f"{SUPABASE_URL}/rest/v1/urls?slug=eq.{slug}&select=original_url,clicks"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data[0] if data else None

async def increment_clicks(slug: str, current_clicks: int):
    url = f"{SUPABASE_URL}/rest/v1/urls?slug=eq.{slug}"
    data = {"clicks": (current_clicks or 0) + 1}
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, json=data, headers=headers)
        response.raise_for_status()
        return response
