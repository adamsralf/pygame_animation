import pygame
from pygame.constants import (
    QUIT, K_KP_PLUS, K_KP_MINUS, K_ESCAPE, KEYDOWN
)
import os

class Settings:
    window_width = 1024
    window_height = 400
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        for i in range(6):
            bitmap = pygame.image.load(os.path.join(Settings.image_path, f"cat{i}.bmp")).convert()
            self.images.append(bitmap)
        self.imageindex = 0
        self.image = self.images[self.imageindex]
        self.rect = self.image.get_rect()
        self.rect.centery = Settings.window_height // 2
        self.clock_time = pygame.time.get_ticks()
        self.animation_time = 100

    def update(self):
        if pygame.time.get_ticks() > self.clock_time:
            self.clock_time = pygame.time.get_ticks() + self.animation_time
            self.imageindex += 1
            if self.imageindex >= len(self.images):
                self.imageindex = 0
            self.image = self.images[self.imageindex]

    def decrease_animation_time(self):
        if self.animation_time >= 10:
            self.animation_time -= 10
        else:
            self.animation_time = 0

    def increase_animation_time(self):
        self.animation_time += 10



if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"
#pylint: disable=no-member
    pygame.init()
#pylint: enable=no-member
    screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 12)


    cat = Cat()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_KP_PLUS:
                    cat.decrease_animation_time()
                elif event.key == K_KP_MINUS:
                    cat.increase_animation_time()
        
        cat.update()

        screen.fill((0, 0, 0))
        screen.blit(cat.image, cat.rect)
        text = font.render(f"animation time: {cat.animation_time}", True, (255, 255, 255)) 
        screen.blit(text, (0, Settings.window_height - 50))
        pygame.display.flip()


#pylint: disable=no-member
    pygame.quit()
#pylint: enable=no-member
