import tkinter as tk
import random
import sys
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
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def _get_contrast_text_color(self):
        """根据背景颜色确定文本颜色（黑色或白色）以保证可读性"""
        # 将十六进制颜色转换为RGB
        rgb = tuple(int(self.bg_color[1:][i:i+2], 16) for i in (0, 2, 4))
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

class BubbleManager:
    """气泡管理器，负责管理多个气泡窗口的创建和显示"""
    
    def __init__(self, root, texts, colors=None, fade_out_duration=1.0, life_duration=40):
        """
        初始化气泡管理器
        
        Args:
            root: 根窗口
            texts: 文本列表
            colors: 颜色列表，如果为None或空则随机生成颜色
            fade_out_duration: 淡出持续时间（秒），默认为1.0
            life_duration: 每个窗口显示的总时间（秒），从创建开始计算
        """
        self.root = root
        self.texts = texts
        self.colors = colors if colors and len(colors) > 0 else None
        self.fade_out_duration = fade_out_duration
        self.life_duration = life_duration
        
        # 存储创建的气泡窗口引用
        self.bubbles = []
        
        # 标记第一个气泡是否已创建
        self.first_bubble_created = False
        
        # 隐藏主窗口
        self.root.withdraw()
    
    def create_bubbles(self, count=None, gradual_interval=0.5):
        """
        按顺序逐渐创建气泡窗口
        
        Args:
            count: 创建的气泡数量，如果为None则使用文本列表的长度
            gradual_interval: 每个气泡创建的间隔时间（秒）
        """
        # 如果没有指定数量，则默认为10个
        if count is None:
            count = 10
        
        # 按顺序创建气泡窗口
        for i in range(count):
            # 计算延迟时间，实现逐渐变多的效果
            delay = int(i * gradual_interval * 1000)
            
            # 使用lambda函数创建气泡，每个气泡使用随机文本和颜色
            self.root.after(delay, self._create_single_bubble)
    
    def _create_single_bubble(self):
        """
        创建单个气泡窗口，随机选择文本和颜色
        """
        # 随机选择文本
        if self.texts:
            text_idx = random.randint(0, len(self.texts) - 1)
            text = self.texts[text_idx]
        else:
            text = "默认文本"
        
        # 随机选择颜色
        if self.colors:
            color_idx = random.randint(0, len(self.colors) - 1)
            color = self.colors[color_idx]
        else:
            color = None  # 将使用随机颜色
        
        # 创建气泡窗口并保存引用
        bubble = BubbleWindow(self.root, text, color, self.fade_out_duration, self.life_duration)
        self.bubbles.append(bubble)
        
        # 将气泡管理器引用添加到气泡对象中，以便在销毁时能移除自身
        if not hasattr(bubble, '_managers'):
            bubble._managers = []
        bubble._managers.append(self)
        
        # 如果是第一个创建的气泡，设置标志
        if not self.first_bubble_created:
            self.first_bubble_created = True

class MultiFormBubbleApp:
    """多表单气泡应用主类"""
    
    def __init__(self, texts, colors=None, bubble_count=None, fade_out_duration=1.0, life_duration=40, gradual_interval=0.5):
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

def main():
    """主函数"""
    # 预定义的文本列表
    default_texts = [
        "你是我生命中的阳光",
        "想你在每一个瞬间",
        "爱你到地老天荒",
        "有你的日子最美好",
        "你是我的唯一",
        "心之所向，爱之所往",
        "余生请多指教",
        "遇见你，是最好的安排",
        "我的眼里只有你",
        "爱是永恒的主题",
        "一想到你，嘴角就扬起",
        "与你共度，便是晴天",
        "深情不及久伴",
        "你在，我便心安",
        "爱情里最美好的事就是有你",
        "你的笑容是我的幸福",
        "世界很大，只爱一个你",
        "执子之手，与子偕老",
        "每一天都比昨天更爱你",
        "你是我藏在心里的甜"
    ]
    
    # 预定义的颜色列表
    default_colors = [
        "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4",
        "#FECA57", "#FF9FF3", "#54A0FF", "#5F27CD",
        "#00D2D3", "#FF9F43"
    ]
    
    # 创建并运行应用
    app = MultiFormBubbleApp(
        texts=default_texts,
        colors=default_colors,  # 可以设置为None来测试随机颜色
        bubble_count=1000,  # 创建bubble_count个气泡窗口
        fade_out_duration=3.0,  # 设置淡出动画持续时间为fade_out_duration秒
        life_duration=40,  # 设置每个窗口显示life_duration秒后淡出
        gradual_interval=0.15  # 每个气泡间隔gradual_interval秒创建，实现逐渐变多的效果
    )
    app.run()

if __name__ == "__main__":
    main()