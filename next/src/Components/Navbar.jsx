"use client"
import { BsQuestionLg, BsGithub } from "react-icons/bs";
import Tutorial from "./Tutorial";
import { useState } from "react";
import Link from "next/link";

export default function Navbar() {

    const [showHelp, setShowHelp] = useState(false);

    return (
        <>
            {showHelp ? <Tutorial showVisible={setShowHelp} /> : null}
            <nav className="navbar navbar-expand" style={{ backgroundColor: "#ffffff", zIndex: 20 }}>
                < div className="container" >
                    <a href="#" className="navbar-brand" style={{ fontWeight: "bold" }}>Kanji Classifier</a>
                    <div style={{ display: "flex", gap: "10px" }}>
                        <BsQuestionLg style={{ width: "25px", height: "25px", color: "black" }} onClick={() => setShowHelp(!showHelp)} />
                        <Link style={{ width: "25px", height: "25px" }} href="https://github.com/al3xbro/kanji-classifier">
                            <BsGithub style={{ width: "24px", height: "24px", color: "black" }} />
                        </Link>
                    </div>
                </div >
            </nav >
        </>
    )
} 