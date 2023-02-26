# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define applegate = Character("Applegate")
define capitan = Character("Capitan")
define hollis = Character("Hollis")
define lespere = Character("Lespere")
image lespere = "3.png"
image applegate = "2.png"
image capitan = "1.png"
image hollis = "4.png"
image space = "space.jpg"


# El juego comienza aquí.

image video_intro = Movie(play="ACTO1-2.mp4", size=(1920, 1080))

label start:

    show video_intro:
        xpos 0 ypos 0

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene space

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show capitan at left

    show lespere at right

    lespere "Dios, estoy dando vueltas. -Alarma: *suena*"

    hide lespere

    show hollis at right

    hollis "Ho▃l█a? Alguien me░░ re░ibe?"

    capitan "Joder, cómo ha podido pasar esto. ¿Alguien me recibe?"

    hide hollis

    show applegate at right

    applegate "Aa█aaa░█aaa██░█aa"

    hide lespere

    show lespere at right

    lespere "¿Capitán? ¿Applegate? ¿Woode?"

    hide lespere

    show applegate at right

    applegate "fjnagmjsimg—-------"

    hide applegate

    show hollis at right

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
    "NO DISPONIBLE"

    return