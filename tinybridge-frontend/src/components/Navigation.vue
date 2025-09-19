<template>
  <nav class="bg-white shadow-sm border-b">
    <div class="max-w-6xl mx-auto px-6">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center space-x-8">
          <router-link
            to="/links"
            class="text-xl font-bold text-gray-900"
          >
            TinyBridge
          </router-link>
          
          <div class="hidden md:flex space-x-6">
            <router-link
              to="/links"
              class="text-gray-600 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
              :class="{ 'text-blue-600': $route.path === '/links' || $route.path.startsWith('/links/') }"
            >
              链接管理
            </router-link>
            <router-link
              to="/create"
              class="text-gray-600 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
              :class="{ 'text-blue-600': $route.path === '/create' }"
            >
              创建链接
            </router-link>
          </div>
        </div>

        <div class="md:hidden">
          <button
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="text-gray-600 hover:text-gray-900"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                v-if="!mobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- 移动端菜单 -->
      <div v-if="mobileMenuOpen" class="md:hidden py-2 border-t">
        <router-link
          to="/links"
          class="block px-3 py-2 text-gray-600 hover:text-gray-900"
          :class="{ 'text-blue-600': $route.path === '/links' || $route.path.startsWith('/links/') }"
          @click="mobileMenuOpen = false"
        >
          链接管理
        </router-link>
        <router-link
          to="/create"
          class="block px-3 py-2 text-gray-600 hover:text-gray-900"
          :class="{ 'text-blue-600': $route.path === '/create' }"
          @click="mobileMenuOpen = false"
        >
          创建链接
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const mobileMenuOpen = ref(false)
</script>