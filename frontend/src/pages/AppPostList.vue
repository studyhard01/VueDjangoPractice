<template>
  <v-app>
    <MainMenu></MainMenu>

    <v-main>
      <PostList></PostList>
    </v-main>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue"
import PostList from '../components/PostList.vue';

export default {
  name: 'App',

  components: {
    MainMenu,
    PostList,
  },

  data: () => ({
    drawer: false,
  }),
};
</script>


