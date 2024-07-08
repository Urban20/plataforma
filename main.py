import pygame
import objetos
import imagenes
import time
pygame.init()

tiempo_juego= time.time()
tiempo = pygame.time.Clock()


resolucion= (900,500)

pantalla = pygame.display.set_mode(resolucion)

fondo = pygame.image.load('fondo.png')

while True:
    try:
        
        teclas= pygame.key.get_pressed()
        pantalla.blit(fondo,(0,0))
        
        #colision personaje- suelo -----------------------------------------------------------
        for plataforma in imagenes.plataformas:
            
            
           
                plataforma.generar()
                if objetos.personaje.hitbox().colliderect(plataforma.generar()):
                        
                        objetos.personaje.posy = plataforma.posy - 132
                        objetos.personaje.suelo = True
                        objetos.personaje.salto(teclas,objetos.personaje.suelo)
                else:
                    objetos.personaje.suelo = False
                    objetos.personaje.salto(teclas,objetos.personaje.suelo)
                    objetos.personaje.gravedad()
                
                
                print(pygame.mouse.get_pos())
            #colision personaje- suelo -----------------------------------------------------------

            #colision enemigo-suelo--------------------------------------------
            
                if objetos.enemigo.hitbox().colliderect(plataforma.generar()):
                    objetos.enemigo.posy = plataforma.posy - 130  
                else:
                    if objetos.enemigo.posx > 0 and objetos.enemigo.posx < objetos.pantallax:

                        objetos.enemigo.gravedad()
                


        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT:
                pygame.quit()
        
        
        
        #jugador----------------
        

        objetos.camara.seguir(objetos.personaje.animacion(teclas),teclas)
        #para que vuelva en caso de que se caiga del mapa
        if objetos.personaje.posy > objetos.pantallay:
            objetos.personaje.posx = objetos.suelo1.posx
            objetos.personaje.posy= 0

        #disparar bolas de fuego
        cooldown= time.time()
       
        if teclas[pygame.K_e] and cooldown - tiempo_juego > 0.5:
            
            bola = objetos.Bola_Fuego()
            objetos.proyectiles.append(bola)
            tiempo_juego = cooldown
        for bola in objetos.proyectiles:
            bola.generar()
            bola.desplazamiento()
            
            if bola.posx > objetos.pantallax or bola.posx < 0:
                objetos.proyectiles.remove(bola)
            
           
                 

        #jugador----------------

        #enemigo----------------
        for enemigo in imagenes.enemigos:
            enemigo.hitbox()
            enemigo.animacion()
            enemigo.target()
            enemigo.ataque()
            enemigo.daño()
          
        
        #enemigo----------------
       
        
        pygame.display.flip()
        tiempo.tick(60)
    except pygame.error:
        pass