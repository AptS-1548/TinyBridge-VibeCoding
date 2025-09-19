<template>
  <div class="max-w-2xl mx-auto p-6">
    <div class="mb-6">
      <h1 class="text-3xl font-bold text-gray-900">创建短链接</h1>
      <p class="text-gray-600 mt-2">输入长链接来生成一个短链接</p>
    </div>

    <div class="bg-white shadow rounded-lg p-6">
      <form @submit.prevent="createLink" class="space-y-6">
        <div>
          <label for="url" class="block text-sm font-medium text-gray-700 mb-2">
            原始链接 *
          </label>
          <input
            id="url"
            v-model="form.url"
            type="url"
            required
            placeholder="https://example.com/very/long/url"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>

        <div>
          <label for="expire_at" class="block text-sm font-medium text-gray-700 mb-2">
            过期时间（可选）
          </label>
          <input
            id="expire_at"
            v-model="form.expire_at"
            type="datetime-local"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <p class="text-sm text-gray-500 mt-1">留空表示永不过期</p>
        </div>

        <div v-if="error" class="text-red-600 text-sm">
          {{ error }}
        </div>

        <div class="flex space-x-4">
          <button
            type="submit"
            :disabled="loading || !form.url"
            class="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {{ loading ? '创建中...' : '创建短链接' }}
          </button>
          <router-link
            to="/links"
            class="flex-1 bg-gray-200 text-gray-800 py-2 px-4 rounded-md hover:bg-gray-300 transition-colors text-center"
          >
            取消
          </router-link>
        </div>
      </form>
    </div>

    <!-- 创建成功的结果显示 -->
    <div v-if="createdLink" class="mt-6 bg-green-50 border border-green-200 rounded-lg p-6">
      <h3 class="text-lg font-medium text-green-800 mb-4">短链接创建成功！</h3>
      <div class="space-y-3">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">短链接：</label>
          <div class="flex items-center space-x-2">
            <input
              :value="createdLink.short_url"
              readonly
              class="flex-1 px-3 py-2 bg-gray-50 border border-gray-300 rounded-md text-sm"
            />
            <button
              @click="copyToClipboard(createdLink.short_url)"
              class="px-3 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 text-sm"
            >
              复制
            </button>
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">原始链接：</label>
          <div class="text-sm text-gray-600">{{ createdLink.url }}</div>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">创建时间：</label>
          <div class="text-sm text-gray-600">{{ formatDate(createdLink.created_at) }}</div>
        </div>
        <div v-if="createdLink.expire_at">
          <label class="block text-sm font-medium text-gray-700 mb-1">过期时间：</label>
          <div class="text-sm text-gray-600">{{ formatDate(createdLink.expire_at) }}</div>
        </div>
      </div>
      
      <div class="mt-4 flex space-x-3">
        <router-link
          to="/links"
          class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 text-sm"
        >
          查看所有链接
        </router-link>
        <button
          @click="resetForm"
          class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300 text-sm"
        >
          创建另一个
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { linksApi, type CreateLinkResponse } from '@/api'

const form = ref({
  url: '',
  expire_at: ''
})

const loading = ref(false)
const error = ref('')
const createdLink = ref<CreateLinkResponse | null>(null)

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('zh-CN')
}

const createLink = async () => {
  try {
    loading.value = true
    error.value = ''
    
    const data: any = {
      url: form.value.url
    }
    
    if (form.value.expire_at) {
      data.expire_at = new Date(form.value.expire_at).toISOString()
    }
    
    createdLink.value = await linksApi.createLink(data)
  } catch (err: any) {
    error.value = err.message || '创建链接失败'
  } finally {
    loading.value = false
  }
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
    alert('链接已复制到剪贴板')
  } catch {
    // 降级方案
    const textArea = document.createElement('textarea')
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    alert('链接已复制到剪贴板')
  }
}

const resetForm = () => {
  form.value = {
    url: '',
    expire_at: ''
  }
  createdLink.value = null
  error.value = ''
}
</script>