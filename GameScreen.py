import pygame


class GameScreen:
    def __init__(self):
        self.player = pygame.Rect(250, 300, 10, 10)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), self.player)
        pygame.display.update()
