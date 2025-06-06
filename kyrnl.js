api/public/kyrnl.js
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const response = await fetch("https://grfheayxwxyseqqbjdwt.supabase.co/storage/v1/object/public/kin-archive/Sim_Sage_KYRNL_06052025183840.json");

    if (!response.ok) {
      return res.status(500).json({ error: 'Failed to fetch KYRNL from Supabase' });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (err) {
    return res.status(500).json({ error: 'Unexpected server error', details: err.message });
  }
}
