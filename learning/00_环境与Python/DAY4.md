# Day 4 任务：第一次调用大模型 API（预计 2 小时，含注册充值）

> 里程碑日。做完今天，你在 GitHub 上就是一个"调过 LLM API"的开发者了。

## 任务 1：注册 DeepSeek 开放平台（15 分钟）

1. 打开 https://platform.deepseek.com → 用手机号注册登录
2. 左侧「充值」→ 充 **10 元**（够你练一个月，后面学习每天成本几分钱）
3. 左侧「API keys」→ 创建 API key → **立刻复制**（只显示这一次）

## 任务 2：把 Key 放进 .env 文件（10 分钟）

在本文件夹新建文件，名字就叫 `.env`（注意以点开头，没有扩展名），内容一行：

```
DEEPSEEK_API_KEY=粘贴你的key
```

**三条安全铁律（违反任何一条都可能被盗 key 乱扣费）：**
- ❌ 绝不把 key 写进 .py 代码里
- ❌ 绝不把 key 提交到 GitHub（我们把 .env 加进了 .gitignore）
- ❌ 绝不把 key 发到任何聊天窗口——包括发给我，我不需要你的 key

## 任务 3：跑通 exercise06（40 分钟）

确保虚拟环境已激活（命令行开头有 `(.venv)`），然后：

```
python exercise06_调用大模型.py
```

看到模型回答 + token 账单 + 第二轮多轮对话 = 成功。

**重点读懂三件事（注释里都写了）：**
1. `headers={"Authorization": f"Bearer {api_key}"}` —— 身份放请求头
2. `data["choices"][0]["message"]["content"]` —— 嵌套取值，模型回复就藏在这
3. 多轮对话的真相：**服务器不记你的历史，是我们每次把完整 messages 重新发过去**——这是理解 Agent 记忆管理的第一块基石

## 任务 4：TODO + git 收尾（30 分钟）

完成 3 个 TODO（TODO 3 是挑战：写一个 while True 命令行聊天机器人，写出半成品也算完成），然后：

```
git add .
git commit -m "day4: first llm api call"
git push
```

用 `git status` 或打开 GitHub 网页确认 **.env 没有被传上去**——这是今天的隐藏考点。

## 卡住时

- 状态码 401 → key 不对（多了空格/少了字符），检查 .env
- 状态码 402 → 余额不足，确认充值成功
- 超时报错 → 网络波动，重跑一次
- 其他报错原文贴给 lead（**贴报错可以，贴 key 不行**）
