<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <ToDoList title="ToDo List:"/>
  </div>
</template>

<script>
import ToDoList from './components/ToDoList.vue'

export default {
  name: 'app',
  components: {
    ToDoList
  }
}
</script>

<style>
</style>
