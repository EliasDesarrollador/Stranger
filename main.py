
#main.py
# Archivo principal del juego 
from game.game import Game

if __name__ == "__main__":
    #Crear instancia del juego 
    juego = Game()
    #Ejecutar el juego 
    juego.run()