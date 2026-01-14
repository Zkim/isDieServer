# DNS 配置步骤

## 在域名提供商配置 DNS 记录

登录你的域名注册商（购买 boxstore.online 的平台），添加以下 DNS 记录：

### A 记录配置

| 类型 | 主机记录 | 记录值 | TTL |
|------|----------|---------|-----|
| A    | @        | 58.34.91.146 | 600 或自动 |
| A    | www      | 58.34.91.146 | 600 或自动 |

**说明:**
- `@` 代表根域名 `boxstore.online`
- `www` 代表子域名 `www.boxstore.online`
- TTL 可设为 600（10分钟）或默认值

### 验证 DNS 生效

配置完成后，等待 DNS 传播（通常 5-30 分钟），然后验证：

```bash
# 查询根域名
dig boxstore.online +short

# 查询 www 子域名
dig www.boxstore.online +short

# 或使用 nslookup
nslookup boxstore.online
nslookup www.boxstore.online
```

如果返回 `58.34.91.146`，说明 DNS 已生效。

### 常见域名提供商配置入口

- **阿里云**: 控制台 → 域名 → 解析设置
- **腾讯云**: 控制台 → 域名管理 → 解析
- **Cloudflare**: Dashboard → DNS → Records
- **GoDaddy**: My Products → Domains → DNS
- **Namecheap**: Domain List → Manage → Advanced DNS

配置完成后告诉我，我将继续配置 Nginx 和获取 SSL 证书。
