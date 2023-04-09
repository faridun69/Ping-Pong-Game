from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
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
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.x += self.speed

win_height = 500
win_width = 600

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
back_color = (43, 7, 227)
window.fill(back_color)

racket1 = Player()
racket2 = Player()

clock = time.Clock()
fps = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        #window.blit((0, 0))
        pass

display.update()
clock.tick(fps)