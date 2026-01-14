# 简单的Python服务

一个基于Flask和Supabase的简单HTTP服务器，支持开发和生产环境部署。

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置 Supabase

1. 复制 `.env.example` 为 `.env`:
```bash
cp .env.example .env
```

2. 在 `.env` 文件中填入你的 Supabase 凭证:
```
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_anon_key_here
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

### 运行服务

**推荐（使用项目虚拟环境）:**
```bash
# 第一次：创建并安装依赖
make venv

# 启动（两种方式任选其一）
./start.sh
# 或
make run
```

**直接开发（已激活虚拟环境时）:**
```bash
python app.py
```

**生产环境:**
```bash
gunicorn app:app -c gunicorn.conf.py
```

**Docker 部署:**
```bash
docker compose up -d
```

服务将在 `http://localhost:5001` 上运行。

## API端点

### 基础端点
- `GET /` - 欢迎页面
- `GET /api/hello?name=yourname` - 问候接口
- `POST /api/data` - 接收JSON数据
- `GET /health` - 健康检查

### Supabase 数据库操作
- `GET /api/data/<table_name>` - 查询表中所有数据
- `POST /api/data/<table_name>` - 插入新数据
- `PUT /api/data/<table_name>/<id>` - 更新指定ID的数据
- `DELETE /api/data/<table_name>/<id>` - 删除指定ID的数据

## 生产环境部署

详细的部署说明请查看 [DEPLOYMENT.md](DEPLOYMENT.md)

### 主要特性

✅ **生产级 WSGI 服务器** - 使用 Gunicorn 替代 Flask 开发服务器  
✅ **CORS 跨域支持** - 支持前端应用调用  
✅ **日志系统** - 自动记录应用日志到文件  
✅ **环境配置分离** - 开发/生产环境独立配置  
✅ **Docker 支持** - 容器化部署  
✅ **Supabase 集成** - 完整的 CRUD 操作支持  

## 项目结构

```
isDieServer/
├── app.py                 # 主应用文件
├── config.py              # 配置管理
├── gunicorn.conf.py       # Gunicorn 配置
├── requirements.txt       # Python 依赖
├── Dockerfile            # Docker 配置
├── docker-compose.yml    # Docker Compose 配置
├── compose.yaml          # Docker Compose (plugin) 配置（与 docker-compose.yml 相同）
├── Procfile              # 云平台部署配置
├── .env.example          # 环境变量示例
├── .gitignore           # Git 忽略文件
├── README.md            # 项目说明
└── DEPLOYMENT.md        # 部署指南
```

## 示例请求

### GET 请求
```bash
curl http://localhost:5001/api/hello?name=张三
```

### Supabase 查询数据
```bash
curl http://localhost:5001/api/data/users
```

### Supabase 插入数据
```bash
curl -X POST http://localhost:5001/api/data/users \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "email": "zhangsan@example.com"}'
```

### Supabase 更新数据
```bash
curl -X PUT http://localhost:5001/api/data/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "李四"}'
```

### Supabase 删除数据
```bash
curl -X DELETE http://localhost:5001/api/data/users/1
```

## 许可证

MIT
