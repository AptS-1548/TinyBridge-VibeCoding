import { apiClient } from './client'
import type {
  Link,
  CreateLinkRequest,
  CreateLinkResponse,
  UpdateLinkRequest,
  GetLinksParams,
} from './types'

export const linksApi = {
  // 获取短链接列表
  async getLinks(params: GetLinksParams = {}): Promise<Link[]> {
    const queryParams = {
      offset: params.offset?.toString() || '0',
      limit: params.limit?.toString() || '20',
    }
    return apiClient.get<Link[]>('/links', queryParams)
  },

  // 获取单个短链接信息
  async getLink(id: string): Promise<Link> {
    return apiClient.get<Link>(`/links/${id}`)
  },

  // 创建短链接
  async createLink(data: CreateLinkRequest): Promise<CreateLinkResponse> {
    return apiClient.post<CreateLinkResponse>('/links', data)
  },

  // 更新短链接
  async updateLink(id: string, data: UpdateLinkRequest): Promise<void> {
    return apiClient.patch<void>(`/links/${id}`, data)
  },

  // 删除短链接
  async deleteLink(id: string): Promise<void> {
    return apiClient.delete<void>(`/links/${id}`)
  },
}

export default linksApi