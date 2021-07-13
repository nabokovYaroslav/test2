/* eslint no-useless-catch: 0 */
import { Cost } from "../../api/costs";

export default {
  namespaced: true,
  state: {
    costs: [],
    costsIsLoading: false,
    hasNext: false,
  },
  getters: {
    costs(state) {
      return state.costs;
    },
    costsIsLoading(state) {
      return state.costsIsLoading;
    },
    hasNext(state) {
      return state.hasNext;
    },
  },
  mutations: {
    setCosts(state, costs) {
      state.costs.push(...costs);
    },
    addCost(state, cost) {
      state.costs.unshift(cost);
    },
    clearCosts(state) {
      state.costs = [];
    },
    removeCost(state, id) {
      state.costs = state.costs.filter((cost) => {
        return cost.id != id;
      });
    },
    setLoad(state, isLoading) {
      state.costsIsLoading = isLoading;
    },
    setHasNext(state, hasNext) {
      state.hasNext = hasNext;
    },
  },
  actions: {
    async getCosts(store, { limit, offset }) {
      try {
        store.commit("setLoad", true);
        const costs = await Cost.list(limit, offset);
        if (costs.data.length < limit - offset) {
          store.commit("setHasNext", false);
        } else {
          store.commit("setHasNext", true);
        }
        store.commit("setCosts", costs.data);
      } catch (error) {
        throw error;
      } finally {
        store.commit("setLoad", false);
      }
    },
    async createCost(store, { name, category, money }) {
      try {
        const response = await Cost.create(name, category, money);
        store.commit("addCost", response.data);
      } catch (error) {
        throw error;
      }
    },
    async deleteCost(store, id) {
      try {
        await Cost.delete(id);
        store.commit("removeCost", id);
      } catch (error) {
        throw error;
      }
    },
    clearCosts(store) {
      store.commit("clearCosts");
    },
  },
};
