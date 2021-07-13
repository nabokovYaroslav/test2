import Request from "./request";
import HTTP_AUTH from "./common";

export const Income = {
  async list(limit, offset) {
    const request = async () => {
      const response = await HTTP_AUTH().get(
        `costs/incomes/?limit=${limit}&offset=${offset}`
      );
      return response;
    };
    const incomes = await Request(request);
    return incomes;
  },
  async create(name, money, user) {
    const request = async () => {
      const response = await HTTP_AUTH().post("costs/incomes/", {
        name: name,
        money: money,
        user: user,
      });
      return response;
    };
    const income = await Request(request);
    return income;
  },
  async delete(id) {
    const request = async () => {
      const response = await HTTP_AUTH().delete(`costs/incomes/${id}/`);
      return response;
    };
    await Request(request);
  },
};
