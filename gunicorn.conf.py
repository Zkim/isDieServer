# Gunicorn 配置文件
import multiprocessing

# 服务器绑定
bind = "0.0.0.0:5001"

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# 工作模式
worker_class = "sync"

# 超时时间
timeout = 120

# 日志
accesslog = "-"  # 输出到标准输出
errorlog = "-"   # 输出到标准错误
loglevel = "info"

# 进程名称
proc_name = "isDieServer"

# 守护进程（生产环境建议设为True，使用进程管理工具如supervisord）
daemon = False

# 优雅重启
graceful_timeout = 30
