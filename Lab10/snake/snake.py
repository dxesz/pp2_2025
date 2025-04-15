import pygame
import random
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="snake",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()


pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 50)]
dx, dy = BLOCK_SIZE, 0
food = (300, 200)
score = 0

font = pygame.font.SysFont("Arial", 25)
clock = pygame.time.Clock()

username = input("Enter your username: ")

def draw_snake():
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

def save_score(username, score):
    conn = psycopg2.connect(database="snake_game", user="postgres", password="1234", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (username, score) VALUES (%s, %s)", (username, score))
    conn.commit()
    cur.close()
    conn.close()

running = True
while running:
    screen.fill(BLACK)
    draw_snake()
    draw_food()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(username, score)
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -BLOCK_SIZE
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, BLOCK_SIZE
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -BLOCK_SIZE, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = BLOCK_SIZE, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if head == food:
        score += 1
        food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()

    if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
        save_score(username, score)
        running = False

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()