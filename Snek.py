import pygame
from pygame.locals import *
import random

class apple:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.on = 0
        self.Surface = pygame.image.load('apple.png')

    # Spawn apple in random location
    def placeFood(self):
        self.x = round(random.randint(0,theApp.width-10)/10)*10
        self.y = round(random.randint(0,theApp.height-10)/10)*10

    def genFood(self):
        self.Surface.convert()
        theApp.screen.blit(self.Surface, (self.x, self.y))

class segment:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = -10
        self.y = -10
        self.dir = 2
        self.dirold = 2
        self.Surface = pygame.Surface((self.width, self.height))

    # Display Segment
    def gen(self):
        if snekington.moving == True:
            self.Surface.fill((0,255,0))
        else:
            self.Surface.fill((63, 32, 0))
        self.Surface.convert()
        theApp.screen.blit(self.Surface, (self.x, self.y))

class snake:
    def __init__(self):
        self.body = []
        self.moving = True
        self.didMove = False
        self.setSnake()

    def setSnake(self):
        # First 3 Segments
        self.body.append(segment())
        self.body[0].x = 20
        self.body[0].y = round((theApp.height/2)/10)*10
        self.body.append(segment())
        self.body[0].x = 10
        self.body[0].y = round((theApp.height/2)/10)*10
        self.body.append(segment())
        self.body[0].x = 0
        self.body[0].y = round((theApp.height/2)/10)*10

    # Clone to lead position after inser()
    def tailMe(self):
        self.body[0].x = self.body[1].x
        self.body[0].y = self.body[1].y
        self.body[0].dir = self.body[1].dir
        self.body[0].dirold = self.body[1].dirold

    # Update Position of the Snake
    def move(self):

        # Move Left
        if self.body[0].dir == 0:
            if self.body[0].dirold == 2:
                self.body[0].dir = 2
                self.move()
                return
            self.crash(food1)
            if self.moving == False:
                self.genSnake()
                return
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].x -= 10

        # Move Up
        elif self.body[0].dir == 1:
            if self.body[0].dirold == 3:
                self.body[0].dir = 3
                self.move()
                return
            self.crash(food1)
            if self.moving == False:
                self.genSnake()
                return
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].y -= 10

        # Move Right
        elif self.body[0].dir == 2:
            if self.body[0].dirold == 0:
                self.body[0].dir = 0
                self.move()
                return
            self.crash(food1)
            if self.moving == False:
                self.genSnake()
                return
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].x += 10

        # Move Down
        elif self.body[0].dir == 3:
            if self.body[0].dirold == 1:
                self.body[0].dir = 1
                self.move()
                return
            self.crash(food1)
            if self.moving == False:
                self.genSnake()
                return
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].y += 10
        self.genSnake()
        self.body[0].dirold = self.body[0].dir

    # Display all Segments in Snake Body
    def genSnake(self):
        for i in range(len(self.body)):
            self.body[i].gen()

    # Increase Snake
    def grow(self):
        self.body.append(segment())
    
    # Collision Detection
    def crash(self, apple):
        # Check move left
        if self.body[0].dir == 0:
            # Wall Check
            if (self.body[0].x-10 == -10):
                self.moving = False
                return
            # Body Check
            for i in range(len(self.body)):
                if (self.body[0].x-10 == self.body[i].x) and (self.body[0].y == self.body[i].y):
                    self.moving = False
                    return
            # Apple Check
            if (self.body[0].x-10 == apple.x) and (self.body[0].y == apple.y):
                apple.placeFood()
                self.grow()
                return

        # Check move up
        elif self.body[0].dir == 1:
            # Wall Check
            if (self.body[0].y-10 == -10):
                self.moving = False
                return
            # Body Check
            for i in range(len(self.body)):
                if (self.body[0].x == self.body[i].x) and (self.body[0].y-10 == self.body[i].y):
                    self.moving = False
                    return
            # Apple Check
            if (self.body[0].x == apple.x) and (self.body[0].y-10 == apple.y):
                apple.placeFood()
                self.grow()
                return

        # Check move right
        elif self.body[0].dir == 2:
            # Wall Check
            if (self.body[0].x+10 == theApp.width):
                self.moving = False
                return
            # Body Check
            for i in range(len(self.body)):
                if (self.body[0].x+10 == self.body[i].x) and (self.body[0].y == self.body[i].y):
                    self.moving = False
                    return
            # Apple Check
            if (self.body[0].x+10 == apple.x) and (self.body[0].y == apple.y):
                apple.placeFood()
                self.grow()
                return  

        # Check move down
        elif self.body[0].dir == 3:
            # Wall Check
            if (self.body[0].y+10 == theApp.height):
                self.moving = False
                return
            # Body Check
            for i in range(len(self.body)):
                if (self.body[0].x == self.body[i].x) and (self.body[0].y+10 == self.body[i].y):
                    self.moving = False
                    return
            # Apple Check
            if (self.body[0].x == apple.x) and (self.body[0].y+10 == apple.y):
                apple.placeFood()
                self.grow()
                return

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snekington's big Journey")
        self._running = True
        self.screen = None
        self.gameTick = 0
        self.width = 320
        self.height = 320
        self.size = self.height , self.width

    def on_init(self):
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.image.load('background.png')
        self.background.convert()
        self._running = True

    def resetGame(self):
        snekington.body.clear()
        snekington.setSnake()
        snekington.moving = True
        food1.placeFood()

    # Input Block
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_UP:
                if snekington.body[0].dir == 3:
                    return
                else:
                    snekington.body[0].dir = 1
            elif event.key == pygame.K_LEFT:
                if snekington.body[0].dir == 2:
                    return
                else:
                    snekington.body[0].dir = 0
            elif event.key == pygame.K_RIGHT:
                if snekington.body[0].dir == 0:
                    return
                else:
                    snekington.body[0].dir = 2
            elif event.key == pygame.K_DOWN:
                if snekington.body[0].dir == 1:
                    return
                else:
                    snekington.body[0].dir = 3
          

    # Calculations Block
    def on_loop(self):

        # End State Check
        if snekington.moving == False:
            passEnd = False
            while not passEnd:
                self.check = pygame.event.wait(5000)
                if self.check.type == KEYDOWN:
                    if self.check.key == pygame.K_ESCAPE:
                        self._running = False
                        passEnd = True
                    elif self.check.key == pygame.K_SPACE:
                        self.resetGame()
                        passEnd = True
                    else:
                        pass
        
        # is game valid
        if snekington.moving == True:

            # Time Check
            if pygame.time.get_ticks() >= self.gameTick + 100:

                # Refresh Stage
                self.screen.blit(self.background,(0,0))

                # Apple Blink
                if food1.on == 3:
                    food1.on = 0
                else:
                    food1.genFood()
                    food1.on += 1

                # Move and Render Snake
                snekington.move()

                # Set Time
                self.gameTick = pygame.time.get_ticks()
        else:
            food1.genFood()
    # Render Block
    def on_render(self):
        pygame.display.update()
    def on_cleanup(self):
        pygame.quit()
    
    # Run Blcok
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            pygame.event.set_allowed(pygame.KEYDOWN)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    snekington = snake()
    food1 = apple()
    food1.placeFood()
    theApp.on_execute()