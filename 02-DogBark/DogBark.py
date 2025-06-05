import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30
    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    image = pygame.image.load("2dogs.JPG")
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("noteworthy", 28)

    font2 = pygame.font.SysFont("'geneva", 30)
    caption2 = font2.render("Mine!!",True, WHITE)

    print(pygame.font.get_fonts())
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Dog Fight", True, BLACK)
    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill(WHITE)
        screen.blit(image, (0, 0))

        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        x_loc = screen.get_width() / 2 - caption1.get_width() / 2
        y_loc = image.get_height() -5
        screen.blit(caption1, (x_loc, y_loc))
        screen.blit(caption2, (50, 200))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
