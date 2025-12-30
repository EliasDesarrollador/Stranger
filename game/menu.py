
# game/menu.py
import pygame
import sys
from config import ANCHO, ALTO, FPS

class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()
        self.running = True

        # Cargar imagen del menu
        self.imagen = pygame.image.load(
            "assets/images/intro.png"
        ).convert_alpha()

        # Ajustar imagen al tamaño de la ventana
        self.imagen = pygame.transform.scale(
            self.imagen, (ANCHO, ALTO)
        )

    def run(self):
        """Bucle del menu"""
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Presionar ENTER para empezar
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        self.running = False

            # Dibujar menu
            self.pantalla.blit(self.imagen, (0, 0))
            pygame.display.update()
            self.reloj.tick(FPS)
