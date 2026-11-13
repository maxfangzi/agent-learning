# Day 4 任务：第一次调用大模型 API（预计 2 小时，含注册）

> 里程碑日。做完今天，你在 GitHub 上就是一个"调过 LLM API"的开发者了。
> 我们用的是 **Mistral**（法国的顶级大模型公司，你已订阅它家产品）。

## 任务 1：获取 Mistral API Key（15 分钟）

1. 打开 https://console.mistral.ai → 注册/登录（La Plateforme 开发者平台）
2. ⚠️ 注意：**Le Chat 网页订阅 ≠ API key**。网页聊天是给"用"的，API key 是给"程序调用"的，两者独立。
3. 进入「API Keys」页面 → Create new key → **立刻复制**（只显示这一次）
4. 如果平台提示需要激活计划：去「Billing/Plans」选免费的 **Experiment** 档（有免费额度，够练习用）；若要求绑卡才能开通，再告诉我，我们商量用哪家的免费额度过渡。

## 任务 2：把 Key 放进 .env 文件（10 分钟）

在本文件夹新建文件，名字就叫 `.env`（注意以点开头，没有扩展名），内容一行：

```
MISTRAL_API_KEY=粘贴你的key
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
- 状态码 403 → 账号还没开通 API 权限/计划，回任务 1 第 4 步检查
- 超时报错 → 网络波动，重跑一次
- 其他报错原文贴给 lead（**贴报错可以，贴 key 不行**）
