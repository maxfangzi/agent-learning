# 阶段 0 · 第 1 天：环境验证 + Python 三个练习

## 今日目标（预计 2-3 小时）

1. ✅ 环境已验证：Python 3.13.12 / Git 2.53 / Cursor 均已安装（我已帮你检查过）
2. ⬜ 你自己打开终端，跑通三个练习
3. ⬜ 注册 GitHub 账号（如还没有），把本目录传上去——完成你人生第一个 git push

## 任务清单（逐条做，做完打勾）

### 任务 1：打开终端（2 分钟）
- 在 Cursor 里：顶部菜单 Terminal → New Terminal（或按 `Ctrl + ~`）
- 输入以下命令确认能进入本目录：
```
cd "D:\dsh做agent的工作区\agent demo\learning\00_环境与Python"
```

### 任务 2：跑通第一个程序（10 分钟）
```
python exercise01_hello.py
```
- 看到 3 行输出 = 成功
- 然后用 Cursor 打开这个文件，逐行读代码里的中文注释，改 2 处再跑一次（注释里告诉你改哪里）

### 任务 3：数据结构练习（30 分钟）
```
python exercise02_数据结构.py
```
- 这个练习教你**字典和列表**——Agent 开发里 90% 的数据都是这两种结构
- 按文件里的 TODO 提示自己补 3 行代码，补错了会报错，读报错信息再改（读报错是程序员的日常）

### 任务 4：函数与类练习（45 分钟）
```
python exercise03_函数与类.py
```
- 函数和类是后面所有 Agent 代码的骨架，看懂这个文件 = 看懂未来 80% 的示例代码

### 任务 5：Git 第一步（30 分钟）
```
git init
git add .
git commit -m "my first python exercises"
```
- 然后去 https://github.com 注册/登录 → 右上角 + → New repository → 名字填 `agent-learning` → 不要勾选任何初始化选项 → Create
- 回到终端（把 yourname 换成你的 GitHub 用户名）：
```
git branch -M main
git remote add origin https://github.com/yourname/agent-learning.git
git push -u origin main
```
- 浏览器打开你的仓库地址，能看到 4 个文件 = 你已经把手写代码发布到全球最大代码平台了

## 卡住了怎么办

把终端里的红色报错原文复制给我，**报错不是失败，是练习的一部分**——读报错、改、再跑，这个循环就是你未来每天的工作内容。
