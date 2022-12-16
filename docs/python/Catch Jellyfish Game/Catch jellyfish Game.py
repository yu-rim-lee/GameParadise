import pygame
import random
import time

pygame.init() 

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Catch jellfish Game!") # 게임 이름

done = False
clock = pygame.time.Clock() 
background = pygame.image.load("images/house.png")

def runGame():
    global done
    score = 0
    start_time = int(time.time())
    remain_time = 0
    game_over = 0

    bug_image = pygame.image.load("images/j1.png")
    bug_image = pygame.transform.scale(bug_image, (90 , 90))
    bugs = []
    for i in range(5):
        bug = pygame.Rect(bug_image.get_rect())
        bug.left = random.randint(0, screen_width)
        bug.top = random.randint(0, screen_height)
        dx = random.randint(-9, 9)
        dy = random.randint(-9, 9)
        bugs.append((bug, dx, dy))

    while not done: 
        clock.tick(30)
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
                print(event.pos[0], event.pos[1])
                for (bug, dx, dy) in bugs:
                    if bug.collidepoint(event.pos):
                        print(bug)
                        bugs.remove((bug, dx, dy))
                        bug = pygame.Rect(bug_image.get_rect())
                        bug.left = random.randint(0, screen_width)
                        bug.top = random.randint(0, screen_height)
                        dx = random.randint(-9, 9)
                        dy = random.randint(-9, 9)
                        bugs.append((bug, dx, dy))
                        score += 1

        if game_over == 0:
            for (bug, dx, dy) in bugs:
                bug.left += dx
                bug.top += dy

            remain_time = 31 - (int(time.time()) - start_time)

            if remain_time <= 0:
                game_over = 1

        for (bug, dx, dy) in bugs:
            screen.blit(bug_image, bug)

        for (bug, dx, dy) in bugs:
            if not bug.colliderect(screen.get_rect()):
                bugs.remove((bug, dx, dy))
                bug = pygame.Rect(bug_image.get_rect())
                bug.left = random.randint(0, screen_width)
                bug.top = random.randint(0, screen_height)
                dx = random.randint(-9, 9)
                dy = random.randint(-9, 9)
                bugs.append((bug, dx, dy))

        screen.blit(background, (0, 0)) # 배경 그리기
        screen.blit(bug_image, (bug.left, bug.top, dx, dy))

        score_image = small_font.render('Catch Jellyfish: {}'.format(score), True, (0, 0, 0))
        screen.blit(score_image, (10, 10))

        remain_time_image = small_font.render('Time: {}'.format(remain_time), True, (0, 0, 0))
        screen.blit(remain_time_image, (screen_width - 10 - remain_time_image.get_width(), 10))

        if game_over == 1:
            game_over_image = large_font.render('GameOver', True, RED)
            screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2, screen_height // 2 - game_over_image.get_height() // 2))

        pygame.display.update()
        
runGame()
pygame.quit()


