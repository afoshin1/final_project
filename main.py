import pygame
import random
import math
pygame.font.init()
class Mouse(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('1.png'),(50, 50))
        self.rect = pygame.Rect(0,0,0,0)


class Weapon(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('korabl.png'),(200, 200))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
    def draw(self):
        window.blit(self.image, self.rect)
    def shoot(self, angle, a, b):
        bullet = Bullet(angle, a, b)   
        all_sprites.add(bullet)
        bullets.add(bullet)     

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('4.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-100, 0)
        self.rect.y = random.randrange(50,400)
        self.speedy = random.randrange(-1,1)
        self.speedx = random.randrange(1,5)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
        if self.rect.top > 800+10<- 25 or self.rect.right>800+20:
            self.rect.x = random.randrange(-100, 0)
            self.rect.y = random.randrange(50, 400)
            self.speedy = random.randrange(-1, 1)
            self.speedx = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('laser.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.rect.y = 700
        self.rect.x = 350 
        self.speed = 25
        self.speedx = (self.speed*math.cos(angle/57.2))
        self.speedy = -(self.speed*math.sin(angle/57.2))
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.y<0 or self.rect.x<0 or self.rect.x>800:
            self.kill()

k=0
font = pygame.font.SysFont('Arial', 40)
win = font.render(str(k), True, (255, 215, 0))
weapon = Weapon((400, 700))
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
picture = pygame.transform.scale(pygame.image.load('fon.png'), (800,1200))
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
mouse = Mouse((0,0))

otstup = pygame.math.Vector2(10,10)
pygame.display.set_caption('Тир')



for i in range(5):
      m = Mob()
      all_sprites.add(m)
      mobs.add(m)

run = True
while run:
    win = font.render(str(k), True, (255, 215, 0))
    window.blit(picture, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    mouse.rect.x = mouse_pos[0]
    mouse.rect.y = mouse_pos[1]
    pygame.mouse.set_visible(0)
    b = mouse.rect.x+25
    a = mouse.rect.y+25
    dx = b-400
    dy = 700-a
    cos = dx/((math.sqrt(math.pow(dy, 2)+math.pow(dx, 2)))+0.01)
    sin = dy/((math.sqrt(math.pow(dy, 2)+math.pow(dx, 2)))+0.01)
    angle = ((math.acos(cos))*57.2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weapon.shoot(angle, a, b)
        elif event.type == pygame.MOUSEBUTTONDOWN:
                weapon.shoot(angle, a, b)
    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        k+=1
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    weapon_image = pygame.transform.rotozoom(weapon.image, angle-90, 1)
    weapon_otstup = otstup.rotate(-angle)
    weapon_rect = weapon_image.get_rect(center = (400, 750)+weapon_otstup)
    all_sprites.draw(window)
    window.blit(win, (700, 50))
    window.blit(mouse.image, mouse.rect)
    window.blit(weapon_image, weapon_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()