// Serverless function — proxy para API Even3 com cache de 5 minutos
// GET /api/inscritos → { count, updatedAt }
// Vars de ambiente: EVEN3_API_TOKEN, EVEN3_EVENT_ID

let cache = { value: null, expires: 0 };

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'method_not_allowed' });
  }

  res.setHeader('Cache-Control', 'public, s-maxage=300, stale-while-revalidate=600');
  res.setHeader('Access-Control-Allow-Origin', '*');

  const now = Date.now();
  if (cache.value && cache.expires > now) {
    return res.status(200).json(cache.value);
  }

  const token = process.env.EVEN3_API_TOKEN;
  const eventId = process.env.EVEN3_EVENT_ID;

  if (!token || !eventId) {
    return res.status(200).json({ count: 0, updatedAt: new Date().toISOString(), note: 'token_not_configured' });
  }

  try {
    const r = await fetch(`https://api.even3.com.br/v1/attendees/${eventId}`, {
      headers: { 'Authorization-Token': token, 'Accept': 'application/json' }
    });
    if (!r.ok) throw new Error(`even3 ${r.status}`);
    const data = await r.json();
    const count = Array.isArray(data) ? data.length : (data.total ?? data.count ?? 0);
    const payload = { count, updatedAt: new Date().toISOString() };
    cache = { value: payload, expires: now + 300_000 };
    return res.status(200).json(payload);
  } catch (e) {
    return res.status(200).json({ count: 0, updatedAt: new Date().toISOString(), error: String(e.message || e) });
  }
}
