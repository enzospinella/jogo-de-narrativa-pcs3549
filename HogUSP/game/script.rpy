# The script of the game goes in this file.

# PERSONAGENS ===============================================================

# Miscelâneos
define Nar = Character(color="#000000", what_italic=True)
define vc = Character("Você")

# Nicoly
define Ny = Character("Nicoly Nicoly", color="#f1208c")
define N1 = Character("Nicoly", color="#ff82ba")
define unknownNy = Character("???", color="#f30cc1")

# Dario
define Da = Character("Dario", color="#ffbe0b")
define unknownDa = Character("???", color="#ffbe0b")

# Lu
define Lu = Character("Luna", color="#db8708")
define unknownLu = Character("???", color="#db8708")

# Ciclista
define Zo = Character("Zoen, o Ciclista", color="#a70303")
define unknownZo = Character("???", color="#a70303")

# Laura
define La = Character("Laura", color="#44006b")
define unknownLa = Character("???", color="#44006b")

# IMAGENS ====================================================================

image escola_overlay_red = Composite(
    (1920, 1080),  # Tamanho da tela ou da imagem (ajuste conforme necessário)
    (0, 0), "bg escola.jpg",  # A imagem de fundo da escola
    (0, 0), Solid((255, 0, 0, 128))  # A sobreposição transparente vermelha
)

image bg livro_fechado = im.Scale("/images/livro aberto.jpg", 1920, 1080)
image bg escola_mortos = im.Scale("/images/bg escola_mortos.jpg", 1920, 1080)
image bg enfermaria = im.Scale("/images/bg enfermaria.jpeg", 1920, 1080)
image la_padrao = im.Scale("/images/la_padrao.png", 762, 955)
image nyc_puta1 = im.Scale("/images/nyc_puta1.png", 762, 955)
image nyc_puta2 = im.Scale("/images/nyc_puta2.png", 762, 955)
image dario_triste = im.Scale("/images/dario_triste.png", 762, 955)

# EFEITOS ====================================================================

define flashbulb = Fade(0.5, 0.0, 0.5, color="#b10000")
define flashbulb2 = Fade(0.5, 0.0, 6, color="#000000")
define flashbulb3 = Fade(0.1, 0.0, 0.9, color="#FFFFFF")

# TRANSIÇÕES =================================================================

transform slide_from_right:
    yalign 1.0
    xalign 2.0  # Mais fora da tela
    linear 0.5 xalign 1.0  # Movimento mais demorado

transform slide_to_right:
    yalign 1.0
    xalign 1.0  # Mais fora da tela
    linear 5.0 xalign 2.0  # Movimento mais demorado

# JOGO =======================================================================

label start:

    play music "nada.mp3" fadein 2.0

    scene bg dark
    
    Nar "Tudo está completamente escuro. Linhas, praticamente invisíveis, moldam o formato de uma caneta e um caderno."

    scene bg livro_fechado with fade

    Nar "No entanto… o formato rapidamente se desfaz."

    scene bg dark with dissolve

    vc "O que está... acontecendo?"

    Nar "Você é um aluno na Alta Academia de Magia. Embora não seja um ótimo aluno, você se dedicou muito para chegar aqui."

    vc "É verdade, eu estudei muito. Ainda tenho muito a aprender."

    Nar "Muitas gerações de poderosos magos passaram por aqui. Magos de transmutação, de emoções, de sabedoria…"

    Nar "E você ainda não tem nenhuma especialidade."

    Nar "Mas onde você estava antes de estar aqui? O que você estava fazendo?"

    vc "Acho que… eu estava…"

    vc "Eu estava na sala de aula."

    Nar "Sim. É verdade. Era uma aula de…"

    Nar "…"

    Nar "Deve ser difícil lembrar. Afinal, você dormiu a aula toda."

    vc "Não! Eu preciso ir bem nesta matéria. Senão vou ser expulso!!!"

    vc "Por favor, me deixe acordar!"

    Nar "…"

    Nar "Ninguém responde. Você está sozinho em um vazio infinitamente plástico. Exceto… por uma pequena fonte de luz."

    Nar "..."

    stop music fadeout 2.0
    play music "visões.mp3" fadein 2.0

    scene escola_overlay_red with flashbulb


    Nar "Você acorda em um ambiente estranho, sob uma luz vermelha, quando escuta..."

    show nyc_puta2

    unknownNy "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

    unknownNy "Vê se você acha nesse livro onde nós ainda somos amigas!" 

    voice "soco.mp3"
    queue sound "mulher_grito.mp3"
    Nar "A garota arremessa o livro na direção de outra na sala." with hpunch

    show nyc_puta2 at right with move
    show nyc_puta1 at right
    hide nyc_puta2
    show lu_padrao at left

    unknownLu "Ny… o que você tá… !!!"

    stop music fadeout 2.0
    play music "class.mp3" fadein 5.0
    $ renpy.music.set_volume(0.5)
    scene bg escola with flashbulb2


    Nar "Você acorda, sentado na sua mesa."

    vc "Puts, passei a aula inteira dormindo de novo…"

    vc "Mas hoje eu sonhei. Foi meio… estranho?"

    show dario_padrao

    play sound "dario.mp3"
    unknownDa "De boa, zé soninho? Cuidado que camarão que dorme a onda leva!!!"
    unknownDa "Amigo, caraca… Você dormiu pesado, hein? Até babou na mesa."
    unknownDa "Relaxa que teu amigo Dario tem lencinho. Tô sempre aqui pra te ajudar!"
    unknownDa "Ihhh, nem me apresentei, sou o teu amigo Dario. Se não ficou claro, né! Hahahaha!"

    Nar "Dario pega um lenço de sua mochila cheia de pins de diferentes cores e brilhos."
    Nar "Nesse tempo todo, o Dario não parou de sorrir. Ele está se esforçando muito para ser legal com você."

    Da "Opa, toma aí, amigo!"
    Da "Depois de uma dormida dessa, aproveitando que nós tamo aqui, queria te fazer uma proposta."
    Da "Agora temos o clube de futebol 2! É um esporte novo que tá bem na moda."
    Da "Reitero que hoje à tarde tem treino. Queria saber se você tá afim de —"

    voice "batida_porta.mp3"
    Nar "Uma moça muitíssimo bem arrumada e produzida chuta a porta, abrindo ela com um estouro." with hpunch

    show nyc_puta2 at right
    show dario_padrao at left with move

    Da "Ishhh, meu Gandalf!"
    Da "O que será agora?"

    hide dario_padrao
    show nyc_puta2 at center with move

    play sound "nicolybrava.mp3"
    unknownNy "LUNA! Sua ordinária. Foi VOCÊ que colocou esse bilhete no meu armário!"

    show nyc_puta2 at right with move
    show lu_padrao at left

    play sound "luna_surpresa.mp3"
    queue sound "luna_surpresa.mp3"
    Lu "Mas… Ny, eu…. eu só tô lendo fanfic…"

    Ny "Atitude típica de lacraia. Sua básica! Ainda fica se fazendo de vítima?"
    hide nyc_puta2
    show nyc_puta1 at right
    Ny "Só VOCÊ saberia a senha do meu armário. E fica colocando bilhetes nele como se a gente ainda fosse amiga?"

    Lu "Mas Ny… você me disse que confiava em mim para —"

    Ny "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

    vc "Espera… eu já ouvi isso antes…"

    Ny "Vê se você acha nesse livro onde nós ainda somos amigas!"

    Lu "Ny… o que você tá… !!!"

    Nar "Nycole arremessa um livro com a força de uma diva revoltada."

    voice "soco.mp3"
    queue sound "mulher_grito.mp3"
    Nar "BLAM!" with hpunch
    Nar "O impacto é ouvido por todos, e a sala inteira se levanta para observar o estado da Luna."

    hide nyc_puta1
    show lu_padrao at center with move

    Nar "Luna fica toda coitada no chão."

    play music "mulher_choro.mp3" channel "music2"
    $ renpy.music.set_volume(1.0, channel="music2")

    Nar "O livro, para a surpresa de ninguém, era um ciclista. Ele se levanta e imediatamente começa a pedalar."

    show lu_padrao at left with move
    show ciclista_padrao at right

    unknownZo "Foi mal, tô atrasado!"

    Nar "O Ciclista sai de cena rapidamente."

    show ciclista_padrao at slide_to_right
    show lu_padrao at center with move

    Nar "Após este evento completamente lógico e racional, todos olham para Luna."
    Nar "Ela está completamente imóvel, mas faz um som estranho, parecido com um cachorro triste."

    Lu "Hyuummmm… :("

    hide ciclista_padrao
    show la_padrao at slide_from_right

    unknownLa "…"

    voice "camera.mp3"
    show la_padrao at slide_to_right
    Nar "Uma garota estranha tira uma foto da Luna e sai da sala, lentamente." with flashbulb3


    show lu_padrao at left with move
    show dario_padrao at right

    Da "Damn, Luna! Você sabe que não dá pra responder ela."
    Da "A Nicoly é uma chata. Mas o look dela tava um arraso hoje."

    hide la_padrao

    Lu "Hyuummmmmmmmmmmmmmmmm… :("

    Da "Respira amiga… Coitada… Toma, eu tenho um feitiço de ibuprofeno pra você!"

    Nar "Dario retira um pedaço de papel azul com runas da mochila."
    stop music channel "music2" fadeout 2.0
    voice "dario_magica.mp3"
    Nar "Ao colocá-lo na cabeça de Luna, o papel brilha."

    Nar "Luna para de gemer e se levanta, ainda triste."

    Lu "O-Obrigada, Dario. Vou voltar a ler a minha fanfic de Parry Hotter…"

    hide lu_padrao
    show dario_padrao at center with move

    menu:
        Da "Interrompeu a gente amigo! Tá chocado? Nunca viu a Nycole tendo um piripaque?"
        "Eu acho que acabei de prever o futuro…":
            jump opcaoA
        "Já vi sim, só achei estranha a situação.":
            jump opcaoB
        "O livro era um ciclista?":
            jump opcaoC

    label opcaoA:
        Da "sh, ficou lelé? Não tem nenhum mago na academia capaz de ver o futuro."
        Da "Dúvido que tenha algum hoje, até teve no passado. Mas ele ficou maluquinho. E você parece normal pra mim!"
        Da "Ah, de qualquer forma, tem informações sobre isso na biblioteca."
        jump afterOpcao
    label opcaoB:
        Da "Ora, a única coisa estranha nessa história é a Luna ler Parry Hotter. Ela não sabe que é tudo mentira?"
        Da "Depois eu devesse levar ela na enfermagia (sim enfermagia), mas ela parece bem."
        Da "Ah, essas duas, costumavam estar tão juntos, agora…"
        jump afterOpcao
    label opcaoC:
        Da "Ou! Nossa, amigo. Ainda tá acordando?"
        Da "Do Zoen que tu perguntou? Ele é o estudante de transmutação. Consegue se transformar em tudo. Esqueceu?"
        Da "Assim, é completamente lógico e racional que ele vire um livro em seu tempo livre."
        jump afterOpcao

    label afterOpcao:

        Da "Retornando, a nossa conversa…"
        Da "Impossível essa escola passar um dia sem drama… Ai ai."
        Da "O bom é que essa vai ser a fofoca do dia!"
        Da "Depois dessa, não acho que vá rolar algo bombástico nas próximas horas que supere a Nycole armando um barraco…"
        Da "Ah, mas isso é muito improvável!"
        Da "Realmente… Enfim, queria te perguntar se você gostaria de participar do clube de Fut 2!"
        Da "Importante: Eu sou o capitão, e posso te mostrar como funciona tudinho!"

        hide dario_padrao
        show dario_triste

        Da "O ruim é que é um pouco cansativo ser o capitão, o melhor aluno da sala e a pessoa mais simpática da escola!"

        Nar "Pela primeira vez, você vê o Dario chorar por um segundo. Mas dura pouco."

        hide dario_triste
        show dario_padrao

        Da "Deixando isso de lado, eu amo muito tudo o que faço! Não trocaria por nada."
        Da "Antes de você dizer sim ou não pra proposta, deixa eu te explicar como funciona o jogo inteirinho!"
        Da "Regras do jogo: Nosso time tem 7 goleiros, e o jogo usa 3 bolas, então a melhor formação é atacar —"

        Nar "O mesmo forte brilho reaparece, enquanto você está acordado." 

        stop music fadeout 2.0
        play music "creepy.mp3" fadein 2.0
        $ renpy.music.set_volume(1.0)

        scene escola_overlay_red with flashbulb3
        hide dario_padrao 

        Nar "Repentinamente, a sua conversa totalmente interessante com o Dario é interrompida."
        Nar "Você está sonhando, novamente. Mas, desta vez, está acordado."
        Nar "E, na sala de aula, você vê…"

        scene bg escola_mortos with flashbulb2

        voice "som_tenso.mp3"
        Nar "{b}O CENÁRIO LENTAMENTE MUDA, PARA MOSTRAR OS CORPOS {color=#c40000}DILACERADOS{/color} DE SEUS COLEGAS DE SALA.{/b}" with vpunch

        voice "som_tenso.mp3"
        Nar "{b}O CORPO DE LUNA, DARIO E NICOLE, {color=#c40000}TODOS ESQUARTEJADOS{/color}.{/b}" with hpunch
        voice "som_tenso.mp3"
        Nar "{b}E AO OLHAR PARA BAIXO, VOCÊ PERCEBE QUE VOCÊ TAMBÉM...{/b}" with vpunch
        voice "som_tenso.mp3"
        Nar "{b}QUE VOCÊ TAMBÉM {color=#c40000}VAI MORRER{/color}.{/b}" with hpunch

        stop music fadeout 5.0
        play music "nada.mp3" fadein 2.0
        scene bg dark with dissolve

        Nar "O cenário fica completamente preto. Você desmaiou."

        scene bg enfermaria with flashbulb2

        Nar "Sua visão lentamente volta ao normal. No entanto, seu corpo ainda sente dor. Machucados, bem onde haviam cortes…"

        Nar "Você olha para baixo, na sua barriga. Havia um corte bem em seu estômago, e agora não há nada. A dor, aos poucos some."

        Nar "Você pensa que isso tudo deve ter sido uma visão."

    # This ends the game.

    return

    
    

