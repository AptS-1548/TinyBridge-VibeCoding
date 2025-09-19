export interface Link {
  id: string
  url: string
  short_url: string
  clicks: number
  created_at: string
  expire_at?: string
}

export interface CreateLinkRequest {
  url: string
  expire_at?: string
}

export interface CreateLinkResponse {
  id: string
  url: string
  short_url: string
  created_at: string
  expire_at?: string
}

export interface UpdateLinkRequest {
  url?: string
  expire_at?: string
}

export interface GetLinksParams {
  offset?: number
  limit?: number
}

export interface ApiResponse<T> {
  data: T
  message?: string
}

export interface ApiError {
  message: string
  code?: number
}