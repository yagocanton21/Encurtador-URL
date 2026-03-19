# Como subir para o Render 🚀

Para hospedar seu encurtador de URL no Render, usei uma configuração chamada **Render Blueprint** (arquivo `render.yaml`), que facilita tudo.

### 1. Preparar o Código
1. Suba a pasta raiz `Encurtador url` para um repositório no seu GitHub.

### 2. Configurar no Render
1. Vá em [dashboard.render.com](https://dashboard.render.com).
2. Clique em **"New +"** e escolha **"Blueprint"**.
3. Conecte seu repositório do GitHub.
4. O Render lerá o arquivo `render.yaml` que eu criei e sugerirá a criação de dois serviços:
    *   `encurtador-backend` (Web Service)
    *   `encurtador-frontend` (Static Site)

### 3. Variáveis de Ambiente
Durante a criação (ou depois nas configurações de "Environment" de cada serviço), você precisará preencher:

**No Backend:**
- `SUPABASE_URL`: Sua URL do Supabase.
- `SUPABASE_KEY`: Sua Key do Supabase.

**No Frontend:**
- `VITE_API_URL`: A URL que o Render gerou para o seu backend (algo como `https://encurtador-backend.onrender.com`).

### 4. Último Ajuste
No arquivo `frontend/src/components/ShortenerForm.jsx`, não esqueça de garantir que a URL do `fetch` use a variável de ambiente ou a URL real do Render em vez de `localhost`.
