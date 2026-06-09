# 今日人品 (jrrp)

一个 AstrBot 插件，每天为每位用户计算一个确定性的人品值 (0-100)。

移植自 [koishi-plugin-jrrp](https://github.com/idlist/koishi-plugin-jrrp)，算法与彩蛋完全兼容。

## 指令

发送 `jrrp` 即可查询今日人品值。

## 实现

基于用户 ID 和当日日期通过 SHA-256 生成确定性的随机数，同一用户同一天查询结果不变。

## 安装

将本插件放入 AstrBot 的 `addons`（或插件目录）并加载。
