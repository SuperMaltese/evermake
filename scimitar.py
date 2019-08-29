import pygame
import pygame.gfxdraw
import math
from drawing import drawGuard, drawHandle, setup, finish
from draw_arc import calcArc, drawArc

import cv2

def main():
    (s, screen) = setup()
    drawGuard(s)
    drawHandle(s)
    
    (center, radius, start, end) = calcArc(((200, 100), (275, 250)), math.pi/2)
    drawArc(s, (0,0,0), center, radius, start, end, 1.5)
    (center, radius, start, end) = calcArc(((200, 130), (225,250)), math.pi/2)
    drawArc(s, (0,0,0), center, radius , start, end, 1.5)
    pygame.draw.line(s, (0,0,0), (200, 100), (200,130), 4)
    pygame.draw.line(s, (0,0,0), (275,250), (275, 300),4)
    pygame.draw.line(s, (0,0,0), (225,250), (225, 300),4)
    pygame.draw.line(s, (0,0,0), (225,300), (275,300), 4)

    s2 = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    s2.fill((255,0,0))
    s2.blit(s,(0,0))

    surf_array = pygame.surfarray.array3d(s2)

    cv2.floodFill(surf_array, None, (250,250), (100, 100, 140))
    pygame.surfarray.blit_array(s2, surf_array)
    
    surf_array = pygame.surfarray.array3d(s2)

    #make mask of where the transparent bits are
    trans_mask = surf_array[:,:,:3] == [255, 255, 255]

    #replace areas of transparency with white and not transparent
    surf_array[trans_mask] = [255, 255, 255]

    #new image without alpha channel...
    pygame.surfarray.blit_array(s2, surf_array)

    finish(s2, screen)

if __name__ == "__main__":
    main()

