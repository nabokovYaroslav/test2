import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import menu from "./modules/menu";
import user from "./modules/user";
import costs from "./modules/costs";
import categories from "./modules/categories";
import incomes from "./modules/incomes";

export const store = new Vuex.Store({
  modules: {
    menu,
    user,
    costs,
    categories,
    incomes,
  },
  strict: process.env.NODE_ENV !== "production",
});
