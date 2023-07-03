"use client"
import Navbar from "../Components/Navbar.jsx";
import Canvas from "../Components/Canvas.jsx";
import Results from "../Components/Results.jsx";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();
export default function Home() {
    return (
        <QueryClientProvider client={queryClient}>
            <Navbar />
            <div className="container">
                <div className="row row-cols-md-2 row-cols-sm-1">
                    <div className="col-md-8" style={{ marginTop: "40px" }}>
                        <Canvas />
                    </div>
                    <Results />
                </div>
            </div>
        </QueryClientProvider>
    )
}
