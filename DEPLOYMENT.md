# 部署指南

## 本地开发

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的配置
```

### 3. 运行开发服务器
```bash
python app.py
```

---

## 生产环境部署

### 方式一：直接使用 Gunicorn

#### 1. 配置环境变量
```bash
export FLASK_ENV=production
export SUPABASE_URL=your_url
export SUPABASE_KEY=your_key
export SECRET_KEY=your_secret_key
```

#### 2. 启动服务
```bash
gunicorn app:app -c gunicorn.conf.py
```

#### 3. 使用 systemd 管理服务（推荐）

创建文件 `/etc/systemd/system/isDieServer.service`:
```ini
[Unit]
Description=isDieServer
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/isDieServer
Environment="PATH=/path/to/isDieServer/.venv/bin"
EnvironmentFile=/path/to/isDieServer/.env
ExecStart=/path/to/isDieServer/.venv/bin/gunicorn app:app -c gunicorn.conf.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启用并启动服务:
```bash
sudo systemctl enable isDieServer
sudo systemctl start isDieServer
sudo systemctl status isDieServer
```

---

### 方式二：使用 Docker

#### 1. 构建镜像
```bash
docker build -t isdie-server .
```

#### 2. 运行容器
```bash
docker run -d \
  -p 5001:5001 \
  --env-file .env \
  --name isdie-server \
  isdie-server
```

#### 3. 使用 Docker Compose（推荐）
```bash
docker compose up -d
```

查看日志:
```bash
docker compose logs -f
```

停止服务:
```bash
docker compose down
```

---

### 方式三：云平台部署

#### Heroku
```bash
# 登录 Heroku
heroku login

# 创建应用
heroku create your-app-name

# 设置环境变量
heroku config:set SUPABASE_URL=your_url
heroku config:set SUPABASE_KEY=your_key
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your_secret_key

# 部署
git push heroku main
```

#### Railway
1. 连接 GitHub 仓库
2. 在 Railway 控制台设置环境变量
3. 自动部署

#### Render
1. 连接 GitHub 仓库
2. 选择 Web Service
3. 构建命令: `pip install -r requirements.txt`
4. 启动命令: `gunicorn app:app -c gunicorn.conf.py`
5. 设置环境变量

---

## Nginx 反向代理配置（可选）

如果需要使用 Nginx 作为反向代理:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

配置 HTTPS (使用 Let's Encrypt):
```bash
sudo certbot --nginx -d your-domain.com
```

---

## 性能优化建议

1. **使用 CDN** - 缓存静态资源
2. **数据库连接池** - 优化数据库连接
3. **缓存** - 使用 Redis 缓存频繁查询的数据
4. **负载均衡** - 多实例部署
5. **监控** - 使用 Sentry 或 Datadog 监控错误和性能

---

## 安全检查清单

- [ ] 设置强密码的 SECRET_KEY
- [ ] 生产环境关闭 DEBUG 模式
- [ ] 配置 HTTPS
- [ ] 限制 CORS 允许的域名
- [ ] 使用环境变量管理敏感信息
- [ ] 定期更新依赖包
- [ ] 配置防火墙规则
- [ ] 设置速率限制（可使用 Flask-Limiter）
