/* eslint no-useless-catch: 0 */
import { User } from "../../api/users";
import { router } from "../../routes";

export default {
  namespaced: true,
  state: {
    user: null,
    authenticated: false,
    userIsLoading: false,

    balance: null,
    balanceIsLoading: false,
  },
  getters: {
    user(state) {
      return state.user;
    },
    userIsLoading(state) {
      return state.userIsLoading;
    },
    balance(state) {
      return state.balance;
    },
    balanceIsLoading(state) {
      return state.balanceIsLoading;
    },
    authenticated(state) {
      return state.authenticated;
    },
  },
  mutations: {
    setUser(state, data) {
      state.user = data.user;
      state.authenticated = data.authenticated;
    },
    setUserLoad(state, isLoading) {
      state.userIsLoading = isLoading;
    },
    setBalance(state, balance) {
      state.balance = balance;
    },
    setBalanceLoad(state, isLoading) {
      state.balanceIsLoading = isLoading;
    },
  },
  actions: {
    async getUser(store) {
      try {
        store.commit("setUserLoad", true);
        const access_token = localStorage.getItem("access_token");
        const refresh_token = localStorage.getItem("refresh_token");
        let user_id = null;
        if (access_token != null && access_token.split(".").length == 3) {
          user_id = JSON.parse(atob(access_token.split(".")[1]))["user_id"];
        } else if (
          refresh_token != null &&
          refresh_token.split(".").length == 3
        ) {
          user_id = JSON.parse(atob(refresh_token.split(".")[1]))["user_id"];
        }
        if (user_id == null) {
          throw new Error();
        }
        const user = await User.getUser(user_id);
        store.commit("setUser", { user: user.data, authenticated: true });
      } catch (error) {
        store.commit("setUser", { user: null, authenticated: false });
        throw error;
      } finally {
        store.commit("setUserLoad", false);
      }
    },

    async login(store, { email, password }) {
      try {
        const tokens = await User.token(email, password);
        localStorage.setItem("access_token", tokens.data.access);
        localStorage.setItem("refresh_token", tokens.data.refresh);
        await store.dispatch("getUser");
      } catch (error) {
        throw error;
      }
    },

    async register(store, { user_name, email, password }) {
      try {
        await User.create(user_name, email, password);
        router.push("/login");
      } catch (error) {
        throw error;
      }
    },

    async getBalance(store) {
      try {
        store.commit("setBalanceLoad", true);
        const balance = await User.getBalance(store.state.user.id);
        store.commit("setBalance", balance.data.balance);
      } catch (error) {
        throw error;
      } finally {
        store.commit("setBalanceLoad", false);
      }
    },

    logout(store) {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      store.commit("setUser", { user: null, authenticated: false });
    },

    redirect() {
      router.push("/home");
    },
  },
};
