# -*- coding: utf-8 -*-
# ============================================
# 练习 5：HTTP 请求 —— 程序员如何和真实世界对话
# 背景：调用 DeepSeek/OpenAI API、访问数据库网关、MCP 工具通信，
#       底层全是今天学的 HTTP 请求。
# 教学重点：先检查状态码，再取数据——这是企业级 API 调用的铁律。
# ============================================

import json
import requests    # 第三方库：Python 发 HTTP 请求的事实标准（先按 DAY3.md pip install）

# --- 1) 第一个 GET 请求：一言 API（免费、无需注册、不限流）---
print("--- 1. 一言 API ---")
resp = requests.get("https://v1.hitokoto.cn/?encode=json", timeout=10)
print("HTTP 状态码:", resp.status_code)      # 200 = 成功


if resp.status_code == 200:                  # 铁律：先检查，再取数据
    data = resp.json()                       # .json() = 响应直接变字典（Day 2 的知识用上了）
    print("今日一言:", data["hitokoto"])
    print("今日一言的类型：",data["type"])
    print("出处:", data.get("from", "未知"))  # .get 的好处：键不存在也不报错，返回默认值
else:
    print(f"请求失败，状态码 {resp.status_code}")

# --- 2) 真实案例：GitHub API 查你自己的仓库 ---
print()
print("--- 2. GitHub API：你的仓库 ---")
resp = requests.get("https://api.github.com/repos/maxfangzi/agent-learning", timeout=10)

if resp.status_code == 200:
    data = resp.json()
    print("仓库名:", data["name"])
    print("创建时间:", data["created_at"][:10])
    print("star 数:", data["stargazers_count"])
else:
    # 403 = 匿名请求被限流（GitHub 每小时只允许 60 次）。等 1 小时或换网络再试
    print(f"状态码 {resp.status_code}，GitHub 说: {resp.json().get('message', '')[:80]}")
    print("（这正是企业级开发天天遇到的事：限流 rate limit。跳过本段继续）")

# --- 3) 带参数的搜索请求：看看 Agent 框架哪家火 ---
print()
print("--- 3. GitHub 搜索：agent framework 按 star 排序 ---")
search = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "llm age", "sort": "stars", "per_page": 3},  # params = URL ?后面的参数
    timeout=10,
)
if search.status_code == 200:
    results = search.json()["items"]         # 嵌套字典/列表，Day 1+2 的知识全用上了
    for i, repo in enumerate(results, start=1):
        print(f"{i}. {repo['full_name']}  ⭐{repo['stargazers_count']}")
        print(repo["html_url"])
        desc = repo["description"] or "(无描述)"
        print(f"   {desc[:60]}")
    # 把结果存成 JSON 文件（数据分析的第一步）
    with open("github_search_result.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("已存入 github_search_result.json，用 Cursor 打开看它的嵌套结构")
else:
    print(f"状态码 {search.status_code}（限流中），本段跳过——不影响你学到的知识")

# --- TODO 区域 ---
# TODO 1: 在第 1 部分后面加一行，打印一言的 "type" 字段（句子类型）
# TODO 2: 把搜索关键词 "ai agent framework" 换成 "llm agent"，重新运行看排名变化
# TODO 3: 在第 3 部分的循环里加一行，打印每个仓库的主页链接（键是 "html_url"）

print()
print("练习 5 完成！你已经会用 Python 和互联网上任何 API 对话了。")
print("阶段 1 你要做的事：把这里的 url 换成大模型 API，就正式迈入 Agent 开发。")
