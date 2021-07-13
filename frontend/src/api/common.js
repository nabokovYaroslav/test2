import axios from "axios";

export const HTTP = axios.create({
  baseURL: "http://localhost:8000/api/",
});

const HTTP_AUTH = () => {
  const http_auth = axios.create({
    baseURL: "http://localhost:8000/api/",
  });
  http_auth.defaults.headers = {
    Authorization: `Bearer ${localStorage.getItem("access_token")}`,
  };
  return http_auth;
};

export default HTTP_AUTH;
