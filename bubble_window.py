import tkinter as tk
from tkinter import font
import time

class BubbleWindow:
    """气泡窗口类，负责创建和管理单个淡出窗口"""
    
    def __init__(self, parent, text, bg_color=None, fade_out_duration=1.0, life_duration=40):
        """
        初始化气泡窗口
        
        Args:
            parent: 父窗口
            text: 显示的文本内容
            bg_color: 背景颜色，如果为None则随机生成
            fade_out_duration: 淡出持续时间（秒），默认为1.0
            life_duration: 窗口显示的总时间（秒），从创建开始计算
        """
        self.parent = parent
        self.text = text
        self.bg_color = bg_color if bg_color else self._generate_random_color()
        
        # 创建顶层窗口
        self.window = tk.Toplevel(parent)
        self.window.overrideredirect(True)  # 无边框窗口
        self.window.attributes('-alpha', 0)  # 初始透明度为0
        self.window.attributes('-topmost', True)  # 窗口置顶
        self.window.configure(bg=self.bg_color)  # 设置窗口背景色
        
        # 获取屏幕尺寸
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        
        # 创建标签显示文本
        self.label = tk.Label(
            self.window, 
            text=self.text, 
            bg=self.bg_color, 
            fg=self._get_contrast_text_color(),
            font=font.Font(family='SimHei', size=12)
        )
        self.label.pack(padx=20, pady=10)
        
        # 更新窗口以获取其大小
        self.window.update_idletasks()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        
        # 随机位置，确保窗口完全显示在屏幕内
        import random
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)
        
        # 设置窗口位置
        self.window.geometry(f"+{x}+{y}")
        
        # 淡入淡出动画参数
        self.alpha = 0
        self.fade_direction = 1  # 1为淡入，-1为淡出
        self.fade_speed = 0.02
        self.fade_in_duration = 1.0  # 淡入持续时间（秒）
        self.fade_out_duration = fade_out_duration  # 淡出持续时间（秒）
        self.life_duration = life_duration  # 窗口显示的总时间
        
        # 记录窗口创建时间
        self.creation_time = time.time()
        
        # 开始动画
        self._start_animation()
        
        # 设置定时器，在life_duration秒后开始淡出
        self.window.after(int(life_duration * 1000), self._fade_out)
    
    def force_fade_out(self):
        """强制窗口开始淡出"""
        self._fade_out()
    
    def _generate_random_color(self):
        """生成随机颜色"""
        import random
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def _get_contrast_text_color(self):
        """根据背景颜色确定文本颜色（黑色或白色）以保证可读性"""
        # 将十六进制颜色转换为RGB
        rgb = tuple[int, ...](int(self.bg_color[1:][i:i+2], 16) for i in (0, 2, 4))
        # 计算亮度（使用相对亮度公式）
        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255
        # 亮度大于0.5使用黑色文本，否则使用白色文本
        return 'black' if luminance > 0.5 else 'white'
    
    def _start_animation(self):
        """开始淡入淡出动画"""
        self._fade_in()
    
    def _fade_in(self):
        """淡入效果"""
        if self.alpha < 1:
            self.alpha += self.fade_speed
            self.window.attributes('-alpha', min(self.alpha, 1))
            # 计算淡入动画的速度，使其在指定时间内完成
            frames_needed = int(self.fade_in_duration / self.fade_speed)
            delay = int(self.fade_in_duration * 1000 / frames_needed)
            self.window.after(delay, self._fade_in)
        else:
            # 淡入完成后，不自动开始淡出，等待外部控制
            pass
    
    def _fade_out(self):
        """淡出效果"""
        if self.alpha > 0:
            self.alpha -= self.fade_speed
            self.window.attributes('-alpha', max(self.alpha, 0))
            # 计算淡出动画的速度，使其在指定时间内完成
            frames_needed = int(self.fade_out_duration / self.fade_speed)
            delay = int(self.fade_out_duration * 1000 / frames_needed)
            self.window.after(delay, self._fade_out)
        else:
            # 淡出完成后销毁窗口
            # 从气泡管理器中移除自身
            for manager in getattr(self, '_managers', []):
                if self in manager.bubbles:
                    manager.bubbles.remove(self)
            self.window.destroy()