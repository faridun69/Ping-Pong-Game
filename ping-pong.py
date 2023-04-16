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
racket2 = Player('racket.png', 550, 200, 25, 100, 4)
ball = GameSprite('tennis_ball.png', 200, 200, 70, 70, 4)

font.init()
font_1 = font.SysFont('Arial', 50)

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
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y < 50:
            speed_y *= -1
        if ball.rect.y > win_height - 50:
            speed_y *= -1
        if ball.rect.x < 5:
            lose1 = font_1.render('ИГРОК 1 ПРОИГРАЛ!', True, (255, 0, 0))
            window.blit(lose1, (50, 200))
            finish = True
        elif ball.rect.x > win_width - 5:
            lose2 = font_1.render('ИГРОК 2 ПРОИГРАЛ!', True, (255, 0, 0))
            window.blit(lose2, (50, 220))
            finish = True
    display.update()
    clock.tick(fps)
