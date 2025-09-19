<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <Navigation />
    <main class="py-8">
      <RouterView />
    </main>
  </div>
</template>
