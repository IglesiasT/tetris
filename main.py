import tetris
import gamelib
import interfaz_grafica

ESPERA_DESCENDER = 8

def main():
    # Inicializar el estado del juego
    gamelib.resize(650, 550)

    juego = tetris.crear_juego(tetris.generar_pieza())

    timer_bajar = ESPERA_DESCENDER
    
    while gamelib.loop(fps=30):
        #Dibujar interfaz gráfica 
        gamelib.draw_begin()
        
        gamelib.title('Tetris ++')        
        interfaz_grafica.mostrar_controles()
        interfaz_grafica.mostrar_grilla(juego)
        interfaz_grafica.mostrar_pieza_actual(juego)
        interfaz_grafica.mostrar_siguiente_pieza()

        gamelib.draw_end()

        for event in gamelib.get_events():
            if not event:
                break
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key
              
            # Actualizar el juego, según la tecla presionada 
            juego = tetris.procesar_teclas(juego, tecla)
            
        
        timer_bajar -= 1
        if timer_bajar == 0:
            timer_bajar = ESPERA_DESCENDER
            # Descender la pieza automáticamente
            
    

gamelib.init(main)