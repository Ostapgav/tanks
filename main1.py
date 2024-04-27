import pygame 

pygame.init()


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
STEP = 50

#ігрове вікно
windows = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(pygame.image.load("images/background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Класи 
class GameSprite(pygame.sprite.Sprite):
    # конструктор класу
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        pygame.sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = pygame.transform.scale(
            pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.angle = 0
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя на вікні
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.rotate_to(90)
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - 80:
            self.rect.x += self.speed
            self.rotate_to(270)
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.rotate_to(0)
        if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - 80:
            self.rect.y += self.speed
            self.rotate_to(180)
    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate)       
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        # bullets.add(bullet)
class Player2(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.rotate_to(90)
        if keys[pygame.K_d] and self.rect.x < SCREEN_WIDTH - 80:
            self.rect.x += self.speed
            self.rotate_to(270)
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.rotate_to(0)
        if keys[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - 80:
            self.rect.y += self.speed
            self.rotate_to(180)
    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate) 

# клас пульки
class Bullet (GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()
# спрайти
player1 = Player("images/enemy.png",50,50,100,100, STEP)
player2 = Player2("images/panzer.png",50,300,100,100,STEP)
# робочі змінні
game=True 
clock = pygame.time.Clock()
FPS=10
# ігровий цикл
while game:
    windows.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    player1.update()
    player2.update2()
    player1.reset()
    player2.reset()
    clock.tick(FPS)
    pygame.display.update()
    
