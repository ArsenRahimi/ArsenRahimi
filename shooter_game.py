#Создай собственный Шутер!
from pygame import *
from random import *
init()

win_width = 700
win_hight = 500


window = display.set_mode((win_width,win_hight))
display.set_caption("Шутер")


backgraund = transform.scale(image.load("galaxy.jpg"),(win_width,win_hight))



FPS = time.Clock()


class GameSprite(sprite.Sprite): 
    def __init__(self, image_sprite, img_x, img_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y
        self.lost =0


    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Hero(GameSprite):
    def updata(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed

        if keys[K_d] :
            self.rect.x += self.speed
        if keys[K_w] :
            self.fire()
    def fire (self):
        pula = Pula('bullet.png', self.rect.x, self.rect.y, 10)
        object_p.add(pula)
        

      

   
class Enemy(GameSprite):
    def updata(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_hight:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

class Pula(GameSprite):
    def updata(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

font.init()
font = font.Font(None, 40)
kills = font.render('Убито', True, (255,255,255))


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

score = 0

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, randint(1, 5))
    monsters.add(monster)

object_p = sprite.Group()

player = Hero("rocket.png",int(win_width/2),  win_hight - 80, 9)
lost = 0
finish = False
run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_w:
                player.fire()
    if finish != True:
       window.blit(backgraund,(0,0))
       player.show_s()
       player.updata()

    for i in monsters:
        i.show_s()
        i.updata()
    for i in object_p:
        i.show_s()
        i.updata()
    prop = font.render('Пропущено '+str(lost), True, (180, 255, 255))
    window.blit(prop,(10, 10))
    kills = font.render('Убито', True, (255,255,255))
    window.blit(prop,(10, 50))

    
    


    colides = sprite.groupcollide(monsters, object_p, True,True)
    for c in colides:
        score - score + 1
        monster = Enemy('ufo.png', randint(80, win_width - 80), -40, randint(1, 5))
        monsters.add(monster)
    display.update()
    FPS.tick(60)