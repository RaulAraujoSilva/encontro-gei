// Serverless function — proxy para API Even3 com cache de 5 minutos
// GET /api/inscritos → { count, presencial, online, visita, visitas{j01..j04}, total, updatedAt }
// count/presencial/online/visita consideram apenas inscrições confirmadas (mesmo critério
// do limite de vagas da Even3); total inclui cadastros sem inscrição concluída.
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
    return res.status(200).json({ count: 0, presencial: 0, online: 0, visita: 0, updatedAt: new Date().toISOString(), note: 'token_not_configured' });
  }

  try {
    const r = await fetch('https://www.even3.com.br/api/v1/attendees', {
      headers: { 'Authorization-Token': token, 'Accept': 'application/json' }
    });
    if (!r.ok) throw new Error(`even3 ${r.status}`);
    const json = await r.json();
    const arr = Array.isArray(json?.data) ? json.data : (Array.isArray(json) ? json : []);
    // Apenas confirmados contam como inscritos (não confirmados têm categoria vazia)
    const confirmados = arr.filter(a => a?.confirmed === true);
    // Segmenta por registration_category: "online" → online; "visita" → visita técnica (Dia 2);
    // demais (Presencial Completo etc.) → presencial. A visita NÃO infla o presencial.
    const cat = (a) => String(a?.registration_category || '')
      .normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    const online = confirmados.filter(a => cat(a).includes('online')).length;
    const visita = confirmados.filter(a => cat(a).includes('visita')).length;
    const presencial = confirmados.length - online - visita;
    // Contagem por jornada (categorias "Visita Técnica — J01..J04")
    const visitas = ['j01', 'j02', 'j03', 'j04'].reduce((o, j) => {
      o[j] = confirmados.filter(a => cat(a).includes('visita') && cat(a).includes(j)).length;
      return o;
    }, {});
    const payload = { count: confirmados.length, presencial, online, visita, visitas, total: arr.length, eventId, updatedAt: new Date().toISOString() };
    cache = { value: payload, expires: now + 300_000 };
    return res.status(200).json(payload);
  } catch (e) {
    return res.status(200).json({ count: 0, presencial: 0, online: 0, visita: 0, updatedAt: new Date().toISOString(), error: String(e.message || e) });
  }
}
