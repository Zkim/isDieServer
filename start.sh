#!/usr/bin/env bash
set -e
# 自动激活虚拟环境并启动应用
if [ -f ".venv/bin/activate" ]; then
  # shellcheck source=/dev/null
  source .venv/bin/activate
  echo "虚拟环境已激活：$VIRTUAL_ENV"
  python app.py
else
  echo ".venv 未找到，请先创建虚拟环境并安装依赖："
  echo "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi
