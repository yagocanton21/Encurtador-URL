import { useState } from 'react'

export default function ShortenerForm() {
  const [url, setUrl] = useState('')
  const [slug, setSlug] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!url) return

    setLoading(true)
    setError('')
    setResult('')

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'
      const response = await fetch(`${apiUrl}/shorten`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, slug })
      })

      if (!response.ok) throw new Error('Erro ao encurtar URL')

      const data = await response.json()
      setResult(data.short_url)
      setUrl('')
      setSlug('')
    } catch (err) {
      console.error(err)
      setError('Erro ao encurtar URL. Verifique se o backend está rodando.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="glass-card">
      <h1>Short.ly</h1>
      <p className="description">
        Transforme seus links longos em algo curto e elegante via FastAPI.
      </p>

      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="url"
            placeholder="Cole sua URL longa aqui..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
        </div>
        
        <div style={{ marginTop: '1rem' }} className="input-group">
          <input
            type="text"
            placeholder="Slug personalizado (opcional)"
            value={slug}
            onChange={(e) => setSlug(e.target.value)}
          />
        </div>

        <button type="submit" disabled={loading} style={{ marginTop: '1.5rem', width: '100%' }}>
          {loading ? <div className="loader" style={{ margin: '0 auto' }}></div> : 'Encurtar URL'}
        </button>
      </form>

      {error && <p style={{ color: '#ef4444', marginTop: '1rem' }}>{error}</p>}

      {result && (
        <div className="result-card">
          <p>Seu link está pronto!</p>
          <div className="short-url">{result}</div>
          <button onClick={() => navigator.clipboard.writeText(result)}>
            Copiar Link
          </button>
        </div>
      )}
    </div>
  )
}
