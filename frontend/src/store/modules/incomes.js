/* eslint no-useless-catch: 0 */
import { Income } from "../../api/incomes";

export default {
  namespaced: true,
  state: {
    incomes: [],
    incomesIsLoading: false,
    hasNext: false,
  },
  getters: {
    incomes(state) {
      return state.incomes;
    },
    incomesIsLoading(state) {
      return state.incomesIsLoading;
    },
    hasNext(state) {
      return state.hasNext;
    },
  },
  mutations: {
    setIncomes(state, incomes) {
      state.incomes.push(...incomes);
    },
    addIncome(state, income) {
      state.incomes.unshift(income);
    },
    clearIncomes(state) {
      state.incomes = [];
    },
    removeIncome(state, id) {
      state.incomes = state.incomes.filter((income) => {
        return income.id != id;
      });
    },
    setLoad(state, isLoading) {
      state.incomesIsLoading = isLoading;
    },
    setHasNext(state, hasNext) {
      state.hasNext = hasNext;
    },
  },
  actions: {
    async getIncomes(store, { limit, offset }) {
      try {
        store.commit("setLoad", true);
        const incomes = await Income.list(limit, offset);
        if (incomes.data.length < limit - offset) {
          store.commit("setHasNext", false);
        } else {
          store.commit("setHasNext", true);
        }
        store.commit("setIncomes", incomes.data);
      } catch (error) {
        throw error;
      } finally {
        store.commit("setLoad", false);
      }
    },
    async deleteIncome(store, id) {
      try {
        await Income.delete(id);
        store.commit("removeIncome", id);
      } catch (error) {
        throw error;
      }
    },
    async createIncome(store, { name, money, user }) {
      try {
        const response = await Income.create(name, money, user);
        store.commit("addIncome", response.data);
      } catch (error) {
        throw error;
      }
    },
    clearIncomes(store) {
      store.commit("clearIncomes");
    },
  },
};
