import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Users from "./pages/Users";
import Folders from "./pages/Folders";
import Documents from "./pages/Documents";

function App() {
    return (
        <>
            <Navbar />

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/users" element={<Users />} />
                <Route path="/folders" element={<Folders />} />
                <Route path="/documents" element={<Documents />} />
            </Routes>
        </>
    );
}

export default App;