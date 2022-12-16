import pygame # 1. pygame 선언

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
BLACK = (0, 0, 0)
size = [640, 640]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ping Pong Game!")

done = False
clock = pygame.time.Clock()

# background = pygame.image.load("house.png")

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 31

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

game_result = "Game Over"        
 

# 4. pygame 무한루프
def runGame():
    global done

    ## 게임판 크기
    screen_width = size[0]
    screen_height = size[1]

    ## 탁구채 크기 (width, height)
    bar_width = 20
    bar_height = 100

    ## 탁구채의 시작점 (x,y), 좌측 맨끝 중앙
    bar_x = bar_start_x = 0
    bar_y = bar_start_y = (screen_height - bar_height) / 2

    ## 탁구공 크기 (반지름)
    circle_radius = 15
    circle_diameter = circle_radius * 2

    ## 탁구공 시작점 (x, y), 우측 맨끝 중앙
    circle_x = circle_start_x =  screen_width - circle_diameter ## 원의 지름 만큼 빼기
    circle_y = circle_start_y =  (screen_width - circle_diameter) / 2

    bar_move = 0
    speed_x, speed_y, speed_bar = -screen_width / 1.28, screen_height / 1.92, screen_height * 1.2
    score = 0

    while not done:
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        screen.fill((255,255,255))

        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_bar * time_sec 
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bar_move = -ai_speed
                elif event.key == pygame.K_DOWN:
                    bar_move = ai_speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bar_move = 0
                elif event.key == pygame.K_DOWN:
                    bar_move = 0
        
        ## 탁구채 이동
        bar_y += bar_move
    
        ## 탁구채 범위 확인
        if bar_y >= screen_height:
            bar_y = screen_height
        elif bar_y <= 0:
            bar_y = 0

        ## 탁구공 범위 확인 
        ## 1) 진행 방향을 바꾸는 행위
        ## 2) 게임이 종료되는 행위
        if circle_x < bar_width: ## bar에 닿았을 때
            
            if circle_y >= bar_y - circle_radius and circle_y <= bar_y + bar_height + circle_radius:
                circle_x = bar_width
                speed_x = -speed_x
                score += 1
        if circle_x < -circle_radius: ## bar에 닿지 않고 좌측 벽면에 닿았을 때, 게임 종료 및 초기화
            circle_x, circle_y = circle_start_x, circle_start_y
            bar_x, bar_y = bar_start_x, bar_start_y
        elif circle_x > screen_width - circle_diameter: ## 우측 벽면에 닿았을 때
            speed_x = -speed_x
        if circle_y <= 0: ## 위측 벽면에 닿았을때
            speed_y = -speed_y
            circle_y = 0
        elif circle_y >= screen_height - circle_diameter: ## 아래 벽면에 닿았을때
            speed_y = -speed_y
            circle_y = screen_height - circle_diameter

        ## 탁구채
        # screen.blit(background, (0, 0))
        pygame.draw.rect(screen, 
                         (255, 0, 0), 
                        (bar_x, bar_y, int(bar_width), int(bar_height)))
        ## 탁구공
        pygame.draw.circle(screen, 
                            (255, 94, 0), 
                            (int(circle_x), int(circle_y)), 
                            int(circle_radius))
                            
        score_image = game_font.render('Ball: {}'.format(score), True, (0, 0, 0))
        screen.blit(score_image, (10, 10))


        # 타이머 집어 넣기
    # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

        timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (0, 0, 0))
    # 출력할 글자, True, 글자 색상
        screen.blit(timer, (510, 10))
        
        if total_time - elapsed_time <= 0:
            game_result = "Game Over!"
            done = True


        
        print(str(score))
        pygame.display.update()

runGame()
pygame.quit()
