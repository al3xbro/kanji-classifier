export default function Navbar() {
    return (
        <nav className="navbar navbar-expand" style={{ backgroundColor: "#ffffff" }}>
            < div className="container" >
                <a href="#" className="navbar-brand montserrat" style={{ fontWeight: "bold" }}>Kanji Classifier</a>
                <a href="https://github.com/al3xbro/cnn-ocr-kanji"> <img src={"/github-mark.png"} width="30" /> </a>
            </div >
        </nav >
    )
} 