# 多表单气泡应用

## 项目简介

这是一个基于Python Tkinter开发的多表单气泡应用程序，能够在屏幕上生成多个带有淡入淡出效果的气泡窗口。每个气泡窗口会随机显示一条浪漫的情话，并在显示一段时间后自动消失。

## 功能特点

- 💬 随机文本显示：每个气泡会随机显示一条预设的浪漫情话
- 🎨 美观的视觉效果：支持自定义颜色和随机颜色生成
- 🌟 平滑的淡入淡出动画：气泡窗口具有优雅的出现和消失效果
- ⏱️ 自动生命周期管理：每个气泡窗口会在指定时间后自动淡出消失
- 🔄 渐进式创建：气泡窗口会按照设定的时间间隔逐个创建，形成逐渐变多的效果

## 技术实现

- 使用Python Tkinter库创建图形界面
- 采用面向对象设计，包含以下主要类：
  - `BubbleWindow`: 负责单个气泡窗口的创建和动画效果
  - `BubbleManager`: 管理多个气泡窗口的创建和生命周期
  - `MultiFormBubbleApp`: 应用程序主类，协调各组件工作
- 实现了自定义的淡入淡出动画效果
- 通过定时器控制气泡窗口的生命周期

## 使用方法

### 环境要求

- Python 3.x
- Tkinter库（通常随Python一起安装）

### 运行程序

1. 确保已安装Python环境
2. 下载或克隆本项目到本地
3. 确保所有Python文件都在同一目录下
4. 在项目目录下执行以下命令：

```bash
python main.py
```

### 自定义设置

你可以通过修改`main.py`文件中的参数来自定义应用程序的行为：

- `bubble_count`: 设置要创建的气泡窗口数量
- `fade_out_duration`: 设置气泡淡出动画的持续时间（秒）
- `life_duration`: 设置每个气泡窗口显示的总时间（秒）
- `gradual_interval`: 设置气泡窗口创建的时间间隔（秒）
- `default_texts`: 自定义气泡中显示的文本内容
- `default_colors`: 自定义气泡的背景颜色

## 项目结构

```
muliti_form_bubble/
├── main.py                   # 主程序文件（入口点）
├── bubble_window.py          # 包含BubbleWindow类
├── bubble_manager.py         # 包含BubbleManager类
├── multi_form_bubble_app.py  # 包含MultiFormBubbleApp类
├── README.md                 # 项目说明文档（英文）
├── README_cn.md              # 项目说明文档（中文）
├── LICENSE                   # MIT许可证文件
└── .gitignore                # Git忽略文件
```

## 许可证

本项目采用MIT许可证 - 详情请查看[LICENSE](LICENSE)文件。

## 示例效果

运行程序后，屏幕上会逐渐出现多个气泡窗口。每个气泡窗口会显示一条随机的浪漫情话，并在40秒后自动淡出消失。随着新气泡的不断创建和旧气泡的消失，视觉效果保持动态和生动。

## 许可证

本项目采用MIT许可证。

## 致谢

- 感谢Python和Tkinter提供的强大功能
- 感谢所有使用和支持本项目的用户