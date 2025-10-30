from multi_form_bubble_app import MultiFormBubbleApp

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