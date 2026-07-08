import axios from "axios";

const api = axios.create({
    baseURL: "https://python-fastapi-application.onrender.com",
    headers: {
        "Content-Type": "application/json"
    }
});

export default api;
