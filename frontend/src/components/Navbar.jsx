import { NavLink } from "react-router-dom";

function Navbar() {
    return (
        <nav
            style={{
                display: "flex",
                gap: "20px",
                padding: "20px",
                background: "#282c34"
            }}
        >
            <NavLink
                to="/"
                style={{ color: "white", textDecoration: "none" }}
            >
                Home
            </NavLink>

            <NavLink
                to="/users"
                style={{ color: "white", textDecoration: "none" }}
            >
                Users
            </NavLink>

            <NavLink
                to="/folders"
                style={{ color: "white", textDecoration: "none" }}
            >
                Folders
            </NavLink>

            <NavLink
                to="/documents"
                style={{ color: "white", textDecoration: "none" }}
            >
                Documents
            </NavLink>
        </nav>
    );
}

export default Navbar;