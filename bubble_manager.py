import tkinter as tk
import random
from bubble_window import BubbleWindow

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