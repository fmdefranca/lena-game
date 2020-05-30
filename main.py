# coding=utf-8

# imports the Pygame library
import pygame
import random


def main():
    # Set up the colors.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    TRANSPARENT = (0, 0, 0, 0)

    cat_image = pygame.image.load(
        r'C:\Projects\lena-game\images\cat.jpg')
    dog_image = pygame.image.load(
        r'C:\Projects\lena-game\images\dog.jpg')
    cat_image = pygame.transform.scale(cat_image, (950, 950))
    dog_image = pygame.transform.scale(dog_image, (550,850))

    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Keyboard events')

    # sets the window size
    windowSurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    windowSurface.fill(WHITE)

    pygame.display.update()

    # infinite loop
    while True:
        # gets a single event from the event queue
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # captures the 'KEYDOWN' and 'KEYUP' events
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # gets the key name
            key_name = pygame.key.name(event.key)

            if key_name == 'q' or key_name == 'Q':
                break

            if key_name == 'c' or key_name =='C':
                windowSurface.blit(cat_image, (150, 250))
            
            if key_name == 'd' or key_name =='D':
                windowSurface.blit(dog_image, (150, 250))

            # if any key is pressed
            if event.type == pygame.KEYDOWN:
                # prints on the console the key pressed
                print(u'"{}" key pressed'.format(key_name))
                windowSurface.fill(WHITE)
                # pygame.draw.rect(windowSurface, BLUE, (random.randint(
                #     1, 2000), random.randint(1, 2000), random.randint(50, 124), random.randint(50, 124)))

            # if any key is released
            # elif event.type == pygame.KEYUP:
            #     # prints on the console the released key
            #     print(u'"{}" key released'.format(key_name))
            #     windowSurface.fill(WHITE)
            #     pygame.draw.rect(windowSurface, GREEN, (random.randint(
            #         1, 2000), random.randint(1, 2000), random.randint(50, 124), random.randint(50, 124)))

            pygame.display.update()

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
