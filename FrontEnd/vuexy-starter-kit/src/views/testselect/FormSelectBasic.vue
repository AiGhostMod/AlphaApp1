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

export default {
  components: {
    BCardCode,
    BFormSelect,
    BCardText,
  },
  data() {
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
  },
}
import axios from 'axios';
// axios
//   .get('https://api.coindesk.com/v1/bpi/currentprice.json')
//   .then(response => (this.info = response.data.bpi))
//   .then(console.log("HIIIIIII1"))
//   .then(console.log(this))
//   .catch(error => console.log(error))
  let data
  axios.get('http://localhost:7071/api/Get_Compounds')
  .then((getResponse) => {
    console.log("GET Response")
    console.log(getResponse.data);
    data = getResponse.data;
    // response.send(data);
  })


  

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