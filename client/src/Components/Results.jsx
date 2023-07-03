import { useStore } from "../useStore"
export default function Results() {
    const { cert, predict } = useStore()
    return (
        <div className="col-md-4" style={{ marginTop: 40 }}>
            {cert && predict && cert.map((item, index) => {
                return <>
                    <div id="best-guess">{predict[index]}</div>
                    <div id="best-certainty">{((Math.round(item * 100) / 100).toFixed(2)) * 100 + "%"}</div></>
            })}
        </div>
    )
}