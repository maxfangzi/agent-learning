# -*- coding: utf-8 -*-
# ============================================
# 练习 1：你的第一个 Python 程序
# 目标：跑通它 → 读懂它 → 改动它
# ============================================

# 1) print 是"往屏幕上输出"的命令，字符串要放在引号里
print("Hello, Agent World!")

# 2) 变量：给一个值起个名字，后面可以反复使用
name = "max"          # TODO 改动点 1：把引号里的内容换成你想要的英文名或昵称
print(f"我叫 {name}，我的目标是 6 个月做出企业级 Agent")   # f 开头的字符串可以把变量嵌进去

# 3) 数字可以做数学运算
weeks = 26             # 6 个月 ≈ 26 周
hours_per_week = 25
total_hours = weeks * hours_per_week
print(f"未来 {weeks} 周，我计划投入 {total_hours} 小时学习")   # TODO 改动点 2：把 13 改成你真实的每周小时数

# 4) if 判断：条件成立才执行
total_hours = weeks * hours_per_week
if total_hours >= 300:
    print("投入超过 300 小时，足够完成企业级项目")
else:
    print("时间偏少，考虑提高每周投入")
