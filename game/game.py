
# Archivo de mecanica del juego 
import pygame
import sys
from config import ANCHO, ALTO, FPS, NEGRO
from entities.player import Player 
from entities.enemy import Enemy
 
class Game:   
    def __init__(self):
        pygame .init()
        #Crear ventana del juego 
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Stranger Things - Upside Down")
        #Reloj para controlar FPS 
        self.reloj = pygame.time.Clock()

        #Control del bucle principal 
        self.running = True
        #Crear objetos del juego 
        self.player  = Player(380, 500)
        self.enemy = Enemy (200, 200)

    def eventos (self):
        """Maneja eventos (cerrar ventana, teclado, etc)"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False
                
    def  actualizar (self):
        """Actualiza la logica del juego """
        self.player.update()
        self.enemy.update()
    
    def dibujar(self):
        """Dibuja todos los elementos en la pantalla"""
        self.pantalla.fill(NEGRO)

        self.player.draw(self.pantalla)
        self.enemy.draw(self.pantalla)

        pygame.display.update()


    def run(self):
        """Bucle principal del juego"""
        while self.running:
            self.eventos()
            self.actualizar()
            self.dibujar()

            #Limitar FPS 
            self.reloj.tick(FPS)
