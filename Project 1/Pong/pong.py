import pygame
from random import randint

pygame.init()

bounce_sound = pygame.mixer.Sound('bounce.wav')


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 500:
            self.rect.y = 500


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        pygame.mixer.Sound.play(bounce_sound)
        pygame.mixer.music.stop()
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def reset(self):
        self.rect.centerx = 400
        self.rect.centery = 300
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size = (800, 600)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Pong")

paddle_l = Paddle(WHITE, 20, 100)
paddle_l.rect.x = 40
paddle_l.rect.y = 250

paddle_r = Paddle(WHITE, 20, 100)
paddle_r.rect.x = 740
paddle_r.rect.y = 250

ball = Ball(WHITE, 10, 10)
ball.rect.x = 295
ball.rect.y = 395

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle_l)
all_sprites_list.add(paddle_r)
all_sprites_list.add(ball)

running = True

clock = pygame.time.Clock()

score_l = 0
score_r = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_l.moveUp(5)
    if keys[pygame.K_s]:
        paddle_l.moveDown(5)
    if keys[pygame.K_UP]:
        paddle_r.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle_r.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 790:
        score_l += 1
        ball.reset()
    if ball.rect.x <= 0:
        score_r += 1
        ball.reset()
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle_l) or pygame.sprite.collide_mask(ball, paddle_r):
        ball.bounce()

    window.fill(BLACK)
    all_sprites_list.draw(window)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score_l), True, WHITE)
    window.blit(text, (250, 10))
    text = font.render(str(score_r), True, WHITE)
    window.blit(text, (550, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
