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
            text: 'Test ID',
            align: 'left',
            sortable: false,
            value: 'id'
          },
          { text: 'Test Name', value: 'name' },
          { text: 'Date', value: 'date' },
          { text: 'No. of Users', value: 'usersCount' },
        ],
        tests: []
      }
    }
  }
</script>