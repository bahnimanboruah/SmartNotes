<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">

      <!-- Brand -->
      <router-link class="navbar-brand text-style" to="/">
        SmartNotes
      </router-link>
<form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="search for notes..." aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
      <!-- Toggler -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">

          <li class="nav-item mx-2">
            <router-link class="btn btn-primary" to="/Home">
              Home
            </router-link>
          </li>

          <li class="nav-item">
            <router-link class="btn btn-success" to="/create">
              Add Notes
            </router-link>
          </li>

        </ul>
      </div>

    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.text-style {
  font-size: 30px !important;
  font-family: fantasy !important;
  color: green !important;
}
</style>
