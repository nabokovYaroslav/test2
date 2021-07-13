import Vue from "vue";
import App from "./App.vue";
import { router } from "./routes.js";
import { store } from "./store/index";

Vue.config.productionTip = false;

import "@/assets/bootstrap-parody.css";
import "@/assets/loader.css";

new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>",
});
