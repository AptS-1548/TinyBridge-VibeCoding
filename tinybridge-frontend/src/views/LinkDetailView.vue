<template>
  <div class="max-w-4xl mx-auto p-6">
    <div class="mb-6">
      <router-link 
        to="/links" 
        class="text-blue-600 hover:text-blue-800 text-sm"
      >
        ← 返回链接列表
      </router-link>
      <h1 class="text-3xl font-bold text-gray-900 mt-2">链接详情</h1>
    </div>

    <div v-if="loading" class="text-center py-8">
      <div class="text-gray-500">加载中...</div>
    </div>

    <div v-else-if="error" class="text-center py-8 text-red-600">
      {{ error }}
    </div>

    <div v-else-if="link" class="space-y-6">
      <!-- 基本信息 -->
      <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">基本信息</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">短链接ID：</label>
            <div class="text-sm text-gray-900 font-mono">{{ link.id }}</div>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">点击次数：</label>
            <div class="text-sm text-gray-900 font-semibold">{{ link.clicks || 0 }}</div>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">创建时间：</label>
            <div class="text-sm text-gray-900">{{ formatDate(link.created_at) }}</div>
          </div>
          <div v-if="link.expire_at">
            <label class="block text-sm font-medium text-gray-700 mb-1">过期时间：</label>
            <div class="text-sm text-gray-900">{{ formatDate(link.expire_at) }}</div>
          </div>
        </div>
      </div>

      <!-- 链接信息 -->
      <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">链接信息</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">短链接：</label>
            <div class="flex items-center space-x-2">
              <input
                :value="link.short_url"
                readonly
                class="flex-1 px-3 py-2 bg-gray-50 border border-gray-300 rounded-md text-sm"
              />
              <button
                @click="copyToClipboard(link.short_url)"
                class="px-3 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 text-sm"
              >
                复制
              </button>
              <a
                :href="link.short_url"
                target="_blank"
                class="px-3 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 text-sm"
              >
                访问
              </a>
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">原始链接：</label>
            <div class="flex items-center space-x-2">
              <input
                :value="link.url"
                readonly
                class="flex-1 px-3 py-2 bg-gray-50 border border-gray-300 rounded-md text-sm"
              />
              <button
                @click="copyToClipboard(link.url)"
                class="px-3 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 text-sm"
              >
                复制
              </button>
              <a
                :href="link.url"
                target="_blank"
                class="px-3 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 text-sm"
              >
                访问
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- 编辑链接 -->
      <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-xl font-semibold text-gray-900 mb-4">编辑链接</h2>
        <form @submit.prevent="updateLink" class="space-y-4">
          <div>
            <label for="edit-url" class="block text-sm font-medium text-gray-700 mb-1">
              目标链接：
            </label>
            <input
              id="edit-url"
              v-model="editForm.url"
              type="url"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          
          <div>
            <label for="edit-expire" class="block text-sm font-medium text-gray-700 mb-1">
              过期时间：
            </label>
            <input
              id="edit-expire"
              v-model="editForm.expire_at"
              type="datetime-local"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
            <p class="text-sm text-gray-500 mt-1">留空表示永不过期</p>
          </div>

          <div v-if="updateError" class="text-red-600 text-sm">
            {{ updateError }}
          </div>

          <div class="flex space-x-3">
            <button
              type="submit"
              :disabled="updating"
              class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {{ updating ? '保存中...' : '保存修改' }}
            </button>
            <button
              type="button"
              @click="resetEditForm"
              class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300 transition-colors"
            >
              重置
            </button>
          </div>
        </form>
      </div>

      <!-- 危险操作 -->
      <div class="bg-red-50 border border-red-200 rounded-lg p-6">
        <h2 class="text-xl font-semibold text-red-800 mb-4">危险操作</h2>
        <p class="text-sm text-red-600 mb-4">
          删除链接后将无法恢复，所有访问该短链接的请求都将失效。
        </p>
        <button
          @click="deleteLink"
          class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors"
        >
          删除链接
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { linksApi, type Link } from '@/api'

const route = useRoute()
const router = useRouter()

const link = ref<Link | null>(null)
const loading = ref(false)
const error = ref('')

const editForm = ref({
  url: '',
  expire_at: ''
})
const updating = ref(false)
const updateError = ref('')

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('zh-CN')
}

const formatDateForInput = (dateString: string) => {
  return new Date(dateString).toISOString().slice(0, 16)
}

const loadLink = async () => {
  const id = route.params.id as string
  if (!id) {
    error.value = '无效的链接ID'
    return
  }
  
  try {
    loading.value = true
    error.value = ''
    link.value = await linksApi.getLink(id)
    resetEditForm()
  } catch (err: any) {
    error.value = err.message || '加载链接详情失败'
  } finally {
    loading.value = false
  }
}

const resetEditForm = () => {
  if (link.value) {
    editForm.value = {
      url: link.value.url,
      expire_at: link.value.expire_at ? formatDateForInput(link.value.expire_at) : ''
    }
  }
}

const updateLink = async () => {
  if (!link.value) return
  
  try {
    updating.value = true
    updateError.value = ''
    
    const data: any = {
      url: editForm.value.url
    }
    
    if (editForm.value.expire_at) {
      data.expire_at = new Date(editForm.value.expire_at).toISOString()
    } else {
      data.expire_at = null
    }
    
    await linksApi.updateLink(link.value.id, data)
    await loadLink()
    alert('链接更新成功')
  } catch (err: any) {
    updateError.value = err.message || '更新链接失败'
  } finally {
    updating.value = false
  }
}

const deleteLink = async () => {
  if (!link.value) return
  
  if (!confirm('确定要删除这个链接吗？此操作不可恢复！')) return
  
  try {
    await linksApi.deleteLink(link.value.id)
    alert('链接已删除')
    router.push('/links')
  } catch (err: any) {
    alert(err.message || '删除链接失败')
  }
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
    alert('内容已复制到剪贴板')
  } catch {
    const textArea = document.createElement('textarea')
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    alert('内容已复制到剪贴板')
  }
}

onMounted(() => {
  loadLink()
})
</script>