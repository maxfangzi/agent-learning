# Day 2 任务：JSON 与文件读写（预计 1.5-2 小时）

> 学完本日，你就掌握了 Agent 开发 80% 的日常数据操作：
> 字典（Day 1）→ JSON（今天）→ HTTP 请求（Day 3）

## 任务 1：跑通并读懂 exercise04（45 分钟）

```
python exercise04_文件与JSON.py
```

读懂四件事：
1. `json.dumps` — 字典变 JSON 字符串（发给模型/工具时用）
2. `json.loads` — JSON 字符串变字典（收到响应时用）
3. `json.dump / json.load` — 直接和文件互转（Agent 记忆持久化的原理）
4. `with open(...) as f` — Python 读写文件的标准姿势

## 任务 2：完成文件底部的 3 个 TODO（30 分钟）

做完重新运行，确认最后打印 **3 条记忆**。
做完后 commit + push（今天开始养成习惯）：

```
git add .
git commit -m "day2: json and file io"
git push
```

## 任务 3（选做）：用 Cursor AI 辅助学习

在 Cursor 里选中 exercise04 任意一段代码，问 AI："逐行解释这段代码"。
**会用 AI 学编程是你的优势，但规则是：先自己猜意思，再问 AI 验证**——顺序反了就永远学不会。

## 卡住时

报错原文贴给 lead。最常见的错误预告：
- `JSONDecodeError` → 字符串里的引号没配对
- `FileNotFoundError` → 运行目录不对，先 `cd` 到本文件夹
- `KeyError: 'xxx'` → 字典里没有这个键，检查拼写
