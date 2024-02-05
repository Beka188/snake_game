import pygame


class MainScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Snake Game Menu", True, (255, 255, 255))
        self.start_text = self.font.render("Press SPACE to start", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "game"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title_text, (200, 200))
        screen.blit(self.start_text, (200, 300))
        pygame.display.update()