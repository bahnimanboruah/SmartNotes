<template>
  <div class="container mt-5">
    <div v-for="article in articles" :key="article.id">
      <h3>
      <router-link
      class="link-style"
      :to="{name:'details', parms:{id:article.id}}"
      >
      {{article.title}}
      </router-link>
      
      </h3>


    <hr/> 
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: [],
    };
  },

  methods: {
    getArticles() {
      fetch("http://localhost:5000//get", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.articles = data; 
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getArticles();
  },
};
</script>

<style>
.link-style
{
font-weight:bold;
color:black;
text-decoration: none;
}
.link-style:hover
{
color:gray;
text-decoration: none;
}
</style>
