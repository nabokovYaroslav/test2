import Request from "./request";
import HTTP_AUTH from "./common";
import { HTTP } from "./common";

export const User = {
  async getUser(user_id) {
    const request = async () => {
      const response = await HTTP_AUTH().get(`users/${user_id}/`);
      return response;
    };
    const user = await Request(request);
    return user;
  },

  async token(email, password) {
    const response = await HTTP.post(`authentication/token/`, {
      email: email,
      password: password,
    });
    return response;
  },

  async create(user_name, email, password) {
    await HTTP.post(`users/`, {
      user_name: user_name,
      email: email,
      password: password,
    });
  },

  async getBalance(id) {
    const request = async () => {
      const response = await HTTP_AUTH().get(`users/${id}/get_balance/`);
      return response;
    };
    const balance = await Request(request);
    return balance;
  },
};
