
# game/menu.py
import pygame
import sys
from config import ANCHO, ALTO, FPS

class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()
        self.running = True

        # Inicializar musica 
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/Kyle Dixon & Michael Stein - Kids - Intensive Drops Network.mp3")
        pygame.mixer.music.play(-1) # Reproducir en bucle 
        try:
            self.imagen = pygame.image.load(
                "assets/menu/intro.png"   # ruta 
            ).convert()

            self.imagen = pygame.transform.scale(
                self.imagen, (ANCHO, ALTO)
            )

        except Exception as e:
            print("ERROR cargando imagen del menu:", e)
            pygame.quit()
            sys.exit()

    def run(self):
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        self.running = False
                        pygame.mixer.music.stop() # para la musica al empezar el juego 

            self.pantalla.fill((0, 0, 0))
            self.pantalla.blit(self.imagen, (0, 0))
            pygame.display.flip()
            self.reloj.tick(FPS)
