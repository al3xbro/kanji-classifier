import Navbar from "./Components/Navbar.jsx";
import Canvas from "./Components/Canvas.jsx";
import Results from "./Components/Results.jsx";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
document.body.style = "background: black;";
const queryClient = new QueryClient();
export default function App() {
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
  );
}
