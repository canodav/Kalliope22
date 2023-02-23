# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define a = Character("Applegate")
define c = Character("Capitan")
define h = Character("Hollis")
define l = Character("Lespere")
image l = "l.jpeg"
image a = "a.jpeg"
image c = "c.jpeg"
image space = "space.jpg"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene space

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show a at left


    # Presenta las líneas del diálogo.

    a "Aquí AG otra vez. Hablemos no podemos hacer más da igual lo que haya pasado."

    show c at right

    c "¡Nos vendrán a recoger! Nos encontrarán tarde o temprano."

    a "Capitán, ¿por qué no se calla?"
    c "Que?"
    a "Ya me ha oído, capitán. No pretenda imponerme su rango, porque nos separan quince mil kilómetros y no tenemos que engañarnos."
    c "¡Compórtese, Applegate!"

    a "No quiero. Esto es un motín de uno solo. No tengo una maldita cosa que perder. Su nave era mala, usted un mal capitán, y espero que se ase cuando llegue al Sol."
    c "¡Le ordeno que se calle!"
    a "Adelante, vuelva a ordenarlo"
    c "..."
    a "Quiero confesarte algo, Capitan. Algo que te hará feliz. Fui uno de los que votaron contra ti en la Rocket Company, hace dos años."
    a "Ah, sí y otra cosa. También te odio a ti, Hollis (FLASHBACK?). Pero tú ya lo sabes. Hace mucho tiempo que lo sabes."




    # Finaliza el juego:

    return
