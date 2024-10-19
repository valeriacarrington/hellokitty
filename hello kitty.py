import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анімована картинка")

# Завантаження зображення
try:
    anime_image = pygame.image.load('C:/Users/Valeria/Downloads/hello kitty purple.jpg')
except pygame.error as e:
    print(f"Cannot load image: {e}")
    pygame.quit()
    exit()

# Змінюємо розмір зображення на 400x400 пікселів
anime_image = pygame.transform.scale(anime_image, (400, 400))

# Налаштування початкової позиції та швидкості руху
image_pos = [WIDTH // 2, HEIGHT // 2]
speed = 2
angle = 0  # Змінна для обертання

# Дозволені кольори фону
background_colors = [
    (64, 0, 64),    # Дуже темний фіолетовий
    (128, 0, 128),  # Темний фіолетовий
    (192, 0, 255),  # Яскравий фіолетовий
    (255, 192, 203),  # Рожевий
    (0, 0, 0),      # Чорний
    (255, 255, 255),  # Білий
    (255, 0, 0),    # Червоний
    (0, 0, 255)     # Синій
]

# Функція для зміни кольору фону
def change_background_color():
    return random.choice(background_colors)

# Головний цикл гри
running = True
bg_color = (0, 0, 0)  # Початковий колір фону

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Зміна кольору фону при натисканні клавіші
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bg_color = change_background_color()
    
    # Зміна швидкості руху
    if keys[pygame.K_UP]:
        speed += 0.1  # Збільшуємо швидкість
    if keys[pygame.K_DOWN]:
        speed = max(1, speed - 0.1)  # Зменшуємо швидкість, не менше ніж 1

    # Очищення екрану
    screen.fill(bg_color)

    # Рух зображення
    image_pos[0] += random.randint(-speed, speed)
    image_pos[1] += random.randint(-speed, speed)

    # Перевірка меж екрану
    image_pos[0] = max(min(image_pos[0], WIDTH - 400), 0)
    image_pos[1] = max(min(image_pos[1], HEIGHT - 400), 0)

    # Мерехтіння зображення
    if random.random() < 0.1:
        alpha = random.randint(0, 255)
        anime_image.set_alpha(alpha)

    # Обертання зображення
    angle += 1  # Збільшення кута обертання
    rotated_image = pygame.transform.rotate(anime_image, angle)  # Обертаємо зображення
    rect = rotated_image.get_rect(center=(image_pos[0] + 200, image_pos[1] + 200))  # Центруємо зображення

    # Відображення зображення
    screen.blit(rotated_image, rect.topleft)

    # Оновлення екрану
    pygame.display.flip()
    pygame.time.delay(30)  # Затримка для управління швидкістю анімації

# Закриття Pygame
pygame.quit()
