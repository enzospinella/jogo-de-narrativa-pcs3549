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

# EFEITOS ====================================================================

define flashbulb = Fade(0.5, 0.0, 0.5, color="#b10000")

# JOGO =======================================================================

label start:

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

    scene escola_overlay_red with flashbulb

    show nyc_padrao

    unknownNy "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

    unknownNy "Vê se você acha nesse livro onde nós ainda somos amigas!" 

    Nar "A garota arremessa o livro na direção de uma garota na sala." with hpunch

    show nyc_padrao at right with move
    show lu_padrao at left

    unknownLu "Ny… o que você tá… !!!"

    scene bg escola with flashbulb

    Nar "Você acorda, sentado na sua mesa."

    vc "Puts, passei a aula inteira dormindo de novo…"

    vc "Mas hoje eu sonhei. Foi meio… estranho?"

    show dario_padrao

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

    Nar "Uma moça muitíssimo bem arrumada e produzida chuta a porta, abrindo ela com um estouro." with hpunch

    show nyc_padrao at right
    show dario_padrao at left with move

    Da "Ishhh, meu Gandalf!"
    Da "O que será agora?"

    hide dario_padrao
    show nyc_padrao at center with move

    unknownNy "LUNA! Sua ordinária. Foi VOCÊ que colocou esse bilhete no meu armário!"

    show nyc_padrao at right with move
    show lu_padrao at left

    Lu "Mas… Ny, eu…. eu só tô lendo fanfic…"

    Ny "Atitude típica de lacraia. Sua básica! Ainda fica se fazendo de vítima?"
    Ny "Só VOCÊ saberia a senha do meu armário. E fica colocando bilhetes nele como se a gente ainda fosse amiga?"

    Lu "Mas Ny… você me disse que confiava em mim para —"

    Ny "CALADA! Pode bancar de inteligente, mas é uma burrinha!"

    vc "Espera… eu já ouvi isso antes…"

    Ny "Vê se você acha nesse livro onde nós ainda somos amigas!"

    Lu "Ny… o que você tá… !!!"

    Nar "Nycole arremessa um livro com a força de uma diva revoltada."
    Nar "BLAM!" with hpunch
    Nar "O impacto é ouvido por todos, e a sala inteira se levanta para observar o estado da Luna."

    hide nyc_padrao
    show lu_padrao at center with move

    Nar "Luna fica toda coitada no chão."
    Nar "O livro, para a surpresa de ninguém, era um ciclista. Ele se levanta e imediatamente começa a pedalar."

    show lu_padrao at left with move
    # show ciclista_padrao

    Zo "Foi mal, tô atrasado!"

    Nar "Zoen sai de cena rapidamente."

    # hide ciclista_padrao
    show lu_padrao at center with move

    Nar "Após este evento completamente lógico e racional, todos olham para Luna."
    Nar "Ela está completamente imóvel, mas faz um som estranho, parecido com um cachorro triste."

    Lu "Hyuummmm… :("

    # show la_foto at right

    unknownLa "…"

    Nar "Uma garota estranha tira uma foto da Luna e sai da sala, lentamente."

    #hide la_foto

    show lu_padrao at left with move
    show dario_padrao at right

    Da "Damn, Luna! Você sabe que não dá pra responder ela."
    Da "A Nicoly é uma chata. Mas o look dela tava um arraso hoje."

    Lu "Hyuummmmmmmmmmmmmmmmm… :("

    Da "Respira amiga… Coitada… Toma, eu tenho um feitiço de ibuprofeno pra você!"

    Nar "Dario retira um pedaço de papel azul com runas da mochila."
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

        # hide dario_padrao
        # show dario_triste

        Da "Retornando, a nossa conversa…"
        Da "Impossível essa escola passar um dia sem drama… Ai ai."
        Da "O bom é que essa vai ser a fofoca do dia!"
        Da "Depois dessa, não acho que vá rolar algo bombástico nas próximas horas que supere a Nycole armando um barraco…"
        Da "Ah, mas isso é muito improvável!"
        Da "Realmente… Enfim, queria te perguntar se você gostaria de participar do clube de Fut 2!"
        Da "Importante: Eu sou o capitão, e posso te mostrar como funciona tudinho!"
        Da "O ruim é que é um pouco cansativo ser o capitão, o melhor aluno da sala e a pessoa mais simpática da escola!"

        Nar "Pela primeira vez, você vê o Dario parar de sorrir por um segundo. Mas dura pouco."

        # hide dario_triste
        # show dario_padrao

        Da "Deixando isso de lado, eu amo muito tudo o que faço! Não trocaria por nada."
        Da "Antes de você dizer sim ou não pra proposta, deixa eu te explicar como funciona o jogo inteirinho!"
        Da "Regras do jogo: Nosso time tem 7 goleiros, e o jogo usa 3 bolas, então a melhor formação é atacar —"

        Nar "O mesmo forte brilho reaparece, enquanto você está acordado." with flashbulb

        Nar "Repentinamente, a sua conversa totalmente interessante com o Dario é interrompida."
        Nar "Você está sonhando, novamente. Mas, desta vez, está acordado."
        Nar "E, na sala de aula, você vê…"

        scene bg escola_mortos with fade

        Nar "O cenário lentamente muda, para mostrar os corpos dilacerados de seus colegas de sala."

        Nar "O corpo de Luna, Dario e Nycole, todos esquartejados."
        Nar "E ao olhar para baixo, você percebe que você também…"
        Nar "Que você também vai morrer."

        scene bg dark with dissolve

        Nar "O cenário fica completamente preto. Você desmaiou."

    # This ends the game.

    return

    
    

