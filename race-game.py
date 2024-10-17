import pygame
import time

# Pygame'i başlat
pygame.init()

# Renkler
white = (255, 255, 255)
black = (0, 0, 0)

# Ekran ayarları
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yarış Oyunu')

# Araba
car_image = pygame.image.load('car.png')
car_width, car_height = car_image.get_size()

# Araba konumu
x = (width * 0.45)
y = (height * 0.8)
x_change = 0

# Saat ayarı
clock = pygame.time.Clock()

# Oyun döngüsü
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    game_display.fill(white)
    game_display.blit(car_image, (x, y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
