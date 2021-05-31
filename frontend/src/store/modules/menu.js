export default {
  namespaced: true,
  state: {
    items: [
      {
        url: "/home",
        text: "Home",
      },
      {
        url: "/categories",
        text: "Categories",
      },
      {
        url: "/costs",
        text: "Costs",
      },
      {
        url: "/incomes",
        text: "Incomes",
      },
      {
        url: "/costs_in_range",
        text: "Costs in range",
      },
    ],
  },
  getters: {
    items(state) {
      return state.items;
    },
  },
};
