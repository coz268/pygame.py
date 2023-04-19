import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

meow_sound = pygame.mixer.Sound('meow.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                meow_sound.play()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
