 # -*- coding: utf-8 -*-
# ============================================
# 练习 3：函数与类 —— 未来 Agent 代码的骨架
# 背景：LangGraph 里的"节点"是函数，工具是函数，
#       Agent 本身是一个类。看懂本文件 = 看懂 80% 的示例代码
# ============================================

# --- 1) 函数：把一段代码打包，起个名字，随时调用 ---
def greet(name):
    return f"你好 {name}，我是客服 Agent"

print(greet("王女士"))
print(greet("李先生"))     # 同一个函数，复用两次

# 带默认值的函数（以后写工具时天天用）
def query_order(order_id, status="查询中"):
    return {"order_id": order_id, "status": status}

print(query_order("A001"))                      # 不传 status → 用默认值
print(query_order("A002", status="已发货"))      # 传了 → 用传入的

# --- 2) 类：把数据（属性）和行为（方法）打包在一起 ---
class CustomerServiceAgent:
    """一个最简单的客服 Agent 骨架"""

    def __init__(self, name):
        # __init__ 在创建对象时自动执行，用来初始化
        self.name = name
        self.memory = []          # Agent 的"记忆"：一个列表

    def receive(self, message):
        # 用户发来消息 → 存进记忆 → 生成回复
        self.memory.append({"role": "user", "content": message})

        # 极简"决策逻辑"：根据关键词选择回复（真正的 Agent 会用大模型做这一步）
        if "退款" in message or "退换" in message:
            reply = "好的，已为您创建退换货工单，请提供订单号"
        elif "订单" in message or "发货" in message:
            reply = "请提供订单号，我来帮您查询物流状态"
        else:
            reply = "您好，请问有什么可以帮您？"

        self.memory.append({"role": "assistant", "content": reply})
        return reply

    def show_memory(self):
        # 打印完整对话历史 —— 和练习 2 的 messages 结构一模一样
        for msg in self.memory:
            print(f"  [{msg['role']}] {msg['content']}")


# --- 3) 使用这个类：创建对象 → 调用方法 ---
agent = CustomerServiceAgent("苏宁小助手")
print("用户:", "我想退款")
print("Agent:", agent.receive("我想退款"))
print()
print("用户:", "订单什么时候发货？")
print("Agent:", agent.receive("订单什么时候发货？"))
print()
print("--- Agent 的记忆（对话历史）---")
agent.show_memory()

# --- 4) 关键理解（读完代码后回头想 30 秒）---
# receive() 里的 if/else 就是"手写的决策"。
# 阶段 1 你要做的，就是把这段 if/else 换成调用大模型 API：
#   用户消息 → 发给大模型（附上工具列表）→ 大模型决定调哪个工具 → 返回结果
# 这个 while 循环 + 大模型决策，就是一个完整的 Agent。

print()
print("练习 3 完成！你刚刚写出了一个微型客服 Agent 骨架。")
