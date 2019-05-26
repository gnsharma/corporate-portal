<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Cantilever</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <test-table />
    </v-content>
  </v-app>
</template>

<script>
import TestTable from '@/components/TestTable.vue'; // @ is an alias to /src

export default {
  name: 'App',
  components: {
    TestTable
  },
  data () {
    return {
      //
    }
  }
}
</script>
