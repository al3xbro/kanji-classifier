import './globals.css'
import "bootstrap/dist/css/bootstrap.css";
import { Analytics } from '@vercel/analytics/react';

export const metadata = {
    title: 'Kanji Classifier',
    description: 'OCR webapp that classifies 3000+ Japanese kanji.',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body style={{ backgroundColor: "black" }}>
                {children}
                <Analytics />
            </body>
        </html>
    )
}
