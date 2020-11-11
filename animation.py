"""Animation with pygame.

A short program which shows how to implement an animation with PyGame.
"""
import pygame
from pygame.constants import (
    QUIT, K_KP_PLUS, K_KP_MINUS, K_ESCAPE, KEYDOWN
)
import os


class Settings:
    """Project global informations.

    This static class contains project global informations like window size and file directories.
    """
    window_width = 1024
    window_height = 400
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")


class Cat(pygame.sprite.Sprite):
    """A cat sprite class.

    Short sprite example with no other function as showing how to implement 
    an animation manually. This class is derived from pygame.sprite.Sprite. 
    """

    def __init__(self):
        """Constructor function.

        Besides all other usual tasks of a constructor this function loads the 
        bitmaps of the animation and stores them into an array. 
        """
        super().__init__()
        self.images = []
        for i in range(6):
            bitmap = pygame.image.load(os.path.join(
                Settings.image_path, f"cat{i}.bmp")).convert()
            self.images.append(bitmap)
        self.imageindex = 0
        self.image = self.images[self.imageindex]
        self.rect = self.image.get_rect()
        self.rect.centery = Settings.window_height // 2
        self.clock_time = pygame.time.get_ticks()
        self.animation_time = 100

    def update(self):
        """Updates the status of the sprite.

        Only the animation part of "update()" is implemented. 
        The animation part checks if the given time frame is reached
        and changes the imageindex. The imageindex controls which 
        bitmap of the animation is to be shown.
        """
        if pygame.time.get_ticks() > self.clock_time:
            self.clock_time = pygame.time.get_ticks() + self.animation_time
            self.imageindex += 1
            if self.imageindex >= len(self.images):
                self.imageindex = 0
            self.image = self.images[self.imageindex]
        # implement game depending logic here

    def change_animation_time(self, delta=10):
        """Decrease the duration between two animation steps by 10ms.

        Keyword arguments:
        delta -- this value in ms will be added to the actual duration (default 10)

        The duration between two animation steps is controlled by the
        member animation_time. By calling this method the animation time will be
        changed by delta ms. The smallest value is 0.
        """
        self.animation_time += delta
        if self.animation_time <= 0:
            self.animation_time = 0


if __name__ == '__main__':
    """Main function

    Starts and runs the the animation example. 

    Hint: This is not a testing main function.
    """

    # Preparation
    os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"
#pylint: disable=no-member
    pygame.init()
#pylint: enable=no-member
    screen = pygame.display.set_mode(
        (Settings.window_width, Settings.window_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 12)

    cat = Cat()
    cat.change_animation_time()
    # main loop
    running = True
    while running:
        clock.tick(60)
        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_KP_PLUS:
                    cat.change_animation_time(-10)
                elif event.key == K_KP_MINUS:
                    cat.change_animation_time(10)

        # update
        cat.update()

        # draw
        screen.fill((0, 0, 0))
        screen.blit(cat.image, cat.rect)
        text = font.render(
            f"animation time: {cat.animation_time}", True, (255, 255, 255))
        screen.blit(text, (0, Settings.window_height - 50))
        pygame.display.flip()

    # bye bye
#pylint: disable=no-member
    pygame.quit()
#pylint: enable=no-member
