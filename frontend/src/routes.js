import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import Costs from "./components/Costs";
import Categories from "./components/Categories";
import Incomes from "./components/Incomes";
import CostInRange from "./components/CostInRange";
import { store } from "./store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: { name: "home" },
  },
  {
    name: "home",
    path: "/home",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
    beforeEnter(to, from, next) {
      if (store.getters["user/authenticated"]) {
        next(false);
      } else {
        next();
      }
    },
  },
  {
    path: "/register",
    component: Register,
    beforeEnter(to, from, next) {
      if (store.getters["user/authenticated"]) {
        next(false);
      } else {
        next();
      }
    },
  },
  {
    path: "/costs",
    component: Costs,
  },
  {
    path: "/categories",
    component: Categories,
  },
  {
    path: "/incomes",
    component: Incomes,
  },
  {
    path: "/costs_in_range",
    component: CostInRange,
  },
];

export const router = new VueRouter({
  routes,
  mode: "history",
});
