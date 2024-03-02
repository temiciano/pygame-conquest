import pygame, sys

# Clase para todos los personajes
class Personaje:
    def __init__(self, pos, speed, idle, walk, jump):
        self.image = pygame.image.load(walk[0])
        self.pos = pos
        self.speed = speed
        self.idle = [pygame.image.load(sprite) for sprite in idle]
        self.walk = [pygame.image.load(sprite) for sprite in walk]
        self.frame = 0
        self.flip = False
        self.walkcounter = 0
        self.idlecounter = 0
        self.jump = False
        self.jumpSpeed = 6
        self.gravity = 1

    def move(self, keys):
        if keys[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            self.pos[1] -= self.jumpSpeed * 4
            self.jumpSpeed -= self.gravity
            if self.jumpSpeed < -6:
                self.jump = False
                self.jumpSpeed = 6
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
            self.flip = False
            self.walkcounter += 1
            if self.walkcounter % 5 == 0:
                self.frame = (self.frame + 1) % len(self.walk)
                self.image = self.walk[self.frame]
        elif keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
            self.flip = True
            self.walkcounter += 1
            if self.walkcounter % 5 == 0:  # Cambiar el sprite cada 5 ciclos
                self.frame = (self.frame + 1) % len(self.walk)
                self.image = self.walk[self.frame]
        else:
            self.pos[0] == self.pos
            self.walkcounter == 0
            self.idlecounter += 1
            if self.idlecounter % 10 == 0:
                self.frame = (self.frame + 1) % len(self.idle)
                self.image = self.idle[self.frame]


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.pos)

pygame.init()

ANCHO, ALTO = 640, 360
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Conquest")

# Framerate
clock = pygame.time.Clock()
FRAMERATE = 24

NEGRO = (0,0,0)
screen.fill (NEGRO)

# Crear los personajes
Player = Personaje([100,180], 3, ['sprites/player/idle1.png', 'sprites/player/idle2.png'], ['sprites/player/walk1.png', 'sprites/player/walk2.png'])

#Bucle de juego  y controles
while True:
    clock.tick(FRAMERATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    Player.move(keys)

    screen.fill(NEGRO)
    Player.draw()
    pygame.display.update()
