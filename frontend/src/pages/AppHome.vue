<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-main>
      <HelloWorld/>
    </v-main>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from '../components/HelloWorld';
import MainMenu from "@/components/MainMenu.vue";

export default {
  name: 'App',

  components: {
    MainMenu,
    HelloWorld,
  },

  data: () => ({
    // drawer: false,
  }),
};
</script>


