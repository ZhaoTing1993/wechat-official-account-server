# 基础镜像
FROM python:3.8-slim-buster

# 安装curl ping工具 (可以忽略这步)
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y curl iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY . .

# 安装所需的软件包
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 在构建镜像时，通过传递 --build-arg 标志来覆盖默认值：docker build --build-arg FLASK_DEBUG=development -t your-image-name .
ENV FLASK_APP=run.py \
    FLASK_DEBUG=false \
    PORT=5000 \
    HOST=0.0.0.0

# 对外暴露端口，可以通过-p覆盖：docker run -p 5000:5000 -e FLASK_ENV=development your-image-name
EXPOSE 5000

# 启动应用程序
CMD ["python", "run.py"]