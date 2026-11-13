# -*- coding: utf-8 -*-
# ============================================
# 练习 2：字典与列表 —— Agent 的数据语言
# 背景：你和 GPT/DeepSeek 对话时，发给 API 的每一条消息
#       就是下面这种"列表里装字典"的结构，学这个 = 学 Agent 数据格式
# ============================================

# --- 1) 列表 list：有序的一串东西，用方括号 ---
tools = ["search", "calculator", "database"]
print("Agent 拥有的工具:", tools)
print("第一个工具:", tools[0])      # 注意：程序员从 0 开始数数
tools.append("file_reader")        # 往列表末尾加一项
print("加一个工具后:", tools)

# --- 2) 字典 dict：键值对，用花括号，像一张登记表 ---
order = {
    "order_id": "20261113001",
    "customer": "王女士",
    "amount": 3599.00,
    "status": "待发货",
}
print("订单号:", order["order_id"])
print("金额:", order["amount"])

# 改字典里的值
order["status"] = "已发货"
print("发货后状态:", order["status"])

# --- 3) 列表 + 字典组合：这就是大模型 API 的消息格式 ---
# 你以后每次调用 DeepSeek/OpenAI，发的就是这个形状的数据：
messages = [
    {"role": "system", "content": "你是一个电商客服 Agent，礼貌且专业"},
    {"role": "user", "content": "我的订单什么时候发货？"},
    {"role": "assistant", "content": "您的订单 20261113001 已发货，预计 3 天送达"},
]


# 用 for 循环遍历列表，逐条打印对话
for msg in messages:
    print(f"[{msg['role']}] {msg['content']}")

# --- TODO 区域：把下面 3 行补全，让程序跑通 ---
# TODO 1: 创建一个新消息字典，role 是 "user"，content 是 "好的谢谢"
# new_msg = {...}   ← 补全右边
new_msg={"role":"user","content":"好的谢谢"}

# TODO 2: 把 new_msg 加到 messages 列表末尾（提示：用上面学过的 .append 方法）
# ...
messages.append(new_msg)

# TODO 3: 用 for 循环重新打印所有消息，确认现在是 4 条
# ...
for msg in messages:
   print(f"[{msg['role']}]{msg['content']}")
print("练习 2 完成！如果你看到了 4 条消息。")
