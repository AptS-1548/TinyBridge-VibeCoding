## 资源设计

核心资源是 `links`（短链接条目）。
每个短链接包含：

* `id`（短链唯一标识，比如 `abc123`）
* `url`（原始长链接）
* `created_at`（创建时间）
* `expire_at`（过期时间，可选）
* `clicks`（点击次数，可选）

---

## API 路径设计

### 1. 创建短链接

**POST** `/api/links`
请求体：

```json
{
  "url": "https://example.com/some/very/long/path",
  "expire_at": "2025-12-31T23:59:59Z"
}
```

响应：

```json
{
  "id": "abc123",
  "url": "https://example.com/some/very/long/path",
  "short_url": "https://short.ly/abc123",
  "created_at": "2025-09-19T06:00:00Z",
  "expire_at": "2025-12-31T23:59:59Z"
}
```

---

### 2. 获取短链接列表

**GET** `/api/links?offset=0&limit=20`
响应：

```json
[
  {
    "id": "abc123",
    "url": "https://example.com",
    "short_url": "https://short.ly/abc123",
    "clicks": 42,
    "created_at": "2025-09-19T06:00:00Z"
  },
  {
    "id": "xyz789",
    "url": "https://foo.com/bar",
    "short_url": "https://short.ly/xyz789",
    "clicks": 7,
    "created_at": "2025-09-18T12:34:56Z"
  }
]
```

---

### 3. 获取单个短链接信息

**GET** `/api/links/{id}`
响应：

```json
{
  "id": "abc123",
  "url": "https://example.com",
  "short_url": "https://short.ly/abc123",
  "clicks": 42,
  "created_at": "2025-09-19T06:00:00Z",
  "expire_at": "2025-12-31T23:59:59Z"
}
```

---

### 4. 更新短链接（例如修改目标地址/过期时间）

**PATCH** `/api/links/{id}`
请求体：

```json
{
  "url": "https://new-destination.com",
  "expire_at": "2026-01-01T00:00:00Z"
}
```

---

### 5. 删除短链接

**DELETE** `/api/links/{id}`
响应：`204 No Content`

---

### 6. 短链跳转

**GET** `/{id}`

* 服务入口，直接 302 跳转到目标地址。
* 例：访问 `https://short.ly/abc123` → 302 → `https://example.com`


