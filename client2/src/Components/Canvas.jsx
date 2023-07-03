import { useRef, useEffect, useState } from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";
const canvasStyle = {
  border: "0.0625rem solid #ffffff",
  borderRadius: "0.25rem",
  marginBottom: "20px",
  width: "100%",
  aspectRatio: "1 / 1",
};

export default function Canvas() {
  const [loaded, setLoaded] = useState(false);
  const mutation = useMutation({
    mutationFn: async (img) => {
      return await axios({
        url: `http://127.0.0.1:8000/upload/`,
        headers: {
          "Content-Type": "multipart/form-data",
        },
        method: `POST`,
        data: img,
      });
    },
    onSuccess: (e) => {
      console.log(e);
    },
    onError: (e) => {
      console.log(e);
    },
  });
  const canvas = useRef();
  useEffect(() => {
    setLoaded(true);
  }, []);
  const [canFire, setCanFire] = useState(true);

  const keydownHandler = (e) => {
    if (e.ctrlKey && e.key === "z") {
      if (canFire) {
        setCanFire(false);
        canvas.current.undo();

        setTimeout(() => {
          setCanFire(true);
        }, 1);
      }
    }
    if (e.ctrlKey && e.key === "y") {
      if (canFire) {
        setCanFire(false);
        canvas.current.redo();

        setTimeout(() => {
          setCanFire(true);
        }, 1);
      }
    }
  };

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
          strokeWidth={10}
          strokeColor="white"
        />
      </div>
      {loaded ? (
        <div className="row">
          <div className="col">
            <button
              id="classify"
              onClick={async () => {
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
              Classify!
            </button>
          </div>
          <div className="col">
            <button id="undo" onClick={canvas.current.undo}>
              Undo
            </button>
            <button id="clear" onClick={canvas.current.resetCanvas}>
              {" "}
              Clear
            </button>
          </div>
        </div>
      ) : null}
    </>
  );
}
