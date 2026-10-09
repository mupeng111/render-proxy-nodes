import os, json
port = int(os.getenv("PORT", "10000"))
cfg = {
  "log": {"level": "info"},
  "inbounds": [{
    "type": "vless", "tag": "vless-ws", "listen": "::", "listen_port": port,
    "users": [{"uuid": os.environ["UUID"]}],
    "transport": {"type": "ws", "path": os.getenv("WS_PATH", "/ws")}
  }],
  "outbounds": [{"type": "direct"}]
}
open("/tmp/config.json","w").write(json.dumps(cfg))
print(f"sing-box WS on :{port}", flush=True)
os.execvp("sing-box", ["sing-box", "run", "-c", "/tmp/config.json"])
