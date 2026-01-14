# Render 部署指南

## 准备工作

✅ 已完成：
- Docker 配置文件
- Render 配置文件 (render.yaml)
- 代码已推送到 GitHub

## 部署步骤

### 1. 注册 Render 账号

访问 https://render.com 并使用GitHub账号登录。

### 2. 创建新的 Web Service

1. 点击 "New +" → "Web Service"
2. 连接你的 GitHub 仓库：`isDieServer`
3. Render 会自动检测到 `render.yaml` 配置

### 3. 配置环境变量

在 Environment 部分添加：

| Key | Value |
|-----|-------|
| SUPABASE_URL | `https://fpgmrrhzytyooqusekot.supabase.co` |
| SUPABASE_KEY | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (你的完整key) |
| FLASK_ENV | `production` |
| SECRET_KEY | (Render会自动生成) |

### 4. 部署设置

- **Runtime**: Docker
- **Plan**: Free
- **Region**: 选择距离你最近的区域（如 Singapore）
- **Health Check Path**: `/health`

点击 "Create Web Service"，Render 会自动：
- 构建 Docker 镜像
- 部署服务
- 提供免费 HTTPS 域名（如 `isdieserver.onrender.com`）

### 5. 绑定自定义域名

部署成功后：

1. 进入你的服务 → Settings → Custom Domains
2. 点击 "Add Custom Domain"
3. 输入：`boxstore.online` 和 `www.boxstore.online`
4. Render 会显示需要添加的 DNS 记录

### 6. 配置 DNS

到你的域名提供商，添加以下记录：

**主域名:**
- 类型: `CNAME`
- 主机记录: `@` 或留空
- 记录值: `isdieserver.onrender.com`（Render提供的值）

**www子域名:**
- 类型: `CNAME`
- 主机记录: `www`
- 记录值: `isdieserver.onrender.com`

⚠️ 注意：某些域名提供商不支持根域名CNAME，此时使用A记录指向Render提供的IP。

### 7. 验证部署

等待几分钟后访问：
- https://isdieserver.onrender.com/health
- https://boxstore.online/health （DNS生效后）

## 优势

✅ **自动HTTPS** - Let's Encrypt证书自动配置  
✅ **零配置** - 无需手动配置Nginx  
✅ **自动部署** - Git push后自动重新部署  
✅ **免费套餐** - 足够个人项目使用  
✅ **全球CDN** - 自动加速  

## 注意事项

- Free plan 会在15分钟无活动后休眠，首次访问可能需要几秒钟启动
- 如需保持常驻，可升级到 Starter plan ($7/月)
- 可以设置定时任务定期访问以保持活跃

## 下一步

部署完成后，你可以：
1. 在Render控制台查看日志
2. 设置自动部署（已默认开启）
3. 监控服务健康状态
4. 配置环境变量热更新
