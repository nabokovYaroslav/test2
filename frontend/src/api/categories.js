import Request from "./request";
import HTTP_AUTH from "./common";

export const Category = {
  async list(limit, offset) {
    const request = async () => {
      let url = "costs/categories/";
      if (limit != null && offset != null) {
        url += `?limit=${limit}&offset=${offset}`;
      }
      const response = await HTTP_AUTH().get(url);
      return response;
    };
    const categories = await Request(request);
    return categories;
  },
  async delete(id) {
    const request = async () => {
      const response = await HTTP_AUTH().delete(`costs/categories/${id}/`);
      return response;
    };
    await Request(request);
  },
  async create(name, user) {
    const request = async () => {
      const response = await HTTP_AUTH().post(`costs/categories/`, {
        name: name,
        user: user,
      });
      return response;
    };
    const category = await Request(request);
    return category;
  },
  async costInRange(startDate, endDate, categories) {
    const request = async () => {
      const response = await HTTP_AUTH().post(
        `costs/categories/get_cost_in_range/`,
        {
          start_date: startDate,
          end_date: endDate,
          categories: categories,
        }
      );
      return response;
    };
    const cost = await Request(request);
    return cost;
  },
};
