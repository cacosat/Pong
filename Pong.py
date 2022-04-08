import pygame
import random

pygame.init()

# Window
win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("PONG")

# Paddle 1
p1x = 20
p1y = 10
mov = 0.7  # Velocidad paletas
score_1 = 0
# Paddle 2
p2x = 765
p2y = 10
score_2 = 0

# Ball
bx = 395
by = 240
# Lista de valores posibles de velocidad de la pelotaw
lst_ball_mov = [-0.6, -0.5, -0.4, -0.3, 0.3, 0.4, 0.5, 0.6]
ball_mov1 = random.choice(lst_ball_mov)
ball_mov2 = random.choice(lst_ball_mov)

# Score
score = pygame.font.Font("freesansbold.ttf", 32)

# Main loop
run = True
while run:
    win.fill((0, 0, 0))
    rend_score = score.render(f"{score_1} : {score_2}", True, (255, 255, 255))
    win.blit(rend_score, (367, 235))

    # Diseño cancha:
    pygame.draw.line(win, (255, 255, 255), (400, 0), (400, 210), 3)
    pygame.draw.line(win, (255, 255, 255), (400, 290), (400, 500), 3)
    # Agregar score al medio

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # lista de teclas presionadas

    # Paddle 1 y movimiento
    # P 1: (x, y, width, height) --> (x, y) = en que parte de la pantalla; (w, h) = caracteristicas dibujo
    paddle_1 = pygame.draw.rect(win, (255, 255, 255), (p1x, p1y, 15, 90))
    if keys[pygame.K_w]:
        p1y -= mov
    if keys[pygame.K_s]:
        p1y += mov

    # Paddle 2 y movimiento
    paddle_2 = pygame.draw.rect(win, (255, 255, 255), (p2x, p2y, 15, 90))
    if keys[pygame.K_UP]:
        p2y -= mov
    if keys[pygame.K_DOWN]:
        p2y += mov

    # Ball, movement y score
    ball = pygame.draw.rect(win, (255, 255, 255), (bx, by, 10, 10))
    bx += ball_mov1
    by += ball_mov2

    # Boundaries:
    # Paddles:
    if p1y <= 0:  # Paddle 1
        p1y = 0
    elif p1y >= 410:
        p1y = 410
    if p2y <= 0:  # Paddle 2
        p2y = 0
    elif p2y >= 410:
        p2y = 410
    # Ball
    if by <= 0 or by >= 490:  # Bordes arriba y abajo, Eje Y
        ball_mov2 = -ball_mov2
        by += ball_mov2
    # Collision
    elif 25 <= bx <= 35 and (p1y <= by <= p1y + 90):   # Paddles 1
        ball_mov1 = -ball_mov1
        bx += ball_mov1
    elif 765 >= bx >= 750 and (p2y <= by <= p2y + 90):  # Paddle 2
        ball_mov1 = -ball_mov1
        bx += ball_mov1

    # Reset Ball y puntuación
    if bx > 800:
        bx = 395
        by = 240
        score_1 += 1
        ball_mov1 = random.choice(lst_ball_mov)
        ball_mov2 = random.choice(lst_ball_mov)
    elif bx < 0:
        bx = 395
        by = 240
        score_2 += 1
        ball_mov1 = random.choice(lst_ball_mov)
        ball_mov2 = random.choice(lst_ball_mov)

    # Maxima puntuación
    if score_1 == 7 or score_2 == 7:
        pygame.quit()

    pygame.display.update()



