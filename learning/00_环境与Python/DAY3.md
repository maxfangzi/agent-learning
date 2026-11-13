# Day 3 任务：pip / 虚拟环境 / HTTP 请求（预计 2 小时）

> 今天以后，你安装任何第三方库、调用任何 API 都是同一套动作。
> **Day 4 就是调用真的大模型 API（DeepSeek），今天是它的彩排。**

## 任务 1：建虚拟环境（20 分钟）

虚拟环境 = 每个项目一个独立的"工具间"，互不污染——企业开发的标准做法。

在终端（确保 `cd` 到 00_环境与Python 文件夹）：

```
python -m venv .venv
.venv\Scripts\activate
```

- 激活成功后，命令行开头会出现 `(.venv)` 字样
- **如果 PowerShell 报"禁止运行脚本"**，先执行这条再重新激活：
  `Set-ExecutionPolicy -Scope Process RemoteSigned`

然后安装第一个第三方库：

```
pip install requests
```

## 任务 2：跑通 exercise05（40 分钟）

```
python exercise05_网络请求.py
```

你会看到：自己 GitHub 仓库的信息、GitHub 上最火的 Agent 框架排名（你的学习路线主角 LangGraph 就在里面）、以及结果被存成 JSON 文件。

## 任务 3：完成 3 个 TODO + 认识 .gitignore（30 分钟）

虚拟环境文件夹 `.venv` 有几百 MB，**不应该传上 GitHub**。在 00_环境与Python 下新建文件 `.gitignore`（没有扩展名），内容：

```
.venv/
__pycache__/
github_search_result.json
agent_memory.json
```

然后照常收尾：

```
git add .
git commit -m "day3: requests and github api"
git push
```

用 `git status` 确认 `.venv` 没有被加进去——这是你学到的第一个"工程素养"。

## 卡住时

- `ModuleNotFoundError: No module named 'requests'` → 没激活虚拟环境，或没 pip install
- 状态码 403 → GitHub 匿名请求限流，等 1 分钟再试（顺便理解什么叫 API 限流）
- 其他报错原文贴给 lead
