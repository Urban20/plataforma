import pygame,time,imagenes,random
pygame.init()



altura_piso = 472
personaje_quieto = True
#memoria-----------------------
ult_tecla= []
proyectiles=[]
ult_pos = []
#memoria-----------------------

pantallax = 900
pantallay = 500

resolucion= (pantallax,pantallay)
pantalla = pygame.display.set_mode(resolucion)


class Entidades():
    def __init__(self,posx,posy,velx,vely,salud):
        self.posx = posx
        self.posy= posy
        self.velx = velx
        self.vely= vely
        self.suelo = False
        self.salud = salud
        
    def hitbox(self):
        hitbox_=pygame.Rect(self.posx,self.posy,90,130)
        return hitbox_
    def gravedad(self):
        
        if self.suelo == False:
            
            self.posy += 5
    def daño(self,status):
        
        if status:
            self.salud -= 1
    def muerte(self):
        pass 



class Jugador(Entidades):
    def __init__(self,posx,posy,velx,vely,salud):
        super().__init__(posx,posy,velx,vely,salud)
        



    def animacion(self,teclas):
        if teclas[pygame.K_d]:
            ult_tecla.clear()
            fotograma = int(time.time()* 10) % 6
            pantalla.blit(imagenes.corriendo_derecha[fotograma],(self.posx,self.posy))
            self.posx += self.velx
            ult_tecla.append('d')
           
            
        elif teclas[pygame.K_a] :
            ult_tecla.clear()
            fotograma = int(time.time()* 10) % 6
            pantalla.blit(imagenes.corriendo_izq[fotograma],(self.posx,self.posy))
            self.posx -= self.velx
            ult_tecla.append('a')
            
            
        else:
            ult_pos.clear()
            if 'd' in ult_tecla:
                
                quieto_der =pantalla.blit(imagenes.personaje_quieto,(self.posx,self.posy))
                ult_pos.append(quieto_der)
                
            elif 'a' in ult_tecla:
                quieto_izq= pantalla.blit(imagenes.personaje_quieto2,(self.posx,self.posy))
                ult_pos.append(quieto_izq)
            else:
                quieto_der= pantalla.blit(imagenes.personaje_quieto,(self.posx,self.posy))
                ult_pos.append(quieto_der)
                

    def salto(self,teclas,status):
        self.suelo = status
        
        if self.suelo == True and teclas[pygame.K_SPACE]:
            
            self.posy -= 200
        
    def atacar(self,teclas,tiempo_juego):
        #disparar bolas de fuego
        cooldown= time.time()
       
        if teclas[pygame.K_e] and cooldown - tiempo_juego > 0.5:
            
            bola = Bola_Fuego()
            proyectiles.append(bola)
            tiempo_juego = cooldown
        for bola in proyectiles:
            bola.generar()
            bola.desplazamiento()
            
            if bola.posx > pantallax or bola.posx < 0:
                proyectiles.remove(bola)



class Material:
    def __init__(self,posx,posy,largo,ancho):
        self.posx = posx
        self.posy = posy
        self.largo = largo
        self.ancho = ancho
    def generar(self):
        suelo= pygame.draw.rect(pantalla,(99, 63, 180 ),(self.posx,self.posy,self.largo,self.ancho))
        
        return suelo


class Camara:
    def __init__(self):
        #limite derecha
        self.limite_x_der = (resolucion[0] - personaje.posx) / 2
        self.limite_x_izq = personaje.posx 
        self.vel_camara = 5

    def seguir(self,pj_quieto,teclas):
        #para la derecha
        if personaje.posx >= self.limite_x_der and not pj_quieto and teclas[pygame.K_d]:
            personaje.posx = self.limite_x_der
            for plataforma in imagenes.plataformas:
                plataforma.posx -= self.vel_camara
            for enemigo in imagenes.enemigos:
                enemigo.posx -= self.vel_camara

        #para la izquierda
        if personaje.posx <= self.limite_x_izq and not pj_quieto and teclas[pygame.K_a]:
            personaje.posx = self.limite_x_izq
            for plataforma in imagenes.plataformas:
                plataforma.posx += self.vel_camara
            for enemigo in imagenes.enemigos:
               
                enemigo.posx += self.vel_camara
                
                


class Bola_Fuego:
    def __init__(self):
        self.imagen= imagenes.bola_de_fuego
        self.imagen2= imagenes.bola_de_fuego2
        self.velx = 7
        self.vely = 7
        self.posx = personaje.posx + 90
        self.posy = personaje.posy + 45
    def generar(self):
        if personaje.posx < enemigo.posx:
            pantalla.blit(self.imagen,(self.posx,self.posy))
        else:
            pantalla.blit(self.imagen2,(self.posx,self.posy))

    def desplazamiento(self):
        if personaje.posx < enemigo.posx:
            self.posx += self.velx
            self.posy -= self.vely
            if self.posy <= personaje.posy - 25 or self.posy > personaje.posy + 130:
                
                self.vely *= -1
        else:
            
            self.posx -= self.velx
            self.posy -= self.vely
            if self.posy <= personaje.posy - 25 or self.posy > personaje.posy + 130:
                
                self.vely *= -1
        
    def hitbox(self):
        hitbox= pygame.Rect(self.posx,self.posy,32,20)
        return hitbox









class Enemigo(Entidades):
    def __init__(self,posx,posy,velx,vely,salud):
        super().__init__(posx,posy,velx,vely,salud)

        self.caminando = True
        
    def ataque(self):
        fotograma = int(time.time()* 5) % 3
        #ataque por derecha----------------------------------------------------
        
        if personaje.posx < self.posx and self.posx - personaje.posx <= 90:
            pantalla.blit(imagenes.ataque_der[fotograma],(self.posx,self.posy))
                
            #IMPLEMENTAR ALGUNA MECANICA QUE ME PERMITA USAR MAS ADELANTE PARA QUITARLE VIDA AL JUGADOR

            #ataque por izq---------------------------------------------------------
        elif personaje.posx > self.posx and personaje.posx - self.posx <= 90:
            pantalla.blit(imagenes.ataque_izq[fotograma],(self.posx,self.posy))
            

    def animacion(self):

        if self.caminando:
        #caminar----------------------------------
            try:
                fotograma = int(time.time()* 5) % 5
                if personaje.posx < self.posx and self.posx - personaje.posx > 90:
                    pantalla.blit(imagenes.enemigo_izq[fotograma],(self.posx,self.posy))
                    
                elif personaje.posx > self.posx and personaje.posx - self.posx > 90:
                    pantalla.blit(imagenes.enemigo_der[fotograma],(self.posx,self.posy))
                    
            except IndexError:
                pass


    def target(self):
        #derecha
        if personaje.posx + 90 < self.posx and self.posx < pantallax:
            self.posx -= self.velx

        #izquierda
        elif personaje.posx - 90> self.posx and self.posx >  - 80:
            self.posx += self.velx
    def daño(self):
        for bola in proyectiles:
            for enemigo in imagenes.enemigos:
                enemigo.salud -= 1
                # si enemigo.salud es mayor que 0:
                if bola.hitbox().colliderect(enemigo.hitbox()) and personaje.posx < enemigo.posx:
                    enemigo.caminando = False 
                    pantalla.blit(imagenes.daño_izq_enemigo[0],(enemigo.posx,enemigo.posy))
                elif bola.hitbox().colliderect(enemigo.hitbox()) and personaje.posx > enemigo.posx:
                    enemigo.caminando = False 
                    pantalla.blit(imagenes.daño_der,(enemigo.posx,enemigo.posy))
                
                else:
                    enemigo.caminando = True

                #IMPLEMENTAR MUERTE DEL ENEMIGO

#objetos----------------------------------------------------
personaje = Jugador(posx=250,posy=0,velx=5,vely=5,salud=3)
suelo1 = Material(0,473,900,50)
suelo2 = Material(posx=50,posy=200,largo=100,ancho=10)
suelo3= Material(pantallax + 50,473,200,10)


distancia_suelo3 = pantallax + 50

suelo3= Material(distancia_suelo3,473,200,10)
distancia_suelo3 += 100
imagenes.plataformas.append(suelo3)

imagenes.plataformas.append(suelo1)
imagenes.plataformas.append(suelo2)

for x in range(1,4):
    vel = random.choice([0.5,1,1.5])
    enemigo = Enemigo(posx=random.randint(5, pantallax - 50),posy=altura_piso - 130,velx= vel,vely=vel,salud=3)
    imagenes.enemigos.append(enemigo)
    

camara = Camara()
#objetos----------------------------------------------------
