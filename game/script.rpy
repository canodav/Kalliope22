# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define applegate = Character("Applegate", color = "#e8ef27d9" )
define capitan = Character("Capitan", color = "#25c20dfd" )
define hollis = Character("Hollis", color = "#e13333fd")
define lespere = Character("Lespere", color = "#1474dafd")

#ESTILS PERSONATGES: ETIQUETA. 
style s_hollis is text:
    size gui.name_text_size
    color "#e13333fd"  

style s_lespere is text:
    size gui.name_text_size
    color "#1474dafd"  

style s_capitan is text:
    size gui.name_text_size
    color "#25c20dfd" 

style s_applegate is text:
    size gui.name_text_size
    color "#e8ef27d9"   

#AVATARS PERSONATGES
image lespere = "3.png"
image applegate = "2.png"
image capitan = "1.png"
image hollis = "4.png"

# BACKGROUND IMAGES
image space = "space.jpg"
image space_1 = "space_1.png"

#Reduir la mida del avatar.
transform set_hollis:
    xalign 0.65
    yalign 0.7
    zoom 0.5

transform set_lespere:
    xalign 0.85
    yalign 0.7
    zoom 0.5

transform set_capitan:
    xalign 0.05
    yalign 0.7
    zoom 0.5

transform set_applegate:
    xalign 1.05
    yalign 0.7
    zoom 0.5

# EFECTES: 
# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)
# Hold at black for a bit.
define fadehold = Fade(0.5, 1.2, 0.5)
# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 1.2, 0.5, color="#fff")


#VIDEOS INTRODUCCIÓ: 
image anim1 = Movie(channel="movie_dp", play = "ACTO1-2.ogv", loop = False)

######################################################################################################
# El juego comienza aquí.
label start:
    scene intro

    #Primera cinematica
    $ renpy.movie_cutscene("ACTO1-2.ogv")
    #fade efect
    with fade

    #Segunda cinematica
    show anim1
    "Lo tenemos. Ponemos rumbo de vuelta a casa. {w=2}{nw}"

    #fade final efect
    with fadehold

    jump t0


######################################################################################################
#label menu:


######################################################################################################

label t0:
    scene space_1
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show capitan at set_capitan
    #with moveinleft

    show hollis at set_hollis 
    show lespere at set_lespere 
    #with moveinright
    
    "{=s_lespere}Lespere: {/=s_lespere} Dios, estoy dando vueltas. -Alarma: *suena*{fast}"

    "{=s_lespere}Lespere: {/=s_lespere} Dios, estoy dando vueltas. -Alarma: *suena*{fast}
    \n\n{=s_hollis}Hollis: {/=s_hollis} Ho▃l█a? Alguien me░░ re░ibe?{fast}"

    hide lespere
    
    "\n\n{=s_hollis}Hollis: {/=s_hollis} Ho▃l█a? Alguien me░░ re░ibe?{fast}"

    hide hollis

    "{=s_capitan}Capitan: {/=s_capitan} Joder, cómo ha podido pasar esto. ¿Alguien me recibe?{fast}"

    show applegate at set_applegate
    
    "{=s_capitan}Capitan: {/=s_capitan} Joder, cómo ha podido pasar esto. ¿Alguien me recibe?{fast}
    \n\n{=s_applegate}Applegate: {/=s_applegate} Aa█aaa░█aaa██░█aa"

    hide applegate

    show lespere at set_lespere
    lespere "¿Capitán? ¿Applegate? ¿Woode?"

    show applegate at set_applegate
    "{=s_lespere}Lespere: {/=s_lespere} ¿Capitán? ¿Applegate? ¿Woode?{fast}
    \n\n{=s_applegate}Applegate: {/=s_applegate} fjnagmjsimg—-------"

    hide applegate

    show hollis at set_hollis

    hollis "Un po█co mal, pe█ro te escucho"
    
    capitan "te escucho! Te escucho!"

    hide hollis

    show lespere at right

    lespere "¿Me recibes?"

    hide lespere

    show hollis at right

    hollis "¿Mejor?"

    menu t0_1:
        "Que contestas"

        "Sí, Lespere, te recibo":
            jump capitan_lespere_1

        "Ahora, Hollis, ya te escucho bien":
            jump capitan_hollis_1

    return

label capitan_lespere_1:

    menu capitan_lespere_q0:
        lespere "Ha habido un accidente"

        "¿Un accidente? ¿Qué ha pasado?":
            lespere "Claramente, ha habido un accidente no te parece?"
        
        "¿Como que un accidente?":
            lespere "Claramente, ha habido un accidente no te parece?"
        
    menu capitan_lespere_q1:
        lespere "Claramente ha habido un accidente ¿No te parece?"

        "Joder ¿Tu sabes algo?":
            jump captain_lespere_2

        "¿Como ha podido pasar?":
            jump captain_lespere_3

label captain_lespere_2:

    menu captain_lespere_2_q0:
        lespere "Contacte con usted para advertirle"
        
        "¿Advertirme de que?":
            lespere "Yo vi que el laboratorio havia algo que no estaba bien"

        "¿Que dices?":
            lespere "Vi que el laboratorio havia algo que no estaba bien"


label captain_lespere_3:
    menu captain_lespere_3_q0:
        lespere "Menuda mierda, estamos jodidos"

        "Calmate":
            lespere "Calmate tu gilipollas, donde estavas tu que no respondiste?"

        "Algo me dice que tu has tenido algo que ver":
            lespere "Vi que el laboratorio havia algo que no estaba bien"

    return

label capitan_hollis_1:
    
    menu capitan_hollis_q0:
        hollis "¿Estas bien? ¿Creo que nadie ha tenido tiempo de ponerse el anclaje?"

        "Ha pasado todo demasiado rapido. No entiendo nada":
            jump capitan_hollis_2
        "No pensamos en eso ahora mismo. ¿vale? Necesitamos soluciones":
            hollis "Nos vamos a morir!!!!!!!!!"
            return
    
    return

label capitan_hollis_2:

    menu capitatan_hollis_q1:
        hollis "Creo que nos ha dado un meteorito. ¡¡Joder!!"

        "Respirar, alterarte drenara tu oxigeno":
            hollis "Dejame, ¿Ahora si te preocupa mi oxigeno?"
            capitan "Anda calla tontito"

        "No vi nada, se estaba reparando el sensor todavia":
            hollis "Podriamos no haber tenido que repararlo en primer lugar"
            capitan "¿A que te refieres?"
    


