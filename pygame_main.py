import pygame
from game import choices, win_or_lose, ScoreBoard
import random

scoreboard = ScoreBoard()

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
top_color = (70, 130, 180)
bottom_color = (20, 20, 20)
for y in range(600):
    ratio = y / 600
    color = tuple(int(top_color[i] * (1 - ratio) + bottom_color[i] * ratio) for i in range(3))
    pygame.draw.line(background, color, (0, y), (800, y))
font = pygame.font.Font(None, 60)
title = font.render("Камень, ножницы, бумага", True, (255, 255, 255))

button_font = pygame.font.Font(None, 40)
result_font = pygame.font.Font(None, 30)
score_font = pygame.font.Font(None, 30)
rock_button = pygame.Rect(150, 300, 200, 50)
scissors_button = pygame.Rect(450, 300, 200, 50)
paper_button = pygame.Rect(300, 400, 200, 50)
exit_button = pygame.Rect(690, 540, 100, 50)

pygame.display.set_caption("Камень, ножницы, бумага")
running = True

rock_text = button_font.render("Камень", True, (255, 255, 255))
scissors_text = button_font.render("Ножницы", True, (255, 255, 255))
paper_text = button_font.render("Бумага", True, (255, 255, 255))
exit_text = button_font.render("Выход", True, (255, 255, 255))

rock_text_rect = rock_text.get_rect(center=rock_button.center)
scissors_text_rect = scissors_text.get_rect(center=scissors_button.center)
paper_text_rect = paper_text.get_rect(center=paper_button.center)
exit_text_rect = exit_text.get_rect(center=exit_button.center)

result = ""

while running:
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    if rock_button.collidepoint(mouse_pos):
        rock_color = (100, 100, 100)
    else:
        rock_color = (70, 130, 180)
    if scissors_button.collidepoint(mouse_pos):
        scissors_color = (100, 100, 100)
    else:
        scissors_color = (70, 130, 180)
    if paper_button.collidepoint(mouse_pos):
        paper_color = (100, 100, 100)
    else:
        paper_color = (70, 130, 180)
    if exit_button.collidepoint(mouse_pos):
        exit_color = (100, 100, 100)
    else:
        exit_color = (70, 130, 180)

    pygame.draw.rect(screen, rock_color, rock_button, border_radius=15)
    pygame.draw.rect(screen, scissors_color, scissors_button, border_radius=15)
    pygame.draw.rect(screen, paper_color, paper_button, border_radius=15)
    pygame.draw.rect(screen, exit_color, exit_button, border_radius=15)

    screen.blit(rock_text, rock_text_rect)
    screen.blit(scissors_text, scissors_text_rect)
    screen.blit(paper_text, paper_text_rect)
    screen.blit(exit_text, exit_text_rect)
    screen.blit(title, (140, 60))

    if result:
        result_text = result_font.render(result, True, (255, 255, 255))
        result_rect = result_text.get_rect(center=(400, 500))
        screen.blit(result_text, result_rect)

    score_text = score_font.render(f"Счет: Вы {scoreboard.user_score} - Компьютер {scoreboard.computer_score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(400, 550))
    screen.blit(score_text, score_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_button.collidepoint(event.pos):
                user_choice = "камень"
            elif scissors_button.collidepoint(event.pos):
                user_choice = "ножницы"
            elif paper_button.collidepoint(event.pos):
                user_choice = "бумага"
            elif exit_button.collidepoint(event.pos):
                scoreboard.save_score()
                running = False
                continue
            else:
                user_choice = None

            if user_choice:
                computer_choice = random.choice(choices)
                result = win_or_lose(user_choice, computer_choice)
                scoreboard.update_score(result)

pygame.quit()