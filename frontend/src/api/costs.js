import Request from "./request";
import HTTP_AUTH from "./common";

export const Cost = {
  async list(limit, offset) {
    const request = async () => {
      const response = await HTTP_AUTH().get(
        `costs/?limit=${limit}&offset=${offset}`
      );
      return response;
    };
    const costs = await Request(request);
    return costs;
  },
  async create(name, category, money) {
    const request = async () => {
      const response = await HTTP_AUTH().post("costs/", {
        name: name,
        category: category,
        money: money,
      });
      return response;
    };
    const cost = await Request(request);
    return cost;
  },
  async delete(id) {
    const request = async () => {
      const response = await HTTP_AUTH().delete(`costs/${id}/`);
      return response;
    };
    await Request(request);
  },
};
