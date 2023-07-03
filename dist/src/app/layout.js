import './globals.css'
import "bootstrap/dist/css/bootstrap.css";
import { Montserrat } from 'next/font/google'

const montserrat = Montserrat({ subsets: ['latin'] })

export const metadata = {
    title: 'Kanji Classifier',
    description: 'OCR webapp that classifies 3000+ Japanese kanji.',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body className={montserrat.className} style={{ backgroundColor: "black" }}>{children}</body>
        </html>
    )
}
