import pygame
import random

class segment:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = -10
        self.y = -10
        self.dir = 0
        self.full = False
        self.Surface = pygame.Surface((self.width, self.height))

    def gen(self):
        self.Surface.fill((255,0,0))
        self.Surface.convert()
        theApp.screen.blit(self.Surface, (self.x, self.y))

class apple:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = round(random.randint(0,theApp.width-10)/10)*10
        self.y = round(random.randint(0,theApp.height-10)/10)*10
        self.Surface = pygame.Surface((self.width, self.height))

    def placeFood(self):
        self.Surface.fill((255,255,0))
        self.Surface.convert()
        theApp.screen.blit(self.Surface, (self.x, self.y))


class snake:
    def __init__(self):
        self.body = []
        self.moving = False
        self.body.append(segment())
        self.body[0].x = 20
        self.body[0].y = 360
        self.body.append(segment())
        self.body[0].x = 10
        self.body[0].y = 360
        self.body.append(segment())
        self.body[0].x = 0
        self.body[0].y = 360

    def tailMe(self):
        self.body[0].x = self.body[1].x
        self.body[0].y = self.body[1].y
        self.body[0].dir = self.body[1].dir

    def move(self):
        if self.body[0].dir == 0:
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].x -= 10

        elif self.body[0].dir == 1:
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].y -= 10

        elif self.body[0].dir == 2:
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].x += 10

        elif self.body[0].dir == 3:
            self.body.insert(0,segment())
            self.tailMe()
            self.body.pop()
            self.body[0].y += 10

        for i in range(len(self.body)):
            self.body[i].gen()

    def grow(self):
        self.body.append(segment())
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.nofood = True
        self.gameTick = 0
        self.size = self.width , self.height = 600 , 600

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface((self.width,self.height))
        self.background.fill((0,0,0))
        self.background.convert()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_UP:
                snekington.body[0].dir = 1
                snekington.moving = True
            if event.key == pygame.K_LEFT:
                snekington.body[0].dir = 0
                snekington.moving = True
            if event.key == pygame.K_RIGHT:
                snekington.body[0].dir = 2
                snekington.moving = True
            if event.key == pygame.K_DOWN:
                snekington.body[0].dir = 3
                snekington.moving = True
            if event.key == pygame.K_SPACE:
                snekington.grow()

    def on_loop(self):
        if self.nofood == True:
            food1.placeFood()
            self.nofood == False
        if snekington.moving == True:
            if pygame.time.get_ticks() >= self.gameTick + 250:
                self.screen.blit(self.background,(0,0))
                snekington.move()
                self.gameTick = pygame.time.get_ticks()
    def on_render(self):
        pygame.display.update()
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    snekington = snake()
    food1 = apple()
    theApp.on_execute()