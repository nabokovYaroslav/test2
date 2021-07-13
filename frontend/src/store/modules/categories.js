/* eslint no-useless-catch: 0 */
import { Category } from "../../api/categories";

export default {
  namespaced: true,
  state: {
    categories: [],
    categoriesIsLoading: false,
    hasNext: false,
  },
  getters: {
    categories(state) {
      return state.categories;
    },
    categoriesIsLoading(state) {
      return state.categoriesIsLoading;
    },
    hasNext(state) {
      return state.hasNext;
    },
  },
  mutations: {
    setCategories(state, categories) {
      state.categories.push(...categories);
    },
    addCategory(state, cost) {
      state.categories.unshift(cost);
    },
    clearCategories(state) {
      state.categories = [];
    },
    removeCategory(state, id) {
      state.categories = state.categories.filter((category) => {
        return category.id != id;
      });
    },
    setLoad(state, isLoading) {
      state.categoriesIsLoading = isLoading;
    },
    setHasNext(state, hasNext) {
      state.hasNext = hasNext;
    },
  },
  actions: {
    async getCategories(store, { limit, offset }) {
      try {
        store.commit("setLoad", true);
        const categories = await Category.list(limit, offset);
        if (categories.data.length < limit - offset) {
          store.commit("setHasNext", false);
        } else {
          store.commit("setHasNext", true);
        }
        store.commit("setCategories", categories.data);
      } catch (error) {
        throw error;
      } finally {
        store.commit("setLoad", false);
      }
    },
    async deleteCategory(store, id) {
      try {
        await Category.delete(id);
        store.commit("removeCategory", id);
      } catch (error) {
        throw error;
      }
    },
    async createCategory(store, { name, user }) {
      try {
        const response = await Category.create(name, user);
        store.commit("addCategory", response.data);
      } catch (error) {
        throw error;
      }
    },
    clearCategories(store) {
      store.commit("clearCategories");
    },
    async getCostInRange(store, { startDate, endDate, categories }) {
      try {
        const response = await Category.costInRange(
          startDate,
          endDate,
          categories
        );
        return response.data;
      } catch (error) {
        throw error;
      }
    },
  },
};
