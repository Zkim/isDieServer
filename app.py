from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 配置CORS（跨域支持）
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 配置日志
if not app.debug:
    # 创建日志目录
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    # 文件日志处理器
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=10240000,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('isDieServer 启动')

# 初始化 Supabase 客户端
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 根路由
@app.route('/')
def home():
    return jsonify({
        'message': '欢迎使用简单服务!',
        'status': 'success'
    })

# GET 请求示例
@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name', '访客')
    return jsonify({
        'message': f'你好, {name}!',
        'status': 'success'
    })

# POST 请求示例
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({
        'message': '数据接收成功',
        'received_data': data,
        'status': 'success'
    }), 201

# 健康检查
@app.route('/health')
def health():
    supabase_status = 'connected' if supabase else 'not configured'
    return jsonify({
        'status': 'healthy',
        'supabase': supabase_status
    })

# Supabase 数据查询示例
@app.route('/api/data/<table_name>', methods=['GET'])
def get_data(table_name):
    if not supabase:
        return jsonify({'error': 'Supabase 未配置'}), 500
    
    try:
        response = supabase.table(table_name).select("*").execute()
        return jsonify({
            'status': 'success',
            'data': response.data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Supabase 插入数据示例
@app.route('/api/data/<table_name>', methods=['POST'])
def insert_data(table_name):
    if not supabase:
        return jsonify({'error': 'Supabase 未配置'}), 500
    
    try:
        data = request.get_json()
        response = supabase.table(table_name).insert(data).execute()
        return jsonify({
            'status': 'success',
            'data': response.data
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Supabase 更新数据示例
@app.route('/api/data/<table_name>/<int:id>', methods=['PUT'])
def update_data(table_name, id):
    if not supabase:
        return jsonify({'error': 'Supabase 未配置'}), 500
    
    try:
        data = request.get_json()
        response = supabase.table(table_name).update(data).eq('id', id).execute()
        return jsonify({
            'status': 'success',
            'data': response.data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Supabase 删除数据示例
@app.route('/api/data/<table_name>/<int:id>', methods=['DELETE'])
def delete_data(table_name, id):
    if not supabase:
        return jsonify({'error': 'Supabase 未配置'}), 500
    
    try:
        response = supabase.table(table_name).delete().eq('id', id).execute()
        return jsonify({
            'status': 'success',
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # 开发环境使用Flask内置服务器
    # 生产环境请使用: gunicorn app:app -c gunicorn.conf.py
    app.run(host='0.0.0.0', port=5001, debug=True)
