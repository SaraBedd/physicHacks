import pygame
import os

# colors
MENU_BACKGROUND_COLOR = (50, 50, 50)
BUTTON_COLOR = (0, 255, 0)
BUTTON_HOVER_COLOR = (100, 255, 100)
TEXT_COLOR = (255, 255, 255)
# constants
LOGO_SIZE = (150, 150)
FONT_NAME = 'assets\\font\\Debrosee-ALPnL.ttf'
FONT_NAME_2 = 'assets\\font\\Pixellettersfull-BnJ5.ttf'
BUTTON_BORDER_RADIUS = 10

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font(FONT_NAME, 32)
        self.title_font = pygame.font.Font(FONT_NAME, 90)
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'logoVf.png')), LOGO_SIZE)
        self.logo_rect = self.logo.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery - 200))
        self.start_button_text = "Start"
        self.start_button_rect = pygame.Rect(self.screen_rect.centerx - 100, self.screen_rect.centery + 100, 200, 50)

    def draw_button(self, text, rect, active):
        color = BUTTON_HOVER_COLOR if active else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, rect, border_radius=BUTTON_BORDER_RADIUS)      
        text_surf = self.font.render(text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=rect.center)

        self.screen.blit(text_surf, text_rect)

    def draw_footer(self):
        footer_logo = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'hackPhysics.png')), (80, 80))
        footer_logo_rect = footer_logo.get_rect(bottomleft=(10, self.screen_rect.bottom - 10))

        self.screen.blit(footer_logo, footer_logo_rect)

        footer_font = pygame.font.Font(FONT_NAME_2, 21)
        footer_text = "Created during McHacks Physics by Patrick and others aka Thomas, Elias, Khalil, and Sara"
        footer_text_surf = footer_font.render(footer_text, True, TEXT_COLOR)
        footer_text_rect = footer_text_surf.get_rect(midleft=(footer_logo_rect.right + 10, footer_logo_rect.centery))

        self.screen.blit(footer_text_surf, footer_text_rect)

    def draw(self):
        self.screen.fill(MENU_BACKGROUND_COLOR)
        self.screen.blit(self.logo, self.logo_rect.topleft)
        mouse_pos = pygame.mouse.get_pos()
        start_button_hover = self.start_button_rect.collidepoint(mouse_pos)

        self.draw_button(self.start_button_text, self.start_button_rect, start_button_hover)

        vertical_middle = (self.logo_rect.bottom + self.start_button_rect.top) // 2
        title_surface = self.title_font.render("QWANDLE", True, TEXT_COLOR)
        title_rect = title_surface.get_rect()
        title_top_position = vertical_middle - (title_rect.height // 2)
        title_rect.centerx = self.screen_rect.centerx
        title_rect.top = title_top_position

        self.screen.blit(title_surface, title_rect)

        self.draw_footer()

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.about_button_rect.collidepoint(event.pos):
                        self.show_about = not self.show_about
                    if self.start_button_rect.collidepoint(event.pos):
                        print("Start the game!")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("QWANDLE - Main Menu")
    main_menu = MainMenu(screen)
    main_menu.run()
