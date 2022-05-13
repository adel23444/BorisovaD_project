import Axios from "axios";
import { baseUrl } from "../../config";

const api = Axios.create(
    {
        headers: {
            "Content-Type": "application/json"
        },
        baseURL: baseUrl,
    }
)

api.interceptors.request.use(
    function (config) {
        const token = localStorage.getItem("token");
        config.headers.Authorization = token ? `Bearer ${token}` : '';
        return config
    }
)

export default { api }