import pygame

pygame.init()

blanco =(255,255,255)
negro=(0,0,0)
marron = (53, 51, 51)
marron_piso= (111, 77, 82 )
verde = (34, 205, 0 )
rojo = (217, 15, 15 )

#personaje----------------
corriendo_derecha= []
corriendo_izq= []

#personaje----------------
enemigos_sprite= pygame.sprite.Group()
#objetos del mapa-------------
plataformas =[]
enemigos= []
#objetos del mapa-------------
#enemigo----------------------
#caminar
enemigo_izq=[]
enemigo_der = []
#atacar
ataque_izq =[]
ataque_der = []
#daño
daño_izq_enemigo=[]
daño_der_enemigo=[]
#enemigo----------------------


#imagenes del jugador----------------------------------------------------------------------------
#quieto en derecha
personaje_quieto= pygame.image.load('quieto.png')
personaje_quieto.set_colorkey(blanco)
#quieto en izq
personaje_quieto2= pygame.image.load('quieto2.png')
personaje_quieto2.set_colorkey(blanco)



for x in range(1,7):
            jugador_derecha = pygame.image.load(f'jugador derecha/{x}.PNG')
                
            jugador_derecha.set_colorkey(blanco)
            corriendo_derecha.append(jugador_derecha)
                
                
                
for x in range(1,7):
        jugador_izq = pygame.image.load(f'jugador izq/{x}.PNG')
                
        jugador_izq.set_colorkey(blanco)
        corriendo_izq.append(jugador_izq)

#bola a la derecha
bola_de_fuego= pygame.image.load('bola fuego.png')
bola_de_fuego.set_colorkey(blanco)
#bola a la izq
bola_de_fuego2= pygame.transform.flip(bola_de_fuego,True,False)
bola_de_fuego2.set_colorkey(blanco)

#imagenes del jugador----------------------------------------------------------------------------
#imagenes enemigo--------------------------------------------------------------------------------
for x in range(1,6):
        #enemigo desde izq
        caminar_izq= pygame.image.load(f'enemigo/caminar/caminar_izq/caminar{x}.PNG')
        enemigo_izq.append(caminar_izq)

        #enemigo desde der
            
        caminar_der= pygame.image.load(f'enemigo/caminar/caminar_der/caminar{x}.PNG')
        enemigo_der.append(caminar_der)
            
for x in range(1,4):
        ataq_izq= pygame.image.load(f'enemigo/ataque/izq/ataque{x}izq.PNG')
        ataque_izq.append(ataq_izq)
        ataq_der = pygame.image.load(f'enemigo/ataque/der/ataque{x}der.PNG')
        ataque_der.append(ataq_der)
#daño-------------------------
for x in range(1,3):
        daño_izq= pygame.image.load(f'enemigo/daño/daño{x}.png')
        daño_izq_enemigo.append(daño_izq)

daño_der = pygame.transform.flip(daño_izq_enemigo[0],True,False)

#imagenes enemigo--------------------------------------------------------------------------------


