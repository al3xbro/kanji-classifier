import Navbar from "./Components/Navbar.jsx"
import Canvas from "./Components/Canvas.jsx"
import Results from "./Components/Results.jsx";
import "./App.css"
import 'bootstrap/dist/css/bootstrap.css';

document.body.style = 'background: black;';

export default function App() {
    return (
        <>
            <Navbar />
            <div className="container">
                <div className="row row-cols-md-2 row-cols-sm-1">
                    <div className="col-md-8" style={{ marginTop: "40px" }}>
                        <Canvas />
                    </div>
                    <Results />
                </div>
            </div >
        </>
    )
}

