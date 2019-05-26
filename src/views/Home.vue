<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <TestTable />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TestTable from '@/components/TestTable.vue'; // @ is an alias to /src

@Component({
  components: {
    TestTable,
  },
})
export default class Home extends Vue {}
</script>
