# -*- coding: utf-8 -*-
# ============================================
# 练习 4：JSON 与文件读写 —— Agent 的"普通话"
# 背景：Agent 调工具、存记忆、和外部系统通信，全靠 JSON。
#       你以后配置 LangGraph、读 MCP 配置、看 API 返回，全是 JSON。
# ============================================

import json    # Python 自带的 JSON 处理模块，import = "把工具箱拿来"

# --- 1) 字典 → JSON 字符串：json.dumps（dumps = "吐出来"）---
tool_call = {
    "tool": "query_order",
    "arguments": {"order_id": "20261113001", "include_logistics": True},
}
json_str = json.dumps(tool_call, ensure_ascii=False, indent=2)
# ensure_ascii=False 让中文正常显示；indent=2 让输出带缩进、好看
print("发给工具的 JSON:")
print(json_str)

# --- 2) JSON 字符串 → 字典：json.loads（loads = "装进来"）---
# 模拟大模型 API 返回的一段 JSON
api_response = '{"reply": "您的订单已发货", "eta_days": 3, "need_human": false}'
data = json.loads(api_response)          # 变回字典，就能用字典的用法了
print()
print("模型回复:", data["reply"])
print("预计送达:", data["eta_days"], "天")
print("需要转人工:", data["need_human"])

# --- 3) 写入文件 / 从文件读取（Agent 的记忆持久化就靠这个）---
memory_file = "agent_memory.json"

# 把对话历史存进文件（"w" = write 模式，没有文件会自动创建）
history = [
    {"role": "user", "content": "我想退款"},
    {"role": "assistant", "content": "好的，请提供订单号"},
]
with open(memory_file, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=2)
# with open(...) as f 是 Python 读写文件的标准写法，缩进块结束文件自动关闭

# 再从文件读回来（"r" = read 模式）
with open(memory_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print()
print(f"从 {memory_file} 读回了 {len(loaded)} 条记忆:")
for msg in loaded:
    print(f"  [{msg['role']}] {msg['content']}")

# --- TODO 区域 ---
# TODO 1: 往 history 列表里 append 一条新消息，role="user"，content="订单号 A001"
his={"role":"user","content":"订单号 A001"}
history.append(his)
# TODO 2: 重新执行"写文件"那三行（把更新后的 history 再存一遍）
with open(memory_file, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=2)
# TODO 3: 重新从文件读回来，打印长度——确认变成了 3 条
with open(memory_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"从 {memory_file} 读回了 {len(loaded)} 条记忆:")
for msg in loaded:
    print(f"  [{msg['role']}] {msg['content']}")
# 提示：把写文件/读文件的代码各复制一份放在 TODO 区域下面改，先跑通再说

print("练习 4 完成！你现在掌握了 Agent 的三大基础数据技能：字典、JSON、文件读写。")
