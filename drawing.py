import pygame
import pygame.gfxdraw

def drawHandle(s):
    pygame.gfxdraw.filled_polygon(s, ((235, 330), (265, 330), (265, 400), (235, 400)), (235, 50, 0)) 
    pygame.draw.polygon(s, (10, 10, 10), ((235, 330), (265, 330), (265, 400), (235, 400)), 3)

def drawGuard(s): 
    pygame.gfxdraw.filled_polygon(s, ((225, 300), (275, 300), (300, 280), (300, 300), (265, 330), (235, 330), (200, 300), (200, 280)), (255, 255, 10))
    pygame.draw.polygon(s, (0,0,0), ((225, 300), (275, 300), (300, 280), (300, 300), (265, 330), (235, 330), (200, 300), (200, 280)), 3)

def setup():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    screen.fill((200,100,0))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    return (s, screen)

def finish(s, screen):
    screen.blit(s, (0,0))
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
def main():
    (s, screen) = setup() 
    pygame.gfxdraw.filled_polygon(s, ((250, 70), (275, 100), (275, 300), (225, 300), (225, 100)), (200, 200, 240))
    drawGuard(s) 
    drawHandle(s)
    pygame.gfxdraw.filled_polygon(s, ((275, 110), (275, 300), (225, 300)), (220, 220, 220))
    pygame.gfxdraw.filled_polygon(s, ((225, 100), (250, 100), (250, 70)), (210, 210, 250))
    pygame.gfxdraw.filled_polygon(s, ((250, 200), (225, 300), (275, 300)), (210, 210, 250))
    pygame.gfxdraw.filled_polygon(s, ((250, 100), (275, 100), (275, 100), (250, 200)), (210, 210, 250))
    pygame.draw.polygon(s, (10, 10, 10), ((250, 70), (275, 100), (275, 300), (225, 300), (225, 100)), 3)
    pygame.draw.line(s, (240, 240, 255), (250, 95), (250, 200))
    finish(s, screen)
    
if __name__ == '__main__':
    main()
