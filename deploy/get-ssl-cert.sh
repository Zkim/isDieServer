#!/bin/bash
# SSL证书获取脚本 - 使用DNS验证

echo "===== 开始获取SSL证书（DNS验证方式） ====="
echo ""
echo "重要提示："
echo "1. certbot会显示需要添加的TXT记录"
echo "2. 请到域名提供商添加这些TXT记录"
echo "3. 等待DNS生效（3-5分钟）"
echo "4. 验证命令: dig _acme-challenge.boxstore.online TXT +short"
echo "5. 确认生效后按Enter继续"
echo ""
echo "按任意键开始..."
read

sudo certbot certonly --manual --preferred-challenges dns \
  -d boxstore.online \
  -d www.boxstore.online \
  --agree-tos \
  --email admin@boxstore.online

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ 证书获取成功！"
  echo "证书路径: /etc/letsencrypt/live/boxstore.online/"
  echo ""
  echo "下一步: 配置Nginx使用证书"
else
  echo ""
  echo "❌ 证书获取失败，请检查TXT记录是否正确"
fi
