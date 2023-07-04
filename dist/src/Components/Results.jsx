import { useStore } from "../app/useStore"
export default function Results() {
    const { cert, predict } = useStore()
    return (
        <div className="col-md-4" style={{ marginTop: 40 }}>
            {cert && predict && cert.map((item, index) => {
                return <>
                    <a id="best-guess" href={`https://jisho.org/search/%23kanji%20${predict[index]}`} target="_blank">{predict[index]}</a>
                    <div id="best-certainty">{Math.trunc(item * 100) + "%"}</div></>
            })}
        </div>
    )
}