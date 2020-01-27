import pygame,random
from queue import SimpleQueue

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.image = pygame.Surface([self.width,self.width])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,(size[0]-10)//self.width) * self.width
        self.rect.y = random.randint(0,(size[1]-10)//self.width) * self.width
    def reset(self):
        New_Block = False
        while not New_Block:
            self.temp_x = random.randint(0,(size[0]-10)//self.width) * self.width
            self.temp_y = random.randint(0,(size[1]-10)//self.width) * self.width
            for block in snake1.snake_group:
                if block.rect.Rect.collidepoint(self.temp_x,self.temp_y):
                    New_Block = True

        
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.length = 3
        self.Pos_Queue = SimpleQueue()
        self.Head_Block = [size[0]//2,size[1]//2]
        self.snake_group = pygame.sprite.Group()
        self.newsnake = SnakeBlock(self.Head_Block)
        self.snake_group.add(self.newsnake)
        self.newsnake = SnakeBlock((self.Head_Block[0],self.Head_Block[1] + self.width))
        self.snake_group.add(self.newsnake)
        self.newsnake = SnakeBlock((self.Head_Block[0],self.Head_Block[1] + (self.width*2)))
        self.snake_group.add(self.newsnake)
        self.direction = 'down'
        
    def update(self):
        self.Pos_Queue.put(self.Head_Block)
        if self.direction == 'right':
            self.Pos_Queue.put(self.Head_Block)
            self.Head_Block[0] += self.width
        elif self.direction == 'left':
            self.Pos_Queue.put(self.Head_Block)
            self.Head_Block[0] -= self.width
        elif self.direction == 'up':
            self.Pos_Queue.put(self.Head_Block)
            self.Head_Block[1] -= self.width
        elif self.direction == 'down':
            self.Pos_Queue.put(self.Head_Block)
            self.Head_Block[1] += self.width
        self.newsnake = SnakeBlock(self.Head_Block)
        self.snake_group.add(self.newsnake)
        self.temp_last_block = self.Pos_Queue.get()
        for block in self.snake_group:
            if block.rect.x == self.temp_last_block[0] and block.rect.y == self.temp_last_block[1]:
                block.kill()
    def draw(self,display_):
        self.snake_group.draw(display_)
    def move(self,val):
        if val in ['right','left','down','up']:
            self.direction = val
    
class SnakeBlock(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.width = 10
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

def gameplay():
    snake1 = Snake()
    apple1 = Apple()
    apple_group = pygame.sprite.Group()
    apple_group.add(apple1)
    game_over = False
    # -------- Main Program Loop ----------- #
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            snake1.move('right')
        elif keys[pygame.K_LEFT]:
            snake1.move('left')
        elif keys[pygame.K_DOWN]:
            snake1.move('down')
        elif keys[pygame.K_UP]:
            snake1.move('up')

        if pygame.sprite.spritecollide(apple1, snake1.snake_group, False):
            apple1.reset()
        #for block in snake1.snake_group:
        #    if pygame.sprite.spritecollide(block, snake1.snake_group, False):
        #        game_over = True
        for block in snake1.snake_group:
            if block.rect.x < 0 or block.rect.x > size[0] or block.rect.y < 0 or block.rect.y > size[1]:
                game_over = True
        print(snake1.direction)
        snake1.update()
        screen.fill(BLACK)
        apple_group.draw(screen)
        snake1.draw(screen)
        clock.tick(50)
        pygame.display.flip()


pygame.init()
width = 700
height = 700
size = (width,height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while True:
    gameplay()
    print('done')
pygame.quit()
