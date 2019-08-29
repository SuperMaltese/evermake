import pygame
import pygame.gfxdraw
import math

def calcArc(pointapointb, angle):
    (a, b) = pointapointb
    distance = math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2))
    r = distance / math.sqrt(2 * (1-math.cos(angle)))
    slant_distance = r * math.cos(angle/2)
    midpoint = (a[0]/2 + b[0]/2, a[1]/2 + b[1]/2)
    old_slope = (b[0]/distance-a[0]/distance, b[1]/distance-a[1]/distance)
    new_slope = (-old_slope[1], old_slope[0])
    center =  (midpoint[0]+slant_distance*new_slope[0],
                    midpoint[1] + slant_distance*new_slope[1])
    #return (center, r, (int(round(center[0]-r)),int(round(center[1]-r)), 2*r, 2*r), math.atan((a[1]-center[1])/(a[0]-center[0])),math.atan((b[1]-center[1])/(b[0]-center[0])))
    return (center, r, math.atan((a[1]-center[1])/(a[0]-center[0])), math.atan((b[1]-center[1])/(b[0]-center[0])))

def drawArc(surface, color, center, r, start, stop, th):
    x = center[0]
    y = center[1]
    points_outer = []
    points_inner = []
    n = round(r*abs(stop-start)/20)
    if n<2:
        n = 2
    for i in range(n):
        delta = i/(n-1)
        phi0 = start + (stop-start)*delta
        x0 = round(x+(r+th)*math.cos(phi0))
        y0 = round(y+(r+th)*math.sin(phi0))
        points_outer.append([x0,y0])
        phi1 = stop + (start-stop)*delta
        x1 = round(x+(r-th)*math.cos(phi1))
        y1 = round(y+(r-th)*math.sin(phi1))
        points_inner.append([x1,y1])
    points = points_outer + points_inner        
    pygame.gfxdraw.aapolygon(surface, points, color)
    pygame.gfxdraw.filled_polygon(surface, points, color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    screen.fill((255,255,255))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.draw.circle(s, (0,0,0), (225,100), 2)
    pygame.draw.circle(s, (0,0,0), (250,250), 2)
    (center, radius, start, end) = calcArc(((225, 100), (250, 250)), math.pi/3)
    #pygame.draw.circle(s, (0,0,0), center, radius)
    #pygame.draw.arc(s, (0,0,0), rect, start, end, 2)
    drawArc(s, (255,0,0), center, radius, start, end, 3,(255,0,0)) 
    screen.blit(s, (0,0))
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        pygame.display.flip()

if __name__ == '__main__':
    main()
