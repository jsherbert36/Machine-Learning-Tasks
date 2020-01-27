from pygame.locals import *
from random import randint
import pygame
import time
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
 
def isCollision(self,x1,y1,x2,y2,bsize):
    if x1 >= x2 and x1 <= x2 + bsize:
        if y1 >= y2 and y1 <= y2 + bsize:
            return True
    return False

class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 


def gameplay():
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
    _running = True
    _display_surf = None
    _image_surf = None
    _apple_surf = None
    game = Game()
    player = Player(3) 
    apple = Apple(5,5)
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
 
        if (keys[K_RIGHT]):
            self.player.moveRight()
 
        if (keys[K_LEFT]):
            self.player.moveLeft()
 
        if (keys[K_UP]):
            self.player.moveUp()
 
        if (keys[K_DOWN]):
            self.player.moveDown()
 
        if (keys[K_ESCAPE]):
            self._running = False
 
        self.player.update()
 
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)
        self.on_render()

        
        clock.tick(50)
        pygame.display.flip()


pygame.init()
self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
pygame.display.set_caption('Test Snake Game')
self._running = True
self._image_surf = pygame.Surface([10,10])
self._image_surf.fill(RED)
self._apple_surf = pygame.Surface([10,10])
self._apple_surf.fill(GREEN)
clock = pygame.time.Clock()

while True:
    gameplay()
    print('done')
pygame.quit()