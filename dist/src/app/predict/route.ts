import axios from "axios";

export async function POST(req: Request) {
  const data = await req.formData();
  console.log(data);
  const res = await axios.post(
    "http://alexserver.sytes.net:8000/predict",
    data,
    { headers: { "Content-Type": "multipart/form-data" } }
  );
  console.log(res.data);
  return new Response(JSON.stringify(res.data));
}
