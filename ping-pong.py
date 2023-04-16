from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, a, b, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (a, b))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_height = 500
win_width = 600

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
back_color = (43, 7, 227)
window.fill(back_color)

racket1 = Player('racket.png', 30, 200, 25, 100, 4)
racket2 = Player('racket.png', 520, 200, 25, 100, 4)
ball = GameSprite('tennis_ball.png', 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3
clock = time.Clock()
fps = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back_color)
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        ball.reset()

    display.update()
    clock.tick(fps)
