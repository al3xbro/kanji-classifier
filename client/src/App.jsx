import Navbar from "./Components/Navbar.jsx"
import Form from "./Components/Form.jsx";
import { ReactSketchCanvas } from 'react-sketch-canvas';
import Results from "./Components/Results.jsx";
import "./App.css"
import 'bootstrap/dist/css/bootstrap.css';

document.body.style = 'background: black;';

const canvasStyle = {
    border: "0.0625rem solid #ffffff",
    borderRadius: "0.25rem",
    marginBottom: "20px",
    width: "100%",
    aspectRatio: "1 / 1"
}

export default function App() {
    return (
        <>
            <Navbar />
            <div className="container">
                <div className="row row-cols-md-2 row-cols-sm-1">
                    <div className="col-md-8" style={{ marginTop: "40px" }}>
                        <div className="row">
                            <ReactSketchCanvas
                                canvasColor="#000000"
                                style={canvasStyle}
                                strokeWidth={10}
                                strokeColor="white"
                                marginBottom
                            />
                        </div>
                        <div className="row">
                            <Form />
                        </div>
                    </div>
                    <Results />
                </div>
            </div >
        </>
    )
}

