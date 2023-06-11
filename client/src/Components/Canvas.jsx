import { useRef, useEffect, useState } from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";

const canvasStyle = {
    border: "0.0625rem solid #ffffff",
    borderRadius: "0.25rem",
    marginBottom: "20px",
    width: "100%",
    aspectRatio: "1 / 1"
}

export default function Canvas() {
    const [loaded, setLoaded] = useState(false)

    const canvas = useRef()
    useEffect(() => {
        setLoaded(true)
    }, [])
    const [canFire, setCanFire] = useState(true);

    const keydownHandler = (e) => {
        if (e.ctrlKey && e.key === 'z') {
            if (canFire) {
                setCanFire(false);
                canvas.current.undo()

                setTimeout(() => {
                    setCanFire(true);
                }, 1);
            }
        }
        if (e.ctrlKey && e.key === 'y') {
            if (canFire) {
                setCanFire(false);
                canvas.current.redo()

                setTimeout(() => {
                    setCanFire(true);
                }, 1);
            }
        }

    };

    useEffect(() => {
        window.addEventListener('keydown', keydownHandler);
        return () => {
            window.removeEventListener('keydown', keydownHandler);
        };
    }, [canFire]);

    return (
        <>
            <div className="row">
                <ReactSketchCanvas
                    ref={canvas}
                    canvasColor="#000000"
                    style={canvasStyle}
                    strokeWidth={10}
                    strokeColor="white"
                />
            </div>
            {
                loaded ? <div className="row">
                    <div className="col">
                        <button id="classify" onClick={async () => {
                            const image = await canvas.current.exportImage("png")
                            console.log(image)
                        }}>Classify!</button>
                    </div>
                    <div className="col">
                        <button id="undo" onClick={canvas.current.undo}>Undo</button>
                        <button id="clear" onClick={canvas.current.resetCanvas}> Clear</button>
                    </div >
                </div >
                    : null}
        </>
    )
}
