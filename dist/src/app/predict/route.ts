import axios from "axios";

// makes a request to private server and returns data
export async function POST(req: Request) {
    const data = await req.formData();
    const res = await axios.post(
        "http://alexserver.sytes.net:8000/predict",
        data,
        { headers: { "Content-Type": "multipart/form-data" } }
    );
    return new Response(JSON.stringify(res.data));
}
