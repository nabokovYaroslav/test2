/* eslint no-useless-catch: 0 */

import { HTTP } from "./common";

const Request = async (request) => {
  try {
    const response = await request();
    return response;
  } catch (error) {
    if (error.response.status == 401) {
      try {
        let refresh_token = localStorage.getItem("refresh_token");
        if (refresh_token == null || refresh_token == "") {
          throw error;
        }
        const tokens = await HTTP.post("authentication/token/refresh/", {
          refresh: refresh_token,
        });
        localStorage.setItem("access_token", tokens.data.access);
        localStorage.setItem("refresh_token", tokens.data.refresh);
        const response = await request();
        return response;
      } catch (error) {
        throw error;
      }
    } else {
      throw error;
    }
  }
};

export default Request;
