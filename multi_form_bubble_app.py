import tkinter as tk
from bubble_manager import BubbleManager


class MultiFormBubbleApp:
    """多表单气泡应用主类"""

    def __init__(self, texts, colors=None, bubble_count=None, fade_out_duration=1.0, life_duration=40,
                 gradual_interval=0.5):
        """
        初始化应用
        
        Args:
            texts: 文本列表
            colors: 颜色列表
            bubble_count: 创建的气泡数量
            fade_out_duration: 淡出持续时间（秒），默认为1.0
            life_duration: 每个窗口显示的总时间（秒），从创建开始计算，默认为40秒
            gradual_interval: 每个气泡创建的间隔时间（秒），实现逐渐变多的效果
        """
        # 创建Tk根窗口
        self.root = tk.Tk()

        # 创建气泡管理器
        self.manager = BubbleManager(self.root, texts, colors, fade_out_duration, life_duration)

        # 创建气泡窗口
        self.manager.create_bubbles(bubble_count, gradual_interval)

        # 设置应用退出处理
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def run(self):
        """运行应用"""

        # 设置根窗口在所有气泡窗口关闭后自动退出，但只在第一个气泡创建后开始检测
        def check_windows():
            # 检查是否还有活跃的气泡窗口
            # 由于Toplevel窗口不计入winfo_children()，我们通过检查气泡管理器中的气泡列表
            # 或者简单地让应用运行直到所有窗口自然关闭
            if self.manager.first_bubble_created and len(self.manager.bubbles) == 0:
                self.root.destroy()
            else:
                self.root.after(500, check_windows)

        # 开始检查逻辑，但会在第一次检查时等待第一个气泡创建
        check_windows()
        self.root.mainloop()

    def _on_closing(self):
        """窗口关闭处理函数"""
        self.root.destroy()
