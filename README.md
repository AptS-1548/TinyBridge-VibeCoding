# TinyBridge 短链接服务

> 🚀 **AI 高效编程示例项目** - 展示如何使用 Claude Code 快速构建全栈应用

一个简洁高效的短链接服务，包含完整的前后端实现。这个项目主要用于演示如何通过 AI 辅助开发来快速构建现代化的 Web 应用。

## 📋 项目概览

### 功能特性

- ✨ **短链接生成** - 将长链接转换为短链接
- 📊 **点击统计** - 实时统计短链接访问次数
- ⏰ **过期管理** - 支持设置链接过期时间
- 🔧 **链接管理** - 查看、编辑、删除短链接
- 📱 **响应式设计** - 完美适配桌面和移动设备
- 🔗 **自动跳转** - 访问短链接自动重定向到目标地址

### 技术栈

**前端**
- Vue 3 + TypeScript
- Tailwind CSS 4
- Vue Router
- Pinia
- Heroicons
- Vite

**后端**
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## 🛠️ 项目结构

```
TinyBridge/
├── docs/                           # 项目文档
│   ├── api.md                      # API 接口文档
│   └── README.md                   # 主文档
├── tinybridge-frontend/            # Vue 3 前端项目
│   ├── src/
│   │   ├── api/                    # API 客户端
│   │   ├── components/             # Vue 组件
│   │   ├── views/                  # 页面组件
│   │   └── router/                 # 路由配置
│   ├── package.json
│   └── vite.config.ts
└── tinybridge-backend/             # FastAPI 后端项目
    ├── app/
    │   ├── api/                    # API 路由
    │   ├── models/                 # 数据模型
    │   ├── database/               # 数据库配置
    │   └── core/                   # 核心配置
    ├── main.py                     # 应用入口
    └── requirements.txt            # Python 依赖
```

## 🚀 快速开始

### 环境要求

- Node.js 20.19.0+ 或 22.12.0+
- Python 3.8+
- Yarn (推荐) 或 npm

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd TinyBridge
```

### 2. 启动后端服务

```bash
cd tinybridge-backend

# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\\Scripts\\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 启动服务
python main.py
```

后端服务将运行在 `http://localhost:8000`

### 3. 启动前端应用

```bash
cd tinybridge-frontend

# 安装依赖
yarn install

# 启动开发服务器
yarn dev
```

前端应用将运行在 `http://localhost:5173`

## 📖 使用指南

### 创建短链接

1. 访问 `http://localhost:5173`
2. 点击"创建新链接"按钮
3. 输入原始链接地址
4. （可选）设置过期时间
5. 点击"创建短链接"

### 管理链接

- **查看列表** - 在首页查看所有创建的短链接
- **查看详情** - 点击"查看"按钮查看链接详细信息
- **编辑链接** - 在详情页面修改目标地址或过期时间
- **删除链接** - 在列表或详情页面删除不需要的链接

### 使用短链接

访问生成的短链接（如 `http://localhost:8000/abc123`），将自动重定向到目标地址，同时增加点击统计。

## 🔌 API 接口

### 基础地址
```
http://localhost:8000/api
```

### 主要端点

| 方法 | 路径 | 描述 |
|------|------|------|
| `POST` | `/links` | 创建短链接 |
| `GET` | `/links` | 获取链接列表 |
| `GET` | `/links/{id}` | 获取单个链接信息 |
| `PATCH` | `/links/{id}` | 更新链接 |
| `DELETE` | `/links/{id}` | 删除链接 |
| `GET` | `/{id}` | 短链跳转 |

### API 文档

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

详细的 API 文档请查看 [docs/api.md](docs/api.md)

## 🎯 AI 开发示例

这个项目展示了如何使用 Claude Code 进行高效的全栈开发：

### 开发流程

1. **需求分析** - 通过对话明确项目需求和技术选型
2. **架构设计** - AI 协助设计项目结构和技术架构
3. **代码生成** - 自动生成前后端代码框架
4. **功能实现** - 逐步实现各个功能模块
5. **测试验证** - 自动化测试和功能验证
6. **文档编写** - 生成完整的项目文档

### AI 辅助的优势

- ⚡ **快速原型** - 从想法到可运行的原型只需几分钟
- 🎯 **最佳实践** - 自动应用行业最佳实践和代码规范
- 🔧 **全栈能力** - 同时处理前端、后端、数据库等各个层面
- 📚 **完整文档** - 自动生成规范的项目文档和 API 文档
- 🐛 **错误处理** - 智能的错误处理和边界情况考虑

## 📝 开发日志

### 项目创建过程

1. **API 设计** (5分钟)
   - 分析需求，设计 RESTful API
   - 定义数据模型和接口规范

2. **后端开发** (15分钟)
   - 创建 FastAPI 项目结构
   - 实现数据模型和数据库配置
   - 开发所有 API 端点
   - 添加 CORS 支持和错误处理

3. **前端开发** (20分钟)
   - 创建 Vue 3 + TypeScript 项目
   - 实现 API 客户端和类型定义
   - 开发页面组件和路由
   - 添加响应式布局和交互

4. **集成测试** (5分钟)
   - 测试前后端通信
   - 验证核心功能

5. **文档编写** (10分钟)
   - 生成项目文档
   - 添加开发和部署指南

**总计时间**: 约 55 分钟（从零到完整可部署的应用）

## 🌟 学习要点

通过这个项目，你可以学习到：

- 如何与 AI 有效协作进行软件开发
- 现代全栈开发的最佳实践
- Vue 3 + TypeScript 的企业级开发模式
- FastAPI 的高效 API 开发
- 前后端分离架构的设计原则
- RESTful API 的设计和实现

## 🤝 贡献指南

这是一个教学示例项目，欢迎提交 Issue 和 Pull Request 来改进项目。

## 📄 许可证

MIT License

## 🙏 致谢

- 感谢 Claude Code 提供的强大 AI 编程辅助
- 感谢 Vue.js、FastAPI 等优秀的开源框架

---

**✨ 记住：好的工具能让开发变得简单高效，而 AI 正是这样的工具！**