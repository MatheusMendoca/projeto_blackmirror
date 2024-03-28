pergunta = -1


while(pergunta != 0 ):
     pergunta = input(f'''
============== B L A C K  M I R R O R ========================================
    1 QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO
    2 QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO
    3 QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISODIO
    4 COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
    5 QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
    6 QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR
    7 O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.
                 SAIR
==============================================================================
escreva a sua pergunta =>''')
     if(pergunta == "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO"):
        print("jona")
     elif(pergunta == "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO"):
        print(" mona jovadi hails") 
     elif(pergunta == "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISODIO"):
        print("steamberry")
     elif(pergunta == "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"):
        print("foi asistir steamberry com noivo")
     elif(pergunta == "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"):
        print(f'''
           ela ficou asustada è muito desesperada é chatiada repledor com 
           nevorssimo para amonstra a verdade
           tenda a processar a serie por difamaçao
''')
     elif(pergunta == "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR"):
         print(f'''
          expossição da vida pessoal ao publico todo mundo achando que conhecer ela mas
 so conhecer um personagem que foi criado serie para pessoas que é mal acaba tadando ela igual ao personagem
 ao aceitar temos e codição sem ler as cosenquencia eles ferram com a vida dela
 tenta atair a atençao da atriz da serie 
''')
     elif(pergunta == "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."):
         print(f'''
          era uma realidade inventada por um computado
          ela destruir o computado passa viver a sua vida e viver o seu sonho
''')
     elif(pergunta == "SAIR"):
         print("obrigado volte sempre")
         break
     else:
         print("nao exitem essa pergunta , por favor pergunte novamente")
    