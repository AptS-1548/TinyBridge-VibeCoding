<template>
  <div class="max-w-6xl mx-auto p-6">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">短链接管理</h1>
      <router-link
        to="/create"
        class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors"
      >
        创建新链接
      </router-link>
    </div>

    <div v-if="loading" class="text-center py-8">
      <div class="text-gray-500">加载中...</div>
    </div>

    <div v-else-if="error" class="text-center py-8 text-red-600">
      {{ error }}
    </div>

    <div v-else>
      <div class="bg-white shadow rounded-lg overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                短链接
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                原始链接
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                点击数
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                创建时间
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                操作
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="link in links" :key="link.id">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-blue-600">
                  <a :href="link.short_url" target="_blank" class="hover:underline">
                    {{ link.short_url }}
                  </a>
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm text-gray-900 truncate max-w-md" :title="link.url">
                  {{ link.url }}
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ link.clicks || 0 }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">
                  {{ formatDate(link.created_at) }}
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <router-link
                  :to="`/links/${link.id}`"
                  class="text-blue-600 hover:text-blue-900 mr-4"
                >
                  查看
                </router-link>
                <button
                  @click="deleteLink(link.id)"
                  class="text-red-600 hover:text-red-900"
                >
                  删除
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="links.length === 0" class="text-center py-8 text-gray-500">
        暂无链接数据
      </div>

      <!-- 分页 -->
      <div v-if="links.length > 0" class="mt-6 flex justify-between items-center">
        <div class="text-sm text-gray-700">
          显示 {{ offset + 1 }} - {{ Math.min(offset + limit, offset + links.length) }} 项
        </div>
        <div class="flex space-x-2">
          <button
            @click="loadPrevious"
            :disabled="offset === 0"
            class="px-3 py-1 border rounded disabled:opacity-50 disabled:cursor-not-allowed"
          >
            上一页
          </button>
          <button
            @click="loadNext"
            :disabled="links.length < limit"
            class="px-3 py-1 border rounded disabled:opacity-50 disabled:cursor-not-allowed"
          >
            下一页
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { linksApi, type Link } from '@/api'

const links = ref<Link[]>([])
const loading = ref(false)
const error = ref('')
const offset = ref(0)
const limit = ref(20)

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('zh-CN')
}

const loadLinks = async () => {
  try {
    loading.value = true
    error.value = ''
    links.value = await linksApi.getLinks({
      offset: offset.value,
      limit: limit.value
    })
  } catch (err: any) {
    error.value = err.message || '加载链接失败'
  } finally {
    loading.value = false
  }
}

const deleteLink = async (id: string) => {
  if (!confirm('确定要删除这个链接吗？')) return
  
  try {
    await linksApi.deleteLink(id)
    await loadLinks()
  } catch (err: any) {
    alert(err.message || '删除失败')
  }
}

const loadPrevious = () => {
  if (offset.value > 0) {
    offset.value = Math.max(0, offset.value - limit.value)
    loadLinks()
  }
}

const loadNext = () => {
  offset.value += limit.value
  loadLinks()
}

onMounted(() => {
  loadLinks()
})
</script>