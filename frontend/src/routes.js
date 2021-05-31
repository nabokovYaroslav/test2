import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./components/Home";
Vue.use(VueRouter);

/*const routes = [
	{
		path: '',
		redirect: {name: 'products'}
	},
	{
		name: 'products',
		path: '/products',
		component: ProductList,

	},
	{
		path: '/products/:id',
		component: Product
	},
	{
		path: '/cart',
		component: Cart
	},
	{
		path: '*',
		component: E404
	},
    {
        path: '/checkout',
        component: Checkout
    }
];*/
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
];

export const router = new VueRouter({
  routes,
  mode: "history",
});
