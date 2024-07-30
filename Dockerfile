# 使用官方Python基础镜像（slim），减少镜像体积
FROM python:3.9.6-slim
# 设置作者信息
LABEL authors="zhangyp"

# 开放端口
EXPOSE 8088

# 避免生成.pyc文件
ENV PYTHONDONTWRITEBYTECODE=1

# 关闭输出缓冲，方便日志记录
ENV PYTHONUNBUFFERED=1

# 设置时区
ENV TZ=Asia/Shanghai

# 设置工作目录
WORKDIR /ewordaqiq

# 复制程序相关文件
COPY requirements.txt /ewordaqiq/
COPY . /ewordaqiq

# 使用阿里云镜像加速依赖下载，同时确保安装过程的错误能被捕获
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && echo "Dependencies installed successfully."

# 指定容器启动时的命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8088"]