<template>
  <v-app>
    <MainMenu></MainMenu>

    <v-main>
      <PostDetail></PostDetail>
    </v-main>
  </v-app>
</template>

<script>
import PostDetail from '../components/PostDetail.vue';
import MainMenu from '../components/MainMenu.vue'

export default {
  name: 'App',

  components: {
    MainMenu,
    PostDetail,
  },

  data: () => ({
    drawer: false,
  }),
};
</script>


