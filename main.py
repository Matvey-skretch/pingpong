from pygame import*

window = display.set_mode((700,500))
back = (102, 90, 202)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        self.image = transform.scale(image.load(player_image),(h,w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_left = Player("Racket.png", 20, 200, 70, 100, 10)
player_right = Player("Racket.png", 600, 200, 70, 100, 10)
ball = GameSprite("Ball_2.jpg", 300, 200, 50, 50, 10)

finish = False
game = True

speed_x = 5
speed_y = 5

font.init()
font1 = font.SysFont("Arisl", 40)
lose1 = font1.render("Player 1 LOOOse", True, (205, 79, 35))
lose2 = font1.render("Player 2 LOOOse", True, (205, 79, 35))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        player_left.reset()
        player_right.reset()
        ball.reset()
        player_left.update_left()
        player_right.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, player_left) or sprite.collide_rect(ball, player_right):
            speed_x *= -1
        if ball.rect.y < 5 or ball.rect.y > 450:
            speed_y *= -1

        if ball.rect.x < 5:
            window.blit(lose1, (200,200))
            finish = True
        if ball.rect.x > 650:
            window.blit(lose2, (200,200))
            finish = True
    display.update()
    time.delay(50)