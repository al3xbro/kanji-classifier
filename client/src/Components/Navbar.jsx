import gitlogo from "../assets/github-mark.png"

export default function Navbar() {
    return (
        <nav className="navbar navbar-expand">
            < div className="container" >
                <a href="#" class="navbar-brand">Kanji Classifier</a>
                <a href="https://github.com/al3xbro/cnn-ocr-kanji"> <img src={gitlogo} width="30" /> </a>
            </div >
        </nav >
    )
} 