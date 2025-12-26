# 构建阶段：安装依赖
FROM python:3.8-slim AS builder
WORKDIR /app
COPY requirements.txt .
# 安装依赖到本地目录
RUN pip install --no-cache-dir -r requirements.txt -t ./deps

# 运行阶段：仅复制必要文件，减小镜像体积
FROM python:3.8-slim
WORKDIR /app
# 从构建阶段复制依赖和应用代码
COPY --from=builder /app/deps ./deps
COPY clean_log.py .
# 添加依赖到Python路径
ENV PYTHONPATH=/app/deps
# 容器启动命令
CMD ["python", "clean_log.py"]