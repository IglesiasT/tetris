"""Lo importante es que se pueda ver el estado del juego y la proxima pieza a salir"""

import gamelib
import tetris

#Coordenadas de la grilla en pixeles JUGAR CON DIMENSIONES()
x1 = 50
y1 = 100
x2 = 350
y2= 500 

def mostrar_grilla(juego):
    """
    Implementación gráfica de la grilla.
    """

    grilla, _ = juego
    
    #Bordes
    gamelib.draw_text('TETRIS', 200, 50, size=26) #Título del juego en pestaña
    gamelib.draw_rectangle(x1, y1, x2, y2)

    #Superficie

def mostrar_pieza_actual(juego):
    """
    Recibe la pieza actual en forma de tupla de tuplas y la muestra en la grilla.
    """
    
    _, pieza = juego

    for coordenada in pieza:
        gamelib.draw_rectangle(x1*(coordenada[0] + 1), y1*(coordenada[1] + 1), x1*(coordenada[0] + 2), y1*(coordenada[1] + 2))

def mostrar_siguiente_pieza():
    """
    Dibuja la siguiente pieza en un recuadro.
    """

    #Dibujar recuadro
    gamelib.draw_rectangle(400, 100, 600, 300, outline='white', fill='black')
    gamelib.draw_text('Siguiente pieza', 500, 120, size=15)
    
    #Dibujar siguiente pieza
    
def mostrar_controles():
    """
    Dibuja un recuadro y varios textos con la funcionalidad de cada tecla
    """

    #Dibujar recuadro
    gamelib.draw_rectangle(400, 300, 600, 500, outline='white', fill='black')
    
    #Controles LEER CON UN FOR TECLAS.TXT? CAMBIAR LOS  POR LA MITAD DEL RECUADRO
    gamelib.draw_text('Controles', 500, 320, size=15)
    gamelib.draw_text('W = Rotar', 500, 360, size=12)
    gamelib.draw_text('A = Izquierda', 500, 380, size=12)
    gamelib.draw_text('S = Derecha', 500, 400, size=12)
    gamelib.draw_text('D = Descender', 500, 420, size=12)
    gamelib.draw_text('G = Guardar partida', 500, 440, size=12)
    gamelib.draw_text('C = Cargar partida', 500, 460, size=12)
    gamelib.draw_text('Esc = Salir', 500, 480, size=12)