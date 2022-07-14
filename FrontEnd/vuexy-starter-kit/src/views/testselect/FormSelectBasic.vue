<template>
  <b-card-code title="BootstrapVue Select">
    <b-card-text>
      <span>Bootstrap custom </span>
      <code>&lt;select&gt;</code>
      <span> using custom styles. Optionally specify options based on an array, array of objects, or an object.</span>
    </b-card-text>

    <div>
      <b-form-select
        v-model="selected"
        :options="options"
      />
      <b-form-select
        v-model="selected"
        :options="options"
        size="sm"
        class="mt-1"
      />
      <div class="mt-1">
        Selected: <strong>{{ selected }}</strong>
      </div>
    </div>

    <!-- <template #code>
      {{ codeBasic }}
    </template> -->




  </b-card-code>
</template>

<script>
import BCardCode from '@core/components/b-card-code'
import { BFormSelect, BCardText } from 'bootstrap-vue'

// import { codeBasic } from './code'
// import axios from 'axios';
//   let datas;
//   axios.get('http://127.0.0.1:5000/compounds/')
//   .then((getResponse) => {
//     console.log("GET Response")
//     console.log(getResponse.data);
//     datas = getResponse.data;
//     // response.send(data);
//   })
  

const axios = require('axios');

// function getLeagues () {
//   return axios.get('http://127.0.0.1:5000/compounds/')
//   .then(response => {
//     return response.data
//   })
//   .catch(error => {
//     console.log(error);
//     return Promise.reject(error);
//   });
// }
// const consoleLeagues = async () => {
//   const leagues = await getLeagues();
//   console.log(typeof leagues);
//   console.log(leagues.data[0].ester);
//   return leagues;
// };
// let test;
// consoleLeagues()
// console.log( test);

export default {
  components: {
    BCardCode,
    BFormSelect,
    BCardText,
  },
  data() 
  {
    return {
      selected: null,
      options: [
        { value: null, text: 'Please select an optionss' },
        { value: 'a', text: 'This is First option' },
        { value: 'b', text: 'Simple Option' },
        { value: { C: '3PO' }, text: 'This is an option with object value' },
        { value: 'd', text: 'This one is disabled', disabled: true },
      ],
      // codeBasic,
    }
  }
  
  // mounted()
  // {
  //   axios.get('http://127.0.0.1:5000/compounds/').then(response => {return response.data})
  // }
}
</script>

<!-- <script>

import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.get(`http://jsonplaceholder.typicode.com/posts`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script> -->


