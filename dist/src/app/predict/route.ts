import axios from "axios"
import multiparty from "multiparty";
import multer from "multer"
export async function POST(request: Request) {
    // const data = await request.json()
    // console.log(request.body)

    const form = new multiparty.Form();
    const data = await new Promise((resolve, reject) => {
        form.parse(request, function (err, fields, files) {
            if (err) reject({ err });
            resolve({ fields, files });
        });
    });
    console.log(`data: `, JSON.stringify(data));

    // const formData = new FormData()
    // formData.append("file", request.files.file)
    // // console.log(formData)
    // const data = await axios.post("http://alexserver.sytes.net:8000/predict", formData)
    // console.log(data)
    return new Response("hi", { status: 200 })
}
export const config = {
    api: {
        bodyParser: false,
    },
};