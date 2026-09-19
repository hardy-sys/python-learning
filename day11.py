WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("愤怒的小鸟 - Python版")

# 颜色定义
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 游戏时钟
clock = pygame.time.Clock()
FPS = 60

# ========== 游戏参数 ==========
bird_radius = 20
bird_origin_x, bird_origin_y = 150, 450   # 小鸟初始位置（弹弓处）
bird_x, bird_y = bird_origin_x, bird_origin_y
bird_speed_x = 0
bird_speed_y = 0
is_flying = False        # 小鸟是否正在飞行
is_dragging = False      # 是否正在拖拽
drag_start_x = 0
drag_start_y = 0

pig_x, pig_y = 600, 470
pig_radius = 25
pig_alive = True

block_x, block_y = 550, 430
block_width, block_height = 40, 80
block_exists = True

ground_height = 100
gravity = 0.5            # 重力加速度
score = 0

# ========== 文字渲染函数 ==========
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# ========== 主循环 ==========
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)

    # 绘制地面
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - ground_height, WIDTH, ground_height))

    # 绘制弹弓（两条棕色线）
    pygame.draw.line(screen, BROWN, (bird_origin_x - 20, bird_origin_y + 30), (bird_origin_x, bird_origin_y), 5)
    pygame.draw.line(screen, BROWN, (bird_origin_x + 20, bird_origin_y + 30), (bird_origin_x, bird_origin_y), 5)

    # 绘制障碍物
    if block_exists:
        pygame.draw.rect(screen, GRAY, (block_x, block_y, block_width, block_height))

    # 绘制小猪
    if pig_alive:
        pygame.draw.circle(screen, YELLOW, (int(pig_x), int(pig_y)), pig_radius)
        pygame.draw.circle(screen, BLACK, (int(pig_x - 8), int(pig_y - 5)), 4)  # 左眼
        pygame.draw.circle(screen, BLACK, (int(pig_x + 8), int(pig_y - 5)), 4)  # 右眼

    # 绘制小鸟
    pygame.draw.circle(screen, RED, (int(bird_x), int(bird_y)), bird_radius)
    # 小鸟眼睛
    pygame.draw.circle(screen, WHITE, (int(bird_x + 6), int(bird_y - 6)), 6)
    pygame.draw.circle(screen, BLACK, (int(bird_x + 8), int(bird_y - 6)), 3)
    # 小鸟嘴巴
    pygame.draw.polygon(screen, YELLOW, [
        (int(bird_x + 15), int(bird_y)),
        (int(bird_x + 28), int(bird_y + 3)),
        (int(bird_x + 15), int(bird_y + 6))
    ])

    # 绘制分数
    draw_text(f"Score: {score}", 36, BLACK, 10, 10)
    draw_text("拖拽小鸟发射，消灭小猪！", 28, BLACK, 10, 50)

    # ========== 事件处理 ==========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 鼠标按下 - 开始拖拽
        if event.type == pygame.MOUSEBUTTONDOWN and not is_flying:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = math.hypot(mouse_x - bird_x, mouse_y - bird_y)
            if distance <= bird_radius:
                is_dragging = True
                drag_start_x, drag_start_y = mouse_x, mouse_y

        # 鼠标松开 - 发射
        if event.type == pygame.MOUSEBUTTONUP and is_dragging:
            is_dragging = False
            is_flying = True
            # 根据拖拽距离计算发射速度
            offset_x = drag_start_x - bird_origin_x
            offset_y = drag_start_y - bird_origin_y
            bird_speed_x = offset_x * 0.15
            bird_speed_y = offset_y * 0.15

    # ========== 拖拽逻辑 ==========
    if is_dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # 限制拖拽范围
        max_drag = 100
        dist = math.hypot(mouse_x - bird_origin_x, mouse_y - bird_origin_y)
        if dist > max_drag:
            angle = math.atan2(mouse_y - bird_origin_y, mouse_x - bird_origin_x)
            mouse_x = bird_origin_x + max_drag * math.cos(angle)
            mouse_y = bird_origin_y + max_drag * math.sin(angle)
        bird_x, bird_y = mouse_x, mouse_y

    # ========== 飞行物理逻辑 ==========
    if is_flying:
        bird_speed_y += gravity       # 重力作用
        bird_x += bird_speed_x
        bird_y += bird_speed_y

        # 小鸟与障碍物碰撞
        if block_exists:
            if (bird_x + bird_radius > block_x and bird_x - bird_radius < block_x + block_width and
                    bird_y + bird_radius > block_y and bird_y - bird_radius < block_y + block_height):
                block_exists = False
                bird_speed_x *= 0.5    # 撞击后减速

        # 小鸟与小猪碰撞（圆心距离判定）
        if pig_alive:
            distance = math.hypot(bird_x - pig_x, bird_y - pig_y)
            if distance < bird_radius + pig_radius:
                pig_alive = False
                score += 100

        # 边界判定 - 落地或飞出屏幕则重置
        if (bird_y >= HEIGHT - ground_height - bird_radius or
                bird_x > WIDTH + 50 or bird_x < -50):
            bird_x, bird_y = bird_origin_x, bird_origin_y
            bird_speed_x = 0
            bird_speed_y = 0
            is_flying = False

    # ========== 游戏状态判定 ==========
    if not pig_alive:
        draw_text("恭喜通关！", 80, BLACK, 230, 180)
        draw_text(f"最终得分: {score}", 50, BLACK, 260, 280)
        draw_text("点击关闭窗口退出", 36, BLACK, 250, 350)

    pygame.display.flip()

pygame.quit()
sys.exit()
