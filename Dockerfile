FROM python:3.13-alpine

# 设置工作目录
WORKDIR /app

# 安装系统依赖（alpine使用apk）
RUN apk add --no-cache gcc musl-dev

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 创建日志目录
RUN mkdir -p logs

# 暴露端口
EXPOSE 5001

# 使用Gunicorn运行应用
CMD ["gunicorn", "app:app", "-c", "gunicorn.conf.py"]
