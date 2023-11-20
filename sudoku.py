import pygame
import sys


def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def draw_game_start(screen, window_width, window_height):
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    screen.blit(background_image, (0, 0))

    title_image = pygame.image.load('SUDOKU TITLE.png')
    title_image = pygame.transform.scale(title_image, (800, 200))
    title_rect = title_image.get_rect(center=(window_width // 2, 150))  # Center the image
    screen.blit(title_image, title_rect)

    button_font = pygame.font.Font(None, 40)
    button_text = ["EASY", "MEDIUM", "HARD"]
    button_width, button_height = 130, 40
    button_spacing = 20

    total_buttons_width = len(button_text) * button_width + (len(button_text) - 1) * button_spacing
    initial_x = (window_width - total_buttons_width) // 2
    global button_rectangles
    button_surfaces = []
    button_rectangles = []

    for i, text in enumerate(button_text):
        text_surface = button_font.render(text, 0, (255, 255, 255))  # Set initial text color to white
        button_surface = pygame.Surface((button_width, button_height))
        button_surface.fill((169, 169, 169))
        button_surface.blit(text_surface, (
            (button_width - text_surface.get_width()) // 2, (button_height - text_surface.get_height()) // 2))

        button_rect = button_surface.get_rect(
            topleft=(initial_x + i * (button_width + button_spacing), window_height - button_height - 20))

        button_surfaces.append(button_surface)
        button_rectangles.append(button_rect)

    for surface, rectangle in zip(button_surfaces, button_rectangles):
        screen.blit(surface, rectangle)

    pygame.display.update()


def change_button_state(button_surface, is_hovered):
    if is_hovered:
        button_surface.fill((0, 0, 255))  # Set button color to blue when hovered
        text_color = (255, 255, 255)  # Set text color to white when hovered
    else:
        button_surface.fill((169, 169, 169))
        text_color = (0, 0, 0)  # Set text color to black when not hovered

    text_surface = button_surface.copy()
    text_surface.fill((0, 0, 0, 0))  # Set text surface to transparent
    text_surface.blit(button_surface, (0, 0))

    font = pygame.font.Font(None, 40)
    rendered_text = font.render("Easy", True, text_color)
    text_rect = rendered_text.get_rect(center=text_surface.get_rect().center)

    text_surface.blit(rendered_text, text_rect.topleft)
    return text_surface


pygame.init()
window_width, window_height = 600, 450
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((window_width, window_height))

# Play background music
play_background_music()

# Draw the game start menu with gray buttons and spacing
draw_game_start(screen, window_width, window_height)

# Declare button_rectangles globally
button_rectangles = []

button_surfaces = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse is over any button
    for i, rectangle in enumerate(button_rectangles):
        if rectangle.collidepoint(mouse_x, mouse_y):
            button_surfaces[i] = change_button_state(button_surfaces[i], True)
        else:
            button_surfaces[i] = change_button_state(button_surfaces[i], False)

    # Redraw the buttons with the updated state
    for surface, rectangle in zip(button_surfaces, button_rectangles):
        screen.blit(surface, rectangle)

    pygame.display.update()


def draw_game_in_progress(screen):
    pass


def draw_game_over(screen):
    pass


if __name__ == "__main__":
    pass
