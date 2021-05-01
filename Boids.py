import pygame
import math
from time import sleep
from random import randint
class Boid:
    def __init__(self, pos, rot, spd, range):
        self.pos = pos
        self.rot = rot
        self.spd = spd
        self.range = range

    def getPolygon(self):
        result = [self.pos]

        left_wing = list(self.pos)
        left_wing[0]-=10
        left_wing[1]-=4

        middle_wing = list(self.pos)
        middle_wing[0]-=7

        right_wing = list(self.pos)
        right_wing[0]-=10
        right_wing[1]+=4

        # Rotate around self.pos by self.rot
        # Convert self.rot into PI writing
        rotation = (self.rot/360) * (2*math.pi)
        
        # Rotate wings around self.pos
        left_wing = rotate_around_point(self.pos, left_wing, rotation)
        middle_wing = rotate_around_point(self.pos, middle_wing, rotation)
        right_wing = rotate_around_point(self.pos, right_wing, rotation)

        result.append(tuple(left_wing))
        result.append(tuple(middle_wing))
        result.append(tuple(right_wing))

        return result

    def setRotation(self, rotation):
        self.rot = rotation

    def tick(self, dt):
        rotation = (self.rot/360) * (2*math.pi)
        self.pos = ((self.pos[0] + ( self.spd/10 * dt ) * math.cos( ( rotation  ) % 2*math.pi)) % pygame.display.get_window_size()[0],
                    (self.pos[1] + (self.spd/10 * dt) * math.sin((rotation ) % 2*math.pi)) % pygame.display.get_window_size()[1])
        

def rotate_around_point(center, point, angle):
    rotated_point = [0,0]
    angle *= math.pi
    rotated_point[0] = math.cos(angle) * (point[0] - center[0]) - math.sin(angle) * (point[1] - center[1]) + center[0]
    rotated_point[1] = math.sin(angle) * (point[0] - center[0]) + math.cos(angle) * (point[1] - center[1]) + center[1]

    return tuple(rotated_point)

def main():
    pygame.init()

    pygame.display.set_caption("Boids")
    
    screen = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
    
    screen.fill((255,0,0))
    boids = []
    running = True

    for i in range(0,BOID_AMOUNT):
        x = randint(0,pygame.display.get_window_size()[0])
        y = randint(0,pygame.display.get_window_size()[1])
        rot = randint(0,360)
        boids.append(Boid((x,y),rot,1, 50))

    for b in boids:
        pygame.draw.polygon(screen, (0,255,0), b.getPolygon())

    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255,0,0))

        for i, b in enumerate(boids):
            b.tick(dt)
            pygame.draw.polygon(screen, (0,255,0), b.getPolygon())
            b.setRotation(b.rot + randint(-1,1))
            if i == 0:
                pygame.draw.circle(screen,(255,255,255), b.pos, b.range, 1)

        pygame.display.update()
        

if __name__=="__main__":
    BOID_AMOUNT = 500
    main()
