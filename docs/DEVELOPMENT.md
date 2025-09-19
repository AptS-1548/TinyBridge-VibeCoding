# TinyBridge 开发指南

## 🛠️ 开发环境配置

### 系统要求

- **操作系统**: macOS, Linux, Windows
- **Node.js**: 20.19.0+ 或 22.12.0+
- **Python**: 3.8+
- **包管理器**: Yarn (推荐) 或 npm
- **IDE**: VS Code (推荐) 或其他支持 TypeScript 的编辑器

### 开发工具推荐

**VS Code 扩展**
- Vue - Official
- Python
- Pylance
- Thunder Client (API 测试)
- GitLens
- Prettier
- ESLint

## 🚀 本地开发

### 1. 项目初始化

```bash
# 克隆项目
git clone <repository-url>
cd TinyBridge

# 安装所有依赖
./scripts/setup.sh  # 如果有安装脚本
```

### 2. 后端开发

```bash
cd tinybridge-backend

# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境 (macOS/Linux)
source .venv/bin/activate

# 激活虚拟环境 (Windows)
.venv\\Scripts\\activate

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
python main.py

# 或者使用 uvicorn 直接启动
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**后端服务地址**: `http://localhost:8000`
**API 文档**: `http://localhost:8000/docs`

### 3. 前端开发

```bash
cd tinybridge-frontend

# 安装依赖
yarn install

# 启动开发服务器
yarn dev

# 构建生产版本
yarn build

# 预览构建结果
yarn preview

# 代码检查
yarn lint

# 类型检查
yarn type-check
```

**前端应用地址**: `http://localhost:5173`

## 📦 部署指南

### 生产环境部署

#### 后端部署

**使用 Docker (推荐)**

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# 构建镜像
docker build -t tinybridge-backend .

# 运行容器
docker run -p 8000:8000 tinybridge-backend
```

**直接部署**

```bash
# 安装依赖
pip install -r requirements.txt

# 使用 gunicorn 部署
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### 前端部署

```bash
# 构建生产版本
yarn build

# dist 目录包含所有静态文件
# 可以部署到任何静态文件托管服务
```

**部署选项**:
- Vercel
- Netlify
- GitHub Pages
- Nginx + 静态文件服务

#### 环境变量配置

**后端 (.env)**
```bash
DATABASE_URL=sqlite:///./tinybridge.db
SECRET_KEY=your-production-secret-key
BASE_URL=https://your-domain.com
```

**前端**
```typescript
// 修改 API 基础地址
export const apiClient = new ApiClient('https://your-api-domain.com/api')
```

### 使用 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./tinybridge-backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./tinybridge.db
      - BASE_URL=http://localhost:8000
    volumes:
      - ./data:/app/data

  frontend:
    build: ./tinybridge-frontend
    ports:
      - "3000:80"
    depends_on:
      - backend
```

```bash
# 启动所有服务
docker-compose up -d

# 停止服务
docker-compose down
```

## 🔧 开发最佳实践

### 代码规范

**前端**
- 使用 TypeScript 严格模式
- 遵循 Vue 3 Composition API 风格
- 使用 ESLint + Prettier 进行代码格式化
- 组件命名使用 PascalCase
- 文件命名使用 kebab-case

**后端**
- 遵循 PEP 8 代码规范
- 使用类型注解
- API 响应使用 Pydantic 模型
- 错误处理要完整
- 添加适当的日志记录

### Git 工作流

```bash
# 功能开发分支
git checkout -b feature/short-description

# 提交信息格式
git commit -m "feat: add user authentication"
git commit -m "fix: resolve CORS issue"
git commit -m "docs: update API documentation"

# 推送并创建 Pull Request
git push origin feature/short-description
```

### 调试技巧

**前端调试**
- 使用 Vue Devtools
- 浏览器开发者工具
- console.log 和 debugger 语句

**后端调试**
- FastAPI 自动重载: `--reload`
- 日志输出: `logging` 模块
- API 测试: Swagger UI 或 Thunder Client

## 📊 性能优化

### 前端优化

- 使用 Vue 3 的懒加载路由
- 图片压缩和懒加载
- 代码分割和 Tree Shaking
- CDN 加速静态资源

### 后端优化

- 数据库查询优化
- 添加缓存层 (Redis)
- 使用连接池
- API 限流和分页

## 🧪 测试

### 前端测试

```bash
# 单元测试
yarn test:unit

# E2E 测试
yarn test:e2e

# 覆盖率报告
yarn test:coverage
```

### 后端测试

```bash
# 安装测试依赖
pip install pytest pytest-asyncio httpx

# 运行测试
pytest

# 覆盖率报告
pytest --cov=app tests/
```

## 🚨 故障排除

### 常见问题

**前端问题**
1. **依赖安装失败**: 清除 `node_modules` 重新安装
2. **类型错误**: 检查 TypeScript 配置
3. **CORS 错误**: 确认后端 CORS 配置

**后端问题**
1. **数据库连接失败**: 检查数据库 URL 配置
2. **模块导入错误**: 确认虚拟环境激活
3. **端口占用**: 更换端口或停止占用进程

### 日志查看

```bash
# 后端日志
tail -f logs/app.log

# 前端构建日志
yarn build --verbose

# Docker 日志
docker logs container_name
```

## 🔄 CI/CD

### GitHub Actions 示例

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '20'
        
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
        
    - name: Build Frontend
      run: |
        cd tinybridge-frontend
        yarn install
        yarn build
        
    - name: Test Backend
      run: |
        cd tinybridge-backend
        pip install -r requirements.txt
        pytest
        
    - name: Deploy
      run: |
        # 部署脚本
        echo "Deploy to production"
```

## 📱 移动端适配

项目已经使用响应式设计，支持各种设备：

- **断点设置**: Tailwind CSS 响应式断点
- **触摸优化**: 按钮和链接的触摸区域
- **性能考虑**: 移动端网络优化

## 🌍 国际化

如需添加多语言支持：

```bash
# 安装 vue-i18n
yarn add vue-i18n@9

# 配置语言文件
src/
  locales/
    zh-CN.json
    en-US.json
```

---

**💡 提示**: 开发过程中遇到问题，可以查看项目的 issue 页面或创建新的 issue。