import pygame
import sys

# --- Configuration ---
WIDTH, HEIGHT = 1280, 720
BG_COLOR = (30, 30, 30)   # Dark background for high-contrast "ink"
INK_COLOR = (0, 255, 150) # Neon green for that "tech" look
BRUSH_SIZE = 5

class Slate:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Transparent Slate Prototype")
        self.canvas = pygame.Surface((WIDTH, HEIGHT))
        self.drawing = False
        self.last_pos = None

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Handle Mouse/Touch Input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3: # Right click to clear
                    self.canvas.fill((0, 0, 0))
                else:
                    self.drawing = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
                self.last_pos = None

            if event.type == pygame.MOUSEMOTION and self.drawing:
                current_pos = event.pos
                if self.last_pos:
                    pygame.draw.line(self.canvas, INK_COLOR, self.last_pos, current_pos, BRUSH_SIZE)
                self.last_pos = current_pos

    def run(self):
        while True:
            self.process_events()
            self.screen.fill(BG_COLOR)
            # Blit the drawing canvas onto the main screen
            self.screen.blit(self.canvas, (0, 0))
            pygame.display.flip()

if __name__ == "__main__":
    slate = Slate()
    slate.run()
