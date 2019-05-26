<template>
  <v-data-table
    :headers="headers"
    :items="tests"
    class="elevation-1"
  >
    <template v-slot:no-data>
      <v-alert :value="true" color="error" icon="info">
        Sorry, there are no tests currently:(
      </v-alert>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            text: 'User Name',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { text: 'User Email', value: 'email' },
          { text: 'Test Taker', value: 'iste' },
          { text: 'Question Creation', value: 'usersCount' },
        ],
        tests: []
      }
    }
  }
</script>