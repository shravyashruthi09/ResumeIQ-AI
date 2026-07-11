import axios from "axios";

const API = axios.create({
    baseURL: "https://resumeiq-ai-7wvx.onrender.com",
});

export default API;