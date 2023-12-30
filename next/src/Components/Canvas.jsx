"use client"
import { useRef, useEffect, useState } from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";
import { useStore } from "../app/useStore";

const canvasStyle = {
    border: "0.0625rem solid #ffffff",
    borderRadius: "0.25rem",
    margin: "auto",
    marginBottom: "20px",
    width: "95%",
    aspectRatio: "1 / 1",
};

export default function Canvas() {
    const [loaded, setLoaded] = useState(false);

    // calls an API and sets global store to response
    const mutation = useMutation({
        mutationFn: async (img) => {
            return await axios({
                url: `/predict`,
                timeout: 300000,
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                method: `POST`,
                data: img,
            });
        },
        onSuccess: (e) => {
            useStore.setState({
                predict: e.data.predictions,
                cert: e.data.certainty,
            });
        },
        onError: (e) => {
            alert(e);
        },
    });

    const canvas = useRef();

    // making sure Canvas is loaded
    useEffect(() => {
        setLoaded(true);
    }, []);
    const [canFire, setCanFire] = useState(true);

    // ctrl + z and ctrl + y handler 
    const keydownHandler = (e) => {
        if (e.ctrlKey && e.key === "z") {
            if (canFire) {
                setCanFire(false);
                canvas.current.undo();

                // disables ctrl + z to prevent multiple calls
                setTimeout(() => {
                    setCanFire(true);
                }, 1);
            }
        }
        if (e.ctrlKey && e.key === "y") {
            if (canFire) {
                setCanFire(false);
                canvas.current.redo();

                // disables ctrl + y to prevent multiple calls
                setTimeout(() => {
                    setCanFire(true);
                }, 1);
            }
        }
    };

    // adds and removes event listener on canFire change
    useEffect(() => {
        window.addEventListener("keydown", keydownHandler);
        return () => {
            window.removeEventListener("keydown", keydownHandler);
        };
    }, [canFire]);

    return (
        <>
            <div className="row">
                <ReactSketchCanvas
                    ref={canvas}
                    canvasColor="#000000"
                    style={canvasStyle}
                    strokeWidth={20}
                    strokeColor="white"
                />
            </div>

            {/* only loads buttons after Canvas */}
            {loaded ? (
                <div className="row">
                    <div className="col">
                        <button
                            id={mutation.isLoading ? "classify-active" : "classify"}
                            disabled={mutation.isLoading}
                            onClick={async () => {
                                // processes input and calls mutate
                                const image = await canvas.current.exportImage("png");
                                const imageBase64 = image.split(",")[1];
                                const blobData = atob(imageBase64);
                                let arrayData = new Uint8Array(blobData.length);
                                for (let i = 0; i < blobData.length; i++) {
                                    arrayData[i] = blobData.charCodeAt(i);
                                }
                                let blob = new Blob([arrayData.buffer], { type: "image/png" });
                                let file = new File([blob], "image.png", { type: "image/png" });

                                let formData = new FormData();
                                formData.append("file", file);
                                mutation.mutate(formData);
                            }}
                        >
                            {mutation.isLoading ? "Loading..." : "Classify!"}
                        </button>
                        <button id="undo" onClick={canvas.current.undo}>
                            Undo
                        </button>
                        <button
                            id="clear"
                            onClick={() => {
                                canvas.current.resetCanvas();
                                useStore.setState({ predict: null, cert: null });
                            }}
                        >
                            Clear
                        </button>
                    </div>
                </div>
            ) : null}
        </>
    );
}
