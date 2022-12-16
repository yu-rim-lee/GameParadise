import pygame
import random

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Avoid jellfish Game!") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("images/house.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("images/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = (screen_width / 2) - (character_width / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.4

# 적 enemy 캐릭터
enemy = pygame.image.load("images/j.png") #130 위에서 밑으로
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = 0 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy_speed = random.randint(3, 6)

enemy1 = pygame.image.load("images/j1.png") #110 밑에서 위로
enemy1_size = enemy1.get_rect().size # 이미지의 크기를 구해옴
enemy1_width = enemy1_size[0] # 캐릭터의 가로 크기
enemy1_height = enemy1_size[1] # 캐릭터의 세로 크기
enemy1_x_pos = random.randint(0, screen_width -enemy1_width) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy1_y_pos = 640 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy1_speed = random.randint(-6, -3)

enemy2 = pygame.image.load("images/j2.png") #90 >
enemy2_size = enemy2.get_rect().size # 이미지의 크기를 구해옴
enemy2_width = enemy2_size[0] # 캐릭터의 가로 크기
enemy2_height = enemy2_size[1] # 캐릭터의 세로 크기
enemy2_x_pos = 0 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy2_y_pos = random.randint(0, screen_width -enemy2_height) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy2_speed = random.randint(3, 6)

enemy3= pygame.image.load("images/j3.png") #70 >
enemy3_size = enemy3.get_rect().size # 이미지의 크기를 구해옴
enemy3_width = enemy3_size[0] # 캐릭터의 가로 크기
enemy3_height = enemy3_size[1] # 캐릭터의 세로 크기
enemy3_x_pos = 0 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy3_y_pos = random.randint(0, screen_width- enemy3_height) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy3_speed = random.randint(-6, -3)



# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 31

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

game_result = "Game Over"

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    # print("fps :" + str(clock.get_fps()))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    enemy_y_pos += enemy_speed
    enemy1_y_pos += enemy1_speed
    enemy2_x_pos += enemy2_speed
    enemy3_x_pos += enemy3_speed
   
    
     
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width-enemy_width)
    
    if enemy1_y_pos < 0:
        enemy1_y_pos = 640
        enemy1_x_pos = random.randint(0, screen_width-enemy1_width)
    
    if enemy2_x_pos > screen_width:
        enemy2_y_pos = random.randint(0, screen_width-enemy2_width)
        enemy2_x_pos = 0

    if enemy3_x_pos < 0:
        enemy3_y_pos = random.randint(0, screen_width-enemy3_width)
        enemy3_x_pos = 640


    


    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌!!")
        running = False

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy1_rect):
        print("충돌!!")
        running = False

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy2_rect):
        print("충돌!!")
        running = False   
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy3_rect):
        print("충돌!!")
        running = False   
    
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기 
    screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos)) # 적 그리기
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos)) # 적 그리기
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos)) # 적 그리기
 
    

     # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (0, 0, 0))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (510, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        game_result = "YOU WIN!!"
        running = False

    pygame.display.update() # 게임화면을 다시 그리기!

# 게임 오버 메시지
msg = game_font.render(game_result, True , (0, 0, 0))
msg_rect = msg.get_rect(center=(int(screen_width /2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()


# 잠시 대기
pygame.time.delay(1000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()