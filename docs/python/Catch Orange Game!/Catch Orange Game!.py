import pygame # 1. pygame 선언
import random
from datetime import datetime
from datetime import timedelta
 
pygame.init() # 2. pygame 초기화

 
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch White Game!") # 게임 이름

clock = pygame.time.Clock()
done= False
# background = pygame.image.load("house.png")

 

clock= pygame.time.Clock()
last_moved_time = datetime.now()
 
KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN: 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E',
}
 
def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)
 
class Snake:
    def __init__(self):
        self.positions = [(0,6),(0,5),(0,4),(0,3),(0,2),(0,1),(0,0)]  # 뱀의 위치
        self.direction = ''
 
    def draw(self):
        for position in self.positions: 
            draw_block(screen, (102,37,0), position)
 
    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]
 
    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'C':
            self.positions.append((y, x + 1))    

        
        
 
 
class Apple:
    Apple = pygame.image.load("j.png")
    def __init__(self, position=(15, 15)):
        self.position = position
 
    def draw(self):
        draw_block(screen, (255, 87, 0), self.position)

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 31

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

game_result = "Game Over"        
 
# 4. pygame 무한루프
def runGame():
    global done, last_moved_time
    #게임 시작 시, 뱀과 사과를 초기화
    snake = Snake() 
    apple = Apple()
    score = 0 
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
                 

 
        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
 
        if snake.positions[0] == apple.position:
              
            snake.grow()    
            apple.position = (random.randint(0, 19), random.randint(0, 19))
             
            score += 1
            
            
            
        if snake.positions[0] in snake.positions[1:]:
            done = True
            return score
 
        # screen.blit(background, (0, 0)) # 배경 그리기
        snake.draw()
        apple.draw()

        score_image = game_font.render('Catch white: {}'.format(score), True, (0, 0, 0))
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

        pygame.display.update() # 게임화면을 다시 그리기!
    
msg = game_font.render(game_result, True , (0, 0, 0))
msg_rect = msg.get_rect(center=(320, 320))
screen.blit(msg, msg_rect)
pygame.display.update()

# pygame.time.delay(1000)


runGame()
pygame.quit()
