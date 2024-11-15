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

# Parte dos diálogos já escritos ta aqui, só faltam todo o resto
# mudança de personagens, etc...

# define Nar = Character()
# define vc = Character("Você")
# define NY = Character("Nycole")
# define dar = Character("Dario")
# define unknownNY = Character("???", color="#f30cc1")
# define unknownLu = Character("???", color="#db8708")

# # define fade_in = Fade(3.0)
# # transform custom_flash(duration=0.5, color="#ff5781", alpha=0.8):
# #     # Set the initial color and opacity
# #     on show:
# #         # Start from transparent
# #         alpha 0.0
# #         # Fade to the specified color and alpha
# #         linear duration alpha
# #         # Quickly fade back out
# #         linear duration 0.0


# # The game starts here.

# label start:

#     scene bg dark

#     Nar "Tudo está completamente escuro. Linhas, praticamente invisíveis, moldam o formato de uma caneta e um caderno."

#     Nar "No entanto… o formato rapidamente se desfaz."

#     vc "O que está... acontecendo?"

#     Nar "Você é um aluno na Alta Academia de Magia. Embora não seja um ótimo aluno, você se dedicou muito para chegar aqui."

#     scene bg school with fade

#     vc "É verdade, eu estudei muito. Ainda tenho muito a aprender."

#     Nar "Muitas gerações de poderosos magos passaram por aqui. Magos de transmutação, de emoções, de sabedoria…"

#     Nar "E você ainda não tem nenhuma especialidade."

#     Nar "Mas onde você estava antes de estar aqui? O que você estava fazendo?"

#     vc "Acho que… eu estava…"

#     vc "Eu estava na sala de aula."

#     Nar "Sim. É verdade. Era uma aula de…"

#     Nar "…"

#     Nar "Deve ser difícil lembrar. Afinal, você dormiu a aula toda."

#     vc "Não! Eu preciso ir bem nesta matéria. Senão vou ser expulso!!!"

#     vc "Por favor, me deixe acordar!"

#     Nar "…"

#     Nar "Ninguém responde. Você está sozinho em um vazio infinitamente plástico. Exceto… por uma pequena fonte de luz."

#     # show expression Solid(color="#ff5781") as custom_flash

#     scene bg red_class

#     unknownNY "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

#     unknownNY "Vê se você acha nesse livro onde nós ainda somos amigas!"

#     Nar "A garota arremessa o livro na direção de uma garota na sala."

#     unknownLu "Ny… o que você tá… !!!"

#     # show expression Solid(color="#ff5781") as custom_flash

#     scene bg class

#     Nar "Você acorda, sentado na sua mesa."

#     vc "Puts, passei a aula inteira dormindo de novo…"

#     vc "Mas hoje eu sonhei. Foi meio… estranho?"

#     dar "De boa, zé soninho? Cuidado que camarão que dorme a onda leva!!!"
#     dar "Amigo, caraca… Você dormiu pesado, hein? Até babou na mesa."
#     dar "Relaxa que teu amigo Dario tem lencinho. Tô sempre aqui pra te ajudar!"
#     dar "Ihhh, nem me apresentei, sou o teu amigo Dario. Se não ficou claro, né! Hahahaha!"

#     Nar "Dario pega um lenço de sua mochila cheia de pins de diferentes cores e brilhos."
#     Nar "Nesse tempo todo, o Dario não parou de sorrir. Ele está se esforçando muito para ser legal com você."

#     dar "Opa, toma aí, amigo!"
#     dar "Depois de uma dormida dessa, aproveitando que nós tamo aqui, queria te fazer uma proposta."
#     dar "Agora temos o clube de futebol 2! É um esporte novo que tá bem na moda."
#     dar "Reitero que hoje à tarde tem treino. Queria saber se você tá afim de —"

#     Nar "Uma moça muitíssimo bem arrumada e produzida chuta a porta, abrindo ela com um estouro."

#     dar "Ishhh, meu Gandalf!"
#     dar "O que será agora?"

#     NY "LUNA! Sua ordinária. Foi VOCÊ que colocou esse bilhete no meu armário!"

#     unknownLu "Mas… Ny, eu…. eu só tô lendo fanfic…"

#     NY "Atitude típica de lacraia. Sua básica! Ainda fica se fazendo de vítima?"
#     NY "Só VOCÊ saberia a senha do meu armário. E fica colocando bilhetes nele como se a gente ainda fosse amiga?"

#     unknownLu "Mas Ny… você me disse que confiava em mim para —"

#     NY "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

#     vc "Espera… eu já ouvi isso antes…"

#     NY "Vê se você acha nesse livro onde nós ainda somos amigas!"

#     unknownLu "Ny… o que você tá… !!!"

#     Nar "Nycole arremessa um livro-ciclista com a força de uma diva revoltada."
#     Nar "BLAM!"
#     Nar "O impacto é ouvido por todos, e a sala inteira se levanta para observar o estado da Luna."

#     Nar "Luna fica toda coitada no chão."
#     Nar "O livro, para a surpresa de ninguém, era um ciclista. Ele se levanta e imediatamente começa a pedalar."

#     zoe "Foi mal, tô atrasado."

#     Nar "Zoen sai de cena rapidamente."

#     Nar "Após este evento completamente lógico e racional, todos olham para Luna."
#     Nar "Ela está completamente imóvel, mas faz um som estranho, parecido com um cachorro triste."

#     unknownLu "Hyuummmm… :("

#     Nar "Laura aparece, lentamente. Ela levanta a câmera fotográfica e diz:"

#     laura "…"

#     Nar "Laura fotografa o estado de Luna."

#     Nar "A garota tira uma foto da Luna e sai da sala, lentamente."

#     dar "Damn, Luna! Você sabe que não dá pra responder ela."
#     dar "A Nicoly é uma chata. Mas o look dela tava um arraso hoje."

#     unknownLu "Hyuummmmmmmmmmmmmmmmm… :("

#     dar "Respira amiga… Coitada… Toma, eu tenho um feitiço de ibuprofeno pra você!"

#     Nar "Dario retira um pedaço de papel azul com runas da mochila."
#     Nar "Ao colocá-lo na cabeça de Luna, o papel brilha."
#     Nar "Luna para de gemer e se levanta, ainda triste."

#     unknownLu "O-Obrigada, Dario. Vou voltar a ler a minha fanfic de Parry Hotter…"

#     menu:
#         dar "Interrompeu a gente amigo! Tá chocado? Nunca viu a Nycole tendo um piripaque?"
#         "Eu acho que acabei de prever o futuro…":
#             jump opcaoA
#         "Já vi sim, só achei estranha a situação.":
#             jump opcaoB
#         "O livro era um ciclista?":
#             jump opcaoC

#     label opcaoA:
#         dar "sh, ficou lelé? Não tem nenhum mago na academia capaz de ver o futuro."
#         dar "Dúvido que tenha algum hoje, até teve no passado. Mas ele ficou maluquinho. E você parece normal pra mim!"
#         dar "Ah, de qualquer forma, tem informações sobre isso na biblioteca."
#         jump afterOpcao
#     label opcaoB:
#         dar "Ora, a única coisa estranha nessa história é a Luna ler Parry Hotter. Ela não sabe que é tudo mentira?"
#         dar "Depois eu devesse levar ela na enfermagia (sim enfermagia), mas ela parece bem."
#         dar "Ah, essas duas, costumavam estar tão juntos, agora…"
#         jump afterOpcao
#     label opcaoC:
#         dar "Ou! Nossa, amigo. Ainda tá acordando?"
#         dar "Do Zoen que tu perguntou? Ele é o estudante de transmutação. Consegue se transformar em tudo. Esqueceu?"
#         dar "Assim, é completamente lógico e racional que ele vire um livro em seu tempo livre."
#         jump afterOpcao

#     label afterOpcao:
#         dar "Retornando, a nossa conversa…"
#         dar "Impossível essa escola passar um dia sem drama… Ai ai."
#         dar "O bom é que essa vai ser a fofoca do dia!"
#         dar "Depois dessa, não acho que vá rolar algo bombástico nas próximas horas que supere a Nycole armando um barraco…"
#         dar "Ah, mas isso é muito improvável!"
#         dar "Realmente… Enfim, queria te perguntar se você gostaria de participar do clube de Fut 2!"
#         dar "Importante: Eu sou o capitão, e posso te mostrar como funciona tudinho!"
#         dar "O ruim é que é um pouco cansativo ser o capitão, o melhor aluno da sala e a pessoa mais simpática da escola!"

#         Nar "Pela primeira vez, você vê o Dario parar de sorrir por um segundo. Mas dura pouco."

#         dar "Deixando isso de lado, eu amo muito tudo o que faço! Não trocaria por nada."
#         dar "Antes de você dizer sim ou não pra proposta, deixa eu te explicar como funciona o jogo inteirinho!"
#         dar "Regras do jogo: Nosso time tem 7 goleiros, e o jogo usa 3 bolas, então a melhor formação é atacar —"

#         Nar "O mesmo forte brilho reaparece, enquanto você está acordado."

#         Nar "Repentinamente, a sua conversa totalmente interessante com o Dario é interrompida."
#         Nar "Você está sonhando, novamente. Mas, desta vez, está acordado."
#         Nar "E, na sala de aula, você vê…"

#         Nar "O cenário lentamente muda, para mostrar os corpos dilacerados de seus colegas de sala."

#         Nar "O corpo de Luna, Dario e Nycole, todos esquartejados."
#         Nar "E ao olhar para baixo, você percebe que você também…"
#         Nar "Que você também vai morrer."

#         Nar "O cenário fica completamente preto. Você desmaiou."




#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return

    
    

