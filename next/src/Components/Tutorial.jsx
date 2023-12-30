"use client"

export default function Tutorial({ showVisible }) {
    return (
        <>
            <div style={{ position: "fixed", width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>

                <div style={{ position: "absolute", width: "100%", height: "100%", backgroundColor: "white", opacity: "0.4" }} onClick={() => { showVisible(false) }} />
                <div>

                    <div style={{ position: "relative", borderRadius: "10px", padding: "20px", backgroundColor: "white", opacity: 1, fontSize: "30px", marginTop: "30px", marginRight: "30px", marginLeft: "30px", marginBottom: "5px", textAlign: "center" }}>Draw on the canvas, and click Classify!</div>
                    <div style={{ textAlign: "right", color: "lightgray", marginRight: "30px" }}>click anywhere to dismiss</div>
                </div>
            </div>
        </>
    );
}