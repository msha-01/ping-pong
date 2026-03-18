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
    def update(self, speed_x, speed_y):
        self.rect.x += speed_x
        self.rect.y += speed_y

    
platform1 = Player('platform1.png', 10, 200, 6, 50, 150)
platform2 = Player('platform2.png', 640, 200, 6, 50, 150)
ball = Ball('ball.png', 300, 200, 7, 50, 50)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255, 255, 255))

    platform1.update1()
    platform1.reset()
    platform2.update2()
    platform2.reset()
    ball.update(4, 4)
    ball.reset()
    display.update()
    clock.tick(60)