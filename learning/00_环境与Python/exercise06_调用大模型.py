# -*- coding: utf-8 -*-
# ============================================
# 练习 6：第一次调用大模型 API —— 里程碑日
# 背景：今天之前，"Agent"对你还是一个词；今天之后，
#       你亲手调过 LLM API，正式迈入 AI 应用开发。
# 说明：我们故意不用任何 SDK，就用 Day 3 学的 requests——
#       这样你能看清大模型 API 的本质：一次带 JSON 的 HTTP 请求。
# 安全铁律：API Key 只存在 .env 文件里，绝不写进代码、
#           绝不提交到 GitHub、绝不发到任何聊天窗口（包括发给我）。
# ============================================

import json
import requests

# --- 0) 从 .env 文件读取 API Key（Key 绝不出现在代码里）---
api_key = None
try:
    with open(".env", encoding="utf-8") as f:
        for line in f:
            if line.startswith("MISTRAL_API_KEY="):
                api_key = line.split("=", 1)[1].strip()
except FileNotFoundError:
    pass  # 没有 .env 文件时走下面的友好提示

if not api_key or "在这里" in api_key:
    print("还没配置 Key！请按 DAY4.md 步骤：")
    print('1. 在本文件夹新建文件 .env')
    print("2. 文件内容写一行： MISTRAL_API_KEY=你的真实key")
    raise SystemExit(0)   # 缺钥匙就体面退出，不崩

# --- 1) 组装请求：Day 1 学的 messages 格式派上用场了 ---
messages = [
    {"role": "system", "content": "你是一个简洁、专业的AI助手，回答不超过三句话"},
    {"role": "user", "content": "用一句话解释：什么是 AI Agent？"},
]

print("正在调用 Mistral API ...")
resp = requests.post(
    "https://api.mistral.ai/v1/chat/completions",      # Mistral 的对话接口（OpenAI 兼容格式）
    headers={"Authorization": f"Bearer {api_key}"},    # 身份凭证放请求头，不放 URL
    json={                                             # json= 参数会自动转成 JSON 并设好头
        "model": "mistral-small-latest",               # 便宜够用；换 "mistral-large-latest" 更强
        "messages": messages,
        "temperature": 0.7,                            # 0-2，越大越随机
    },
    timeout=60,
)

# --- 2) 铁律依旧：先查状态码，再取数据 ---
if resp.status_code != 200:
    print(f"调用失败，状态码 {resp.status_code}")
    print("API 的报错说明:", resp.text[:300])
    print("常见原因：key 写错(401) / 没开通付费或免费额度(403) / 网络问题")
    raise SystemExit(0)

data = resp.json()
reply = data["choices"][0]["message"]["content"]       # 嵌套取值：choices列表→第0个→message→content
print()
print("模型回复:", reply)

# --- 3) 看"账单"：每次调用花了多少 token（=多少钱）---
usage = data["usage"]
print()
print(f"本次消耗: 输入 {usage['prompt_tokens']} tokens + 输出 {usage['completion_tokens']} tokens")
print(f"Mistral 定价见 console.mistral.ai → Pricing，这次调用通常不到 1 分钱")

# --- 4) 多轮对话：把模型的回答接回 messages（Day 1 练习 2 的结构）---
messages.append({"role": "assistant", "content": reply})
messages.append({"role": "user", "content": "那它和我们平时用的聊天机器人有什么区别？同样一句话概括"})

resp2 = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"model": "mistral-small-latest", "messages": messages, "temperature": 0.7},
    timeout=60,
)
print()
print("第二轮回答:", resp2.json()["choices"][0]["message"]["content"])
print()
print("注意：第二轮模型'记得'上一轮——不是因为服务器存了你的会话，")
print("而是我们把完整历史重新发了一遍。这个理解对做 Agent 至关重要。")

# --- TODO 区域 ---
# TODO 1: 把 system 内容换成客服人设："你是电商客服小苏，礼貌专业，只回答售后问题"，
#         user 消息换成"我的订单三天了还没发货"，重新运行看回答变化
# TODO 2: 加一行打印 resp2.json()["usage"]，看完整账单结构（用 Cursor 看这个 JSON 有哪些键）
# TODO 3（挑战）: 把两次调用改成 while True 循环，做一个命令行多轮聊天：
#         input() 等用户输入 → append 到 messages → 调 API → 打印回复
#         输入 q 退出。写出来你就拥有了自己的 ChatGPT 雏形！
#         卡住了把你的半成品发我看，写不出来也不影响明天继续。

print()
print("练习 6 完成！你已经是调过大模型 API 的开发者了。")
