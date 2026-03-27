from pygame import *
window =display.set_mode((700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

class Ball(GameSprite):
    speed_x = 4
    speed_y = 4
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(self, platform1) or sprite.collide_rect(self, platform2):
            self.speed_x *= -1
    
platform1 = Player('platform1.png', 10, 200, 6, 50, 150)
platform2 = Player('platform2.png', 640, 200, 6, 50, 150)
ball = Ball('ball.png', 300, 200, 7, 50, 50)
font.init()
win1 = font.SysFont('Arial', 50).render('первый игрок выиграл', True, (0, 255, 0))
win2 = font.SysFont('Arial', 50).render('второй игрок выиграл', True, (0, 255, 0))


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((255, 255, 255))
        if ball.rect.x > 650:
            window.blit(win1, (200, 200))
            finish = True
        elif ball.rect.x < 0:
            window.blit(win2, (200, 200))
            finish = True

        platform1.update1()
        platform1.reset()
        platform2.update2()
        platform2.reset()
        ball.update()
        ball.reset()
        display.update()
    clock.tick(60)