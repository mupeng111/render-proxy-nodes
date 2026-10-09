FROM ghcr.io/sagernet/sing-box:latest
USER root
RUN apk add --no-cache python3
COPY entrypoint.py /entrypoint.py
EXPOSE 10000
ENTRYPOINT ["python3", "/entrypoint.py"]
