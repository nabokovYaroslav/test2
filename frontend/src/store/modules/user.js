import Request from "../../api/request";
import { HTTP } from "../../api/common";

export default {
  namespaced: true,
  state: {
    user: null,
  },
  getters: {
    user(state) {
      return state.user;
    },
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    async getUser(store) {
      const request = async () => {
        HTTP.defaults.headers = {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        };
        const response = await HTTP.get("user/get_user");
        return response;
      };
      const user = await Request(request);
      store.commit("setUser", user.data);
    },
    logout(store) {
      store.commit("setUser", null);
    },
  },
};
