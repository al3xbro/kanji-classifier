import { NextApiRequest, NextApiResponse } from "next";
import multiparty from "multiparty";
import axios from "axios";
import fs from "fs"

const uploadImage = async (req: NextApiRequest, res: NextApiResponse) => {
    const form = new multiparty.Form();
    const data = await new Promise((resolve, reject) => {
        form.parse(req, function (err, fields, files) {
            if (err) reject({ err });
            resolve({ fields, files });
        });
    });
    const formData = new FormData();
    // @ts-ignore
    console.log(data.files.file)
    // formData.append("file", data.fields[0]);
    // @ts-ignore
    formData.append("file", fs.createReadStream(data.files.file[0].path));

    // console.log(formData)
    const reponse = await axios.post("http://alexserver.sytes.net:8000/predict", formData, { headers: { 'Content-Type': 'multipart/form-data' } })
    console.log(reponse.data)

    res.status(200).json({ success: true });
};

export default uploadImage;
export const config = {
    api: {
        bodyParser: false,
    },
};