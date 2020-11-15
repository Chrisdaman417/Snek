import pygame
#from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width , self.height = 1280 , 720

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface((int(self.width/2),int(self.height/2)))
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _running = False
            if event.key == pygame.K_RETURN:
                self.background.fill((255,255,255))
                self.background.convert()
                self.screen.blit(self.background, (int(self.width / 2 / 2),int(self.height / 2 / 2)))
            if event.key == pygame.K_SPACE:
                self.background.fill((0,255,0))
                self.background.convert()
                self.screen.blit(self.background, (int(self.width / 2 / 2),int(self.height / 2 / 2)))
            if event.key == pygame.K_UP:
                box.Surface.fill((0,0,0))
                self.screen.blit(box.Surface, (box.x, box.y))
                box.Surface.fill((255,0,0))
                box.y -= 10
                box.Surface.convert()
                self.screen.blit(box.Surface, (box.x, box.y))
            if event.key == pygame.K_LEFT:
                box.Surface.fill((0,0,0))
                self.screen.blit(box.Surface, (box.x, box.y))
                box.Surface.fill((255,0,0))
                box.x -= 10
                box.Surface.convert()
                self.screen.blit(box.Surface, (box.x, box.y))
            if event.key == pygame.K_RIGHT:
                box.Surface.fill((0,0,0))
                self.screen.blit(box.Surface, (box.x, box.y))
                box.Surface.fill((255,0,255))
                box.x += 10
                box.Surface.convert()
                self.screen.blit(box.Surface, (box.x, box.y))
            if event.key == pygame.K_DOWN:
                box.Surface.fill((0,0,0))
                self.screen.blit(box.Surface, (box.x, box.y))
                box.Surface.fill((255,255,0))
                box.y += 10
                box.Surface.convert()
                self.screen.blit(box.Surface, (box.x, box.y))

    def on_loop(self):
        pass
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

class object:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 0
        self.y = 0
        self.dir = 0
        self.Surface = pygame.Surface((self.width, self.height))

if __name__ == "__main__":
    theApp = App()
    box = object()
    theApp.on_execute()