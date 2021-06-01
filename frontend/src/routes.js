import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";

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
  },
  {
    path: "/register",
    component: Register,
  },
];

export const router = new VueRouter({
  routes,
  mode: "history",
});
