# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Personagens
define e = Character( )
define a = Character("Aline")
define b = Character ("Sarah")
define c = Character ("Camila")
define m = Character ("Amanda")
define d = Character ("Mãe")


# Som

define audio.quarto = "audio/leonelmail-quarto.mp3"
define audio.cidade = "audio/cidade.wav"
define audio.tension = "audio/tension-erh.wav"
define audio.triste = "audio/inspectorj-triste.wav"
define audio.passosapressados = "audio/sgel05-apressado.wav"
define audio.casa1 = "audio/inspectorj-ambience.wav"
define audio.dia = "audio/hargissssound__dia.wav"
define audio.piano2 = "audio/dasgoat-piano.mp3"

# The game starts here.
# Começo do jogo

label start:

    play sound quarto
    scene quarto 1

    show sarah at left

    #musica ambiente

    "A história começa com uma jovem chamada Sarah."
    "Ela é filha única, morando com sua mãe em um bairro da cidade qualquer."
    "Era de noite, quando estava em seu quarto."

    show sarah at left

    b "Cara. Que tédio... O que eu posso fazer agora?"

    "Entediada, ela se mexeu em sua cadeira de plástico, esticando as mãos para cima."
    "A tela do computador tinha um brilho intenso e mostrava alguns sites abertos."

    b "Não é como se algo novo acontece todo dia...  Ah..."
    b "Ei, o que é isso? {w} Um meme?"

    show meme tempo


    b "Espera, máquinas do tempo?"

    hide meme tempo

    b" Ha. Só pode ser piada."
    b"HAHA! Até parece. Eu não acho eu faria algo assim."
    b"Ao menos não desperdiçar essa chance... Com uma máquina do tempo. Visitar minha avó quando era jovem. Ha..."
    b"Na real. Vou dormir."

    "Sarah desligou o seu computador e fez seu ritual para enfim, dormir."
    b"Vou apagar a luz. E não vou correr. Não é como se eu tivesse medo do escuro... Ha."

    "Dito isso, ela se forçou a andar devagar na escuridão do quarto. Bateu o dedo no pé na quina da cama e resmungou alto."

    #som impacto, esbarrando em algo

    b"NÃO CREIO. TODA VEZ ISSO."
    b"Que raiva."

    "Por fim, se jogou na cama, puxando seu cobertor. Se enrolou e fechou os olhos com força, bufando."

    b"Espero dormir logo."

    "Então passou-se algumas horas. A garota estava inquieta, mil pensamentos vindo a sua mente."

    b"Não... Isso não faz sentido. Por que eu penso nisso a essa hora da noite?"
    b"... Acho que eu vou sentar um pouco."

    "Ela se levanta devagar, não enxergando nada. Porém, ela sabia que sempre deixava o celular na escrivaninha ao lado de sua cama. Estendeu o braço e apalpou, porém não encontrou nada."

    b"Ah qual é. Meu celular não."

    "Começando a ficar agitada, ela continuou a mover o braço, mas nenhum celular foi encontrado."

    b"Não creio. Eu coloquei ele aqui!"

    "Ela se levantou, e nisso sentiu um enjoou, e caiu."

    #som baque no chão

    stop sound

    "Com um baque, seu corpo foi ao chão e fechou os olhos."

    "..."
    "..."
    "..."
    "..."

#aqui ela acabou de viajar ao passado, para a época da sua avó

    scene avenida
    with dissolve

    show  sarah at left
    show camila at right

    play music cidade

    "???""Ei..."
    "???""Ei. Acorde..."
    "???""Hum... Vai, reage."

    b"..."
    b"............."
    b"Ugh..."

    "A garota tentou abrir os olhos, mas parecia uma tarefa difícil. Sentia seu corpo pesado, desnorteada e sem a menor noção de onde estava."

    b"...Eu cai da cama... Não cai?"
    b"Ugh..."

    "Respirando fundo, ela cosegue abrir os olhos. Coloca as mãos no superfice em que estava e se força a levantar."

    b"Ah..."
    b"Que dor de cabeça..."

    "???""Ah! Você acordou!"
    "???""Eu estava preocupada..."

    "Sarah conseguiu ficar em pé, ainda cambaleando. O mundo girava a sua frente, aos seus olhos tudo parecia embaçado."
    "Colocou a mão na cabeça, fechando os olhos."

    b"...Onde... Eu estou?"

    "Perguntou, ainda de olhos fechados."

    "???""Ah. Espere, moça, você caiu aqui... Você está bem?"

    b"Não."

    "Respondeu prontamente, a sua voz ficando ríspida."

    b"Estou irritada na verdade."
    b"Onde estou?"

    "???""Poxa... Moça, eu acho que você está perdida..."
    "???""Meu nome é Camilla. Posso te ajudar?"

    c"Você estava caida no chão..."
    c"Então eu vim ver o que estava acontecendo."

    "Ela finalmente abriu os olhos, a claridade ofuscando a visão. Piscando, ela conseguiu ver o que estava a sua frente. Não era seu quarto."

    #show seis neutra

    "Era uma praça, com várias árvores, calçada pavimentada de pedras e várias casas de porte médio."
    "Não parecia ser algo que conhecia..."

    b"Ah para."

    #show sarah irritada

    b"Onde que eu estou?!"

    #show camilla triste

    c"E-ei calma! Qual seu nome? Eu posso te ajudar!"
    c"Na verdade nem eu sei como... Mas vou tentar!"

    b"Cara, isso aqui não é onde eu moro! Eu moro em Nova XX!"

    "Irritada, a garota comeeçou a olhar ao seu redor, virando-se e andando. Isso chamou atenão de algumas pessoas, que pararam para olha-la."
    "Seus cabelos estavam começando a grudar em seu rosto, com o suor descendo a testa."

    b"Isso não é onde eu moro! Que saco, onde que eu estou?!"

    c"M-moça! Espere! Por favor não faça isso!"

    b"Não pode ser! Mãe!"

    c"Moça! Vem comigo!"

    "Camilla pegou em seu pulso, assutando Sarah. Com uma feição preocupada, ela falou baixo."

    c"Se ele virem que você está fazendo um alvoroço... Eles podem te levar. Vem comigo."

    b"Q-quem?"

    "Sarah olhou ao redor. De alguns cantos daquela praça, começaram a aparecer alguns homens de farda verde e usando uma espécie de capacete preto."

    "Ela reconheceu o uniforme e gelou."

    c"Vamos!"

    stop music

    play sound passosapressados

    #som de passos de corrida

    scene rua comum
    with dissolve

    show camila at right
    show sarah at center

    "Depois de alguns minutos andando apressadamente, elas viraram um beco, estreito e após atravesa-lo, seguiram para a direita em uma rua sinuosa."
    "Continuaram o percurso, Sarah olhando ao seu arredor e tentando identificar algo familiar."

    stop sound

    "Foi quando olhou para uma casinha amarela, de portão cinza claro e telhado vermelho."

    b"E-eu conheço! Espera, aquela não é a casa do-"

    c"Silêncio! Por favor... Eles estão em toda parte."
    c"Vou levar você comigo minha jovem."

    b"E-ei ei! Para onde??"

    c"Minha casa, ali você vai se acalmar e te ajudo a achar o seu caminho de casa."
    c"Agora venha comigo, em silêncio. Por favor."

    b"Não pode ser... Eu acho que conheço esse lugar!"

    "Camila soltou o pulso da garota, e continuou a caminhar com passos apressados."
    "Sarah a seguiu em silêncio, vendo que conhecia algumas poucas casas. Ou aomenos, acreditava que conhecia..."
    "Com o coração a mil, ela fez o máximo para não chamar atenção nas ruas."
    "Ela percebeu que vestia roupas diferentes das demais pessoas, que eram de cores voltadas para o marrom como ternos."

    c"Venha logo, não quero que as pessoas fiquem nos encarando."

    "Camilla destrancou seu portão cinzento, em frente a uma casa pequena de cor amarela. Havia um jardim modesto em frente, com flores bem cuidadas e o piso tinha um padrão marrom escuro."
    "Com um baque, ela fecha o portão e retira as chaves da sua bolsa."

    #som de portão fechando

    c"Entre minha jovem."

    b"Certo..."

    scene casa camila tarde
    with dissolve
    play sound casa1

    show sarah at left
    show camila at right

    "Sarah estava com um pressentimento incomum."
    "Aquilo tudo era real... Porém parecia um sonho."
    "Reconheceu algumas casas, porém esta não."
    "Vários pensamentos vieram a sua mente no momento, mal conseguindo ouvir o que a mulher a sua frente falava."

    b"... Isso é um sonho... Certo?"

    c"Sonho? Não minha querida, estamos bem vivas da silva. Gostaria de um café?"

    b"... Qual era o seu nome mesmo?"

    c"Camilla, meu bem. Sente-se, você precisa respirar um pouco."

    b"..."

    "Sem contestar, Sarah pegou a cadeira de madeira, percebendo agora o lugar em que estava."
    "O chão era de madeira, assim como a maioria dos móveis, envernizados e marrons. A maioria deles tinha panos feitos em crochê, como se acompanhasse cada móvel da dasa."
    "Havia um telefone com fio, e Sarah percebeu que era o chamsdo telefone de disco. Ela já havia visto um desses, em algum lugar."
    "O sofá era pequeno, coberto com alguns panos. Havia um tapete grande no chão também."

    c"Eu vou trazer o café, está quase pronto."

    hide camila
    with dissolve

    "Sarah ouviu, e voltou a si. A mulher mais velha estava na cozinha, e já sentia o cheiro de café sendo feito."
    "E bom, ela não gostava de café."

    b"Putz..."

    c"Você perguntou alguma coisa?"

    b"A-ah não. Estou apenas pensando alto..."

    c"Esses jovens. Com essas gírias..."

    "Nisso, a garota percebu que estava sendo observada por um par de olhos curiosos. Perto da escaria acima, alguém estava parado, uma figura pequena."
    "Curvou a cabeça para ver o que era, porém o vulto despareceu."

    b"...Eu... Não sei onde eu estou. Mas... Algo está errado."

    c"O que está errado?"

    show camila at right

    b"A-AH! Que susto!"

    c"Ihihi, desculpe. Aqui, trouxe seu café."

    "Colocando a xícara na mesa, a mulher se sentou e deixou um longo suspiro ecoar."

    "Ela parecia cansada."

    "Em silêncio, a convidade se sento também, olhando para o chão."

    c"... Sabe, você me parece bem familiar. Já nos conhecemos de algum lugar?"

    b"... Eu acho que não."

    c"Ah! Já sei, você deve ser uma das alunas da dança do salão!!"

    c"Sabia que conhecia você."

    c"Sabe, eu tenho uma filha. Ela é um pouco tímida, está no quarto dela."

    c"Eu e a minha espo- amiga moramos aqui."

    c"M-minha filha adora brincade de boneca... Mas ao brincar no quintal, suja algumas na lama. Acho que algumas crianças brincam disso também."

    c"Você se lembrou da onde veio?"

    b"... Eu acho que sim."

    c"Que bom! Se quiser pode fazer uma ligação para seus pais... Temos um telefone."

    b"N-não precisa... Desculpe a confusão, Dona Camila..."

    "Nisso, ouviu-se um barulho vindo da escada. Alguém estava descendo a escadaria."

    "???""Camila, você fez café?"

    "Falou uma voz feminina, e Camila ficou quieta."

    "???""Estou descendo."

    "A mulher que desceu as escadas tinha uma pele morena, um cabelo curto e carregava uma criança em seu colo."

    hide camila
    show aline at left
    show criança at left

    "Assim que viu Sarah, ela parou e olhou para Camila e depois para Sarah."

    "Se seguiu um silêncio desconfortável, em que Sarah olhava com surpresa para a mulher a sua frente."

    "???""Ah... Temos visitas. Olá, acredito que a Camila não tenha mencionado... Sou amiga dela, Aline."

    b"..."

    b"..."

    b"...Ah. Entendi. Meu nome é Sarah..."

    b"Desculpe incomodar, eu pretendia ir embora."

    c"Mas tão cedo? Você se lembra onde mora?"

    b"E-eu acho que sim."

    c"Aline, acho que ela se perdeu... Trouxe ela aqui, ela precisava de ajuda."

    a"Tudo bem. Sarah, você disse que se lembra onde mora? Posso levaar você ate lá, o que acha?"

    b"...Eu não me lembro o endereço... O nome digo. Mas posso ir andando."

    "Nesta hora, a criança levantou a cabeça e Aline a colocou no chão. Ela tinha pele morena, mas cabelos cacheados longos, diferente da mãe."
    "Ela estava sonolenta, passando as costas da mão no olho várias vezes."
    "Segurou a barra do seu vestido azul, apertando antes de dizer."

    "???""Mãe... Tem pão de queijo?"

    "Ela olhou para a Camila, que a segurou no colo. Novamente o silêncio se instarou."

    #show todo mundo com cara de nervouiseerrr

    b"Eu vou indo agora..."

    a"Eu acompanho você até o portão."

    b"Tudo bem. Obrigada Dona Camila, por ter me ajudado... E boa tarde..."

    "Sarah se levantou e rumou para a porta, que Aline já havia aberto."

    "Estava ficando tarde, a cada segundo que passava Sarah ficava cada vez mais nervosa."

    stop sound

    scene rua comum
    show sarah at right
    show aline at left

    "Aline percebeu que esqueceu as chaves do portão, e voltou dentro de casa para pega-las."

    a"Um minuto."

    hide aline

    #show sarah triste

    b"...Eu entendi. Ou eu acho que entendi..."
    b"Mas... Como?"
    b"Como...?"

    stop sound

    play sound triste

    "Segurando as lágrimas, mordeu o lábio inferior da boca, olhando para baixo."

    b"Está... Tudo errado..."

    show aline at left

    a"Aqui! Achei a chave, vou abrir pra você."
    a"Tem algo de errado? Você parece triste."

    b"... Você não precisa me acompanhar. Posso ir sozinha."

    a"Eu falei que poderia te acompanhar, não falei?"
    a"...Tudo bem você não gostar de mim por eu ser negra, mas..."

    b"N-não é isso!!"

    "A garota virou o rosto, brava."
    "Cerrou as mãos em punho e olhou para baixo."

    b"Eu posso me virar sozinha..."

    a"Eu acho que juntas, as mulheres são mais fortes..."
    a"Eu posso te acompanhar, sem problemas. Eu corro bem rápido."

    b"Não."

    "Aline segurou o portão, já aberto. Ela encarava com curiosidade Sarah. Ela puxou o portão, como um sinal para Sararh ir."

    b"Obrigada. Eu vou achar meu caminho, Dona Alice..."

    "Nisso, ela saiu. Com passos apressados, de distanciando rapidamente da casa amarela."

    stop sound

    scene avenida noite
    with dissolve

    play music cidade

    "Sarah estava magoada."
    "Triste e com o coração apertando, segurando as lágrimas conforme andava pelas ruas."
    "Quando se deu conta, estava novamente naquela praça, que levava a uma avenida. Os carros não eram muitos por entre as ruas, assim como as pessoas caminhando, saindo de seus expedientes."
    "Respirou fundo, na tentativa de aliviar os pensamentos emaranhados, dentro de sua cabeça."

    show sarah at right

    b"Isso... Não pode ser real. Não pode..."

    b"Como é possível? Eu voltei para o passado..."

    b"E ainda... Vi minhas avós! Quer dizer nem sabia que era dua avós..."

    b"Ninguém nunca me contava nada... Justo porque elas são duas mulheres..."

    b"Eu já não vou com a cara dos meus parentes... Bom, se eles esconderam isso de mim. Que trouxas."

    "Ela se sentou num banco de madeira, proximo a uma árvore, não muito distante da pista de carros."

    "Ficou de braços cruzados, pensando no que fazer a seguir."

    "Ela conhecia algumas poucas histórias de viajem no tempo. Quando esse evento ocorria com o protagonista, ele não deveria alterar nada, pois implicaria na própria existencia."
    "E se ela tivesse feito algo irreparável?"
    "Não tinha o conhecimento que sua avó tinha uma parceira, pois a mesma havia falecido quando era uma criança."
    "Começou a pensar no pior, nas possibilidades de que não poderia nem mesmo existir."
    "E agora?"

    b"..."
    b"Nuna pensei em dizer isso... Mas..."

    "???""Ei!"

    stop music

    play music tension fadeout 3.0

    #show policial mau ou a sombra dele

    "Sarah se virou na direção da voz. Se levantou no memso instante, assustada."

    b"Não creio! São os tiras!"

    b"Ah cara... Agora não..."

    "Policial""EI mocinha! Onde pensa que está?"

    b"Ah não..."

    "Sarah se lembrou que em suas aulas de história, essa época do pais, policiais prendiam muitas pessoas. Mesmo sem motivos."
    "Por ser um pais patriarcal, mulheres andarem sozinhas na rua não era bem visto. Principalmente se havia preconceito contra pessoas negras..."

    "Ela pensou em duas coisas: fugir na direção contrária ao policial ou então tentar ser razoável."
    "A primeira pareceu a mais sensata."

    "Se virou e correu."

    "Correu pois sabia que sua vida dependia disso, e que no momento, nada mais importava."

    b"Se eu ainda estou aqui, é porque eu não alterei- ao menos não muito- a linha do tempo!"
    b"Eu... Vou sair daqui!"

    "Policial""Peste! VOLTE AQUI!"

    b"Corre, corre Sarah!"

    "Ela virou a esquina, pedindo lisença para as pessoas a sa frente, conforme corria."

    "Os cabelos chamavam atenção, mas a garota corria tão rápido que quando as pessoas percebiam, ela já estava longe."

    "O Policial pareceu desistir em algum ponto, pois após em algum determinado tempo, ela parou de ouvir a voz dele."

    "Foi parando de correr, até virar uma caminhada. Parou e encostou a mão ao lado de uma árvore, cansada e ofegante."

    b"... Eu... Eu consegui...?"

    "Exausta, ela puxava o ar para seus pulmões com força e cada inspiração doia."

    b"...Será... Que eu consegui..."

    "Sarah fechou os olhos por um instante."

    "Foi quando sentiu alguém colocando a mão em seu ombro."

    "???""Te achei, garota."
    "???""Você vem comigo."

    "Sarah gritou, tentando se desvincular da mão enluvada do homem. Era o mesmo policial de antes, com o rosto vermelho e carranca."

    b"Me solte!"

    "Puxou seu pulso com força, mas ele era mais forte. A figura dele a assutou, pois sabia o que policiais como ele poderia fazer."

    "???""Garota tola! Vou te levar comigo!"

    b"ME SOLTA SEU NOJENTO"

    "Nesse momento, uma figura apareceu atrás dele e o atingiu com força."

    play sound thud

    "Ele foi ao chão, caindo com um grande baque no asfalto."

    stop sound

    "Sarah ficou zonza, não conseguindo distinguir muito a figura a sua frente."

    a"Sarah! Falei que ia junto com você!"

    a"Menina teimosa!"

    "Era Aline, sua avó, que a salvou."

    show aline at left

    "Sarah ficou sem palavras ao perceber que era ela e começou a chorar."

    a"E-ei, já passou. Mas temos que sair daqui, a vizinhança vai notar."

    b"..."

    b"O-obrigada..."

    a"Não me agradeça. Juntas somos fortes. Vamos!"

    b"P-pra onde?"

    a"Minha casa. Você vem comigo, tudo bem?"

    b"..."

    b"O-obrigada..."

    scene rua comum noite
    with dissolve



    "Elas seguiram num ritmo apressado até a casa de portão cinza."
    "Aline tinha seu modesto macacão azul, e escondeu sua chave inglesa em seu bolso largo."
    "O percurso foi silêncioso, sem tempo para conversas."

    b"..."

    b"Aline... Eu sei de você e a Camila."

    a"..."

    b"Eu não tenho nada contra, na verdade... Mas... Deve ser... Difícil..."

    a"... É bem difícil."

    b"Desculpe... Se pareci-"

    a"Tudo bem. Você me parece uma boa pessoa... E meu sexto sentido nunca falhou."

    "Sarah pensou no que poderia dizer para a sua avó, na qual não tinha muitas memórias."
    "Não queria alterar o futuro... Ao menos não para algo ainda pior."

    b"..."
    b"...Qual o nome da sua filha?"

    a"Amanada..."
    a"Nossa pequena Amanda."

    "Sarah sorriu. Era o nome da sua mãe."

    "Nunca pensou em conhecer sua mãe, só que criança."

    a"Você não se importaria em dormir no sofá?"

    b"A."

    b"Tudo bem... Eu não me importo."

    a"Certo. Estamos quase lá."



    scene casa camila noite
    with dissolve

    play music casa1

    show sarah at left
    show aline at right

    a"Pronto. Deixei arrumado aqui para você."

    b"... Desculpe incomodar."

    a"Tudo bem. Amanhã cedo vamos procurar a sua casa e seus pais."

    b"Tudo bem."

    "Sarah de algum modo, começou a se sentir em casa."
    "Sua casa do futuro ficava em São Paulo, mas longe do centro. Era diferente, tanto em estilo e estrutura."

    "Sarah teve um dia e tanto, pensou."
    "Sem dúvidas, a parte do policial... Foi a mais assustadora."

    b"...Eu espero que essa epóca de ditadura... Acabe logo."

    a"É. Eu também..."
    a"Eu já vi muitos camaradas... Pegos."
    a"Todo dia eu rezo, para que eu não seja... Mais uma vítima."

    b"...Eu espero... Que você e sua familía sejam... Muito felizes."

    a"Obrigada, Sarah."
    a"Tudo vai se encaixar amanhã."

    b"Certo. Boa noite."

    "Sarah ouviu Aline sair e apagar as luzes."

    hide aline

    "Ela se cobriu com o cobertor, que tinha um cheiro diferente. De criança com shampoo."

    b"He. Deve ser da mãe."
    b"Eu espero... Que eu consiga voltar para casa."
    b"Eu quero... Voltar pro meu tempo..."

    b"Eu não ia aguentar crescer aqui. Nesse período... Como tem gente que esqueceu disso?"

    "Com muitas dúvidas em sua mente, não conseguiu dormir."
    "Se virou no sofá, não achando uma posição certa."

    b"E se... Eu olhasse as coisas da casa...?"
    b"Esse telefone parece irado..."

    "Não. Isso é falta de educação."

    "Ouviu alguém se aproximar, e já era bem tarde da noite."
    "Eram passos quase que silênciosos no chão de madeira."

    "Sarah fingiu que dormia. Poderia ser..."

    show criança

    m"Oi."
    m"Quer ser minha amiga?"

    b"Ah!"

    "Ela pulou do sofá, assustando também a criança."

    m"Nossa tia, que susto."

    b"Cara... O que eu falo pra ela?"

    b"Ei... Você não quer ir dormir não?"
    b"Acho que ta ficando meio tarde..."

    m"Eu queria brincar. Brinca comigo?"

    "A criança estendeu uma boneca de pano, um pouco suja e bem gasta."

    b"Certo... Então vamos brincar um pouquinho."

    scene casa camila dia
    with dissolve

    play sound dia

    "Já era de manhã."
    "Aline era a primeira a acordar, pois chegava cedo no trabalho."

    show aline at right

    "Quando desceu para fazer café, encontrou a jovem Sarah esparramada no sofá, e sua filha, Amanda, junto."

    "Sorriu e andou devagar, tentando não acorda-las."

    "Porém não funcinou, pois Sarah já estava acordada e se levantou."

    show sarah at left

    "Amanda dormia profundamente no sofá, Sarah a cobriu com o cobertor e cumprimentou Aline."

    b"Bom dia..."
    a"Bom dia."
    b"Vamos sair agora?"
    a"Sim. Vou fazer um café. Gostaria?"
    b"Tudo bem."

    "Aline preparou um rápido café da manhã. Sarah comeu um pedaço de pão e permaneceu quieta, escutando o som dos pássaros e as poucas buzinas de carros que vinham da rua."
    "A mulher mais velha se sentou na cadeira e não demorou para terminar a refeição, habituada a fazer isso rapidamente."

    b"...Aline. Você trabalha aonde?"
    a"Em uma fábrica. Não é muito longe daqui, mas uso o bonde."
    b"... É verdade, aqui ainda existia bondes..."
    a"Existia?"
    a"O que você está falando?"
    a"Você mora longe do centro?"

    b"Ah... Eu acho que sim. Eu não tinha visto um desses antes..."

    a"Ah. Achei que conhecesse, pois meninas do campo não costumam usar calças jeans."

    b"Ah."

    "Sarah começou a suar, nervosa."
    "Aline parecia uma pessoa esperta, e se descobrisse que ela do futuro?"
    "Não... Sarah pensou que não seria para tanto."
    "Tentaria enrolar mais um pouco e pensar de um modo de voltar para casa."

    b"Ugh.."
    a"O que foi?"

    stop music
    play music piano2

    "Sarah começoua sentir um forte enjoou. A sua visão começou a ficar embassada, o ambiente girando ao seu redor."
    "Esssa sensação... Sim... Foi a primeira vez quando teve antes de dormir."

    a"Você está bem?"

    b"... Ugh... Está tudo... Girando..."

    b"Eu... Preciso de contar uma coisa...."

    "Aline se levantou e a segurou pelos ombros, as mãos calejadas tocando sua testa."

    a"Você não está com febre..."
    a"Eu vou pegar um xarope."

    b"E-espera..."
    b"Eu queria dizer... Que..."


    menu:

        m"Decida sua escolha: "

        "Contar a verdade":

            jump situacao1

        "Não contar a verdade":

            jump situacao2

label  situacao1:

    a"O que foi?"

    b"Eu... Não sou daqui. Você..."
    b"Você é a minha avó..."

    a"O que? Você bateu a cabeça, criança?"

    "O enjoou ficou mais forte e ela abaixou a cabeça, fechando os olhos."

    b"Eu queria... Ter tido mais tempo com você... Vó..."
    b"Por favor... Tome cuidado... Quando você for idosa..."
    b"Não reaja a um assalto..."
    b"Vó..."

    a"Espera, como assim?"
    a"Explique isso, menina!"
    a"Sarah?"
    a"Sarah!"

    "Tudo ficou escuro para a garota. Ela não ouviu mais nada e não sentia seu corpo. Desmaiou."

    scene quarto 1
    with fade

    show sarah at right

    "Sarah acordou gritando, faltando ar e jogando as mãos para cima."

    b"Gasp! Ahhh!!"

    "Assustada, a garota permaneceu em sua cama, tentando respirar."
    "Então ouviu o som de passos apressados e a porta do seu quarto abriu."

    d"Sarah! Filha, está tudo bem?"

    stop music

    play music casa1

    show mae at left

    b"M-mãe!"

    "A mulher se aproximou, sentando na beirada da cama, colocando a mão na testa da garota."

    d"Você não está com febre... Quer um xarope?"

    b"N-não!"
    b"É que... Eu acho... Que eu tive um sonho... Ou então..."

    d"...Tudo bem. Você quer me contar? O que aconteceu?"

    b"...Eu vi a vó... Ela estava... Viva..."
    b"Ela e a Camila... Você também estava lá..."
    b"Foi um sonho... Só pode..."

    d"Acho que suas avós tem mostrado muito as fotos delas, de quando eu era uma criança..."
    d"Elas estão para vir nesse final de semana. Acabaram de ligar perguntando de você."

    b"Elas... As vovós estão vivas?"

    d"Ué. COmo não estariam?"
    d"Elas sempre vem aos finais de semana. Elas falaram que vão trazer o seu bolo favorito."

    b"É-é sério?"
    b"Porque... Porque meu sonho elas..."

    d"Acho que você teve um pesadelo."
    d"Coitada. Deve ter sonhado."

    b"Parecia... Uma viajem no tempo...."

    d"Não diga essas coisas. Se você mudar o passado, você muda o futuro."
    d"Acho que foi aquele filme ou aquela série..."
    d"Esses jovens."
    d"Bom... Se está tudo bem, vou descer e terminar o jantar."
    d"Não demore, ok?"

    b"C-certo..."

    "A mulher saiu do quarto, fechando a porta. Sarah ficou sozinha, ainda assustada."

    hide mae

    b"Aquilo... Não foi um sonho..."
    b"Eu... Mudei a linha do tempo?"
    b"Minhas avós... Estão vivas?"

    "Lágrimas caim pelos olhos da jovem. Ela cobriu com as mãos, mas não parava de chorar e soluçar baixinho."
    "Estava feliz. Ainda não entendia o que havia acontecido... Mas tinha as memórias de uma vida sem suas avós."
    "E agora, tinha duas, que iriam visita-la no fim de semana..."

    b"Será que... Eu mudei a linha do tempo? Eu fiz alguma coisa...?"
    b"...Bom... Que bom..."

    "Sarah sorriu para si mesma. Enxugou as lágrimas do rosto e se levantou."

    "Sua barriga roncou de fome e entendeu isso como um sinal para descer e jantar com sua mãe."
    "Abriu a porta, a luz do corredor ofuscando sua visão."

    b"Mãe! Tô descendo!"
    b"Estou com fome... E com vontade de beber café..."

    "Fim do jogo! Obrigada por ter jogado!"

    return

label  situacao2:

    show sarah at left
    show aline at right

    a"O que foi? Sarah?"
    a"Sarah!"

    "Sarah se curvou, a tontura cada vez mais forte."
    "Aline contiuava sem saber o que fazer, apenas colocou a mão nas costas da garota, para tentar apoia-la."

    a"Q-quer que eu te leve para a sala?"

    "Tudo continuava a girar e girar, vendo as coisas distorcidas."
    "O que estava acontecendo, afinal?"

    b"...Urrgh... Eu não posso te contar... Mas..."
    b"...Urgh..."

    a"Ei, Sarah, o que foi? O que eu posso fazer?"

    b"..."

    b"...Eu vou voltar para casa... Eu acho..."
    b"É... Bem longe daqui..."

    a"Eu falei que iria te ajudar, não falei?"

    b"....Você... Obrigada..."

    "Dito isso, Sarah desmaiou."

    scene quarto 1
    with fade

    show sarah at right

    "Sarah acordou gritando, faltando ar e jogando as mãos para cima."

    b"Gasp! Ahhh!!"

    "Assustada, a garota permaneceu em sua cama, tentando respirar."
    "Então ouviu o som de passos apressados e a porta do seu quarto abriu."

    d"Sarah! Filha, está tudo bem?"

    show mae at left


    b"M-mãe!"

    "A mulher se aproximou, sentando na beirada da cama, colocando a mão na testa da garota."

    d"Você não está com febre... Quer um xarope?"

    stop music

    play music casa1

    b"N-não!"
    b"É que... Eu acho... Que eu tive um sonho... Ou então..."

    d"...Tudo bem. Você quer me contar? O que aconteceu?"

    b"...Eu vi a vó... Ela estava... Viva..."
    b"Ela e a Camila... Você também estava lá..."
    b"Foi um sonho... Só pode..."

    d"Sarah... Me desculpe..."
    d"Mas elas... Morreram quando você era pequena..."
    d"Eu achava que você nem lembrasse mais..."

    "A mulher ficou triste, abaixandoa cabeça."

    d"Os demais... Familiares... Preferem não falar sobre elas..."
    d"Mas... Elas foram ótimas mães..."
    d"Eu também sinto muita saudade delas..."

    "Sarah ficou chocada. Pode ter feito realmente uma viajem no tempo. Ou pode ter sido um sonho..."
    "Desviando o olhar, ela escondeu o rosto da mãe."
    "Começou a se sentir culpada... E se tivesse feito algo diferente?"

    b"Não... Ao se fazer uma viajem no tempo... Não pode se alterar o passado..."
    b"Compromete a sua própria existencia..."

    d"... O que você está dizendo? Já sei... Foi essas suas séries."
    d"Você tem vsito muito disso..."
    d"Aposto que foi um sonho."

    b"É... Deve ter sido."
    b"Acho que vou voltar a dormir."

    d"Tudo bem então. Amanhã iremos ao dentista, não esqueça disso."

    b"ok."

    d"Boa noite. Qualquer coisa você me chama, tudo bem?"

    b"... Certo... Valeu mãe."

    d"Que isso. Boa noite."

    hide mae

    "A mulher fechou a porta. Sarah voltou a dormir, cobrindo-se com o cobertor."
    "Fechou os olhos e pensou se tudo foi realmente um sonho..."

    "Fim do jogo! Obrigada por jogar!"


    return
