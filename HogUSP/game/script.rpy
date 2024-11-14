# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ny = Character("Nicoly Nicoly", color="f1208c")
define N1 = Character("Nicoly", color="ff82ba")
define Da = Character("Dario", color="ffbe0b")
define Narrador = Character(color="000000")



# The game starts here.

label start:

    scene bg dark
    
    Narrador "Tudo está completamente escuro. Linhas, praticamente invisíveis, moldam o formato de uma caneta e um caderno."

    Narrador "No entanto… o formato rapidamente se desfaz."
    
    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "OMG, UAU! Que lugar é esse?"

    show dario_full1

    Da "De boa, zé soninho? Cuidado que camarão que dorme a onda leva!!!"
    Da "Amigo, caraca… Você dormiu pesado, hein? Até babou na mesa."
    Da "Relaxa que teu amigo Dario tem lencinho. Tô sempre aqui pra te ajudar!"
    Da "Ihhh, nem me apresentei, sou o teu amigo Dario. Se não ficou claro, né! Hahahaha!"


    "Dario pega um lenço de sua mochila cheia de pins de diferentes cores e brilhos."
    "Nesse tempo todo, o Dario não parou de sorrir. Ele está se esforçando muito para ser legal com você."

    Da "Opa, toma aí, amigo!"
    Da "Depois de uma dormida dessa, aproveitando que nós tamo aqui, queria te fazer uma proposta."
    Da "Agora temos o clube de futebol 2! É um esporte novo que tá bem na moda."
    Da "Reitero que hoje à tarde tem treino. Queria saber se você tá afim de –"

    hide dario_full1

    Ny "You've created a new Ren'Py game."

    Ny "You can add new scenes to script.rpy."

    hide nyc_full1 
    show dario_full1

    Da "Once you add a story, pictures, and music, you can release it to the world!"

    Da "Da hora"

    menu:
        Da "DARIO DARIO DARIO DARIO"
        "Escolher frase 1":
            Ny "Você escolheu a primeira frase."
        "Escolher frase 2":
            Ny "Você escolheu a segunda frase."
        "Escolher frase 3 muito longaaaaa":
            Ny "nYPI"

    # This ends the game.

    return
