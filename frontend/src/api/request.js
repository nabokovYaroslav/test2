import { HTTP } from "./common";

const Request = async (request) => {
  try {
    const response = await request();
    return response;
  } catch (error) {
    try {
      const tokens = await HTTP.post("authentication/token/refresh/", {
        refresh: localStorage.getItem("refresh_token"),
      });
      localStorage.setItem("access_token", tokens.data.access);
      localStorage.setItem("refresh_token", tokens.data.refresh);
      const response = await request();
      return response;
    } catch (error) {
      return error;
    }
  }
};

export default Request;
