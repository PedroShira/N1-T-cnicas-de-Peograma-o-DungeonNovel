import random
Jogadas = 0
Sala = 1
SalasIniciais = 1,2,3,4,5,7,8
caminho = 0

print('Ah! Então você é o lider da guilda? Seja bem vindo!\n''Aquele ali é o calabouço que dissemos nas cartas, nossos batedores indentificaram devoradores de mentes, seres que dominaram a capacidade de distorcer o próprio espaço tempo para viagens instantâneas, achamos que eles estão planejando um ataque ao reino, por isso chamamos você.\n''Por favor nos ajude!\n\n No mesmo instante você aceitou a proposta')
while (Sala != 9) and (Jogadas <7):
  if Sala in SalasIniciais:
    print('Você entra em uma sala, a porta se fecha e vocês se veem em uma sala cheia de devoradores de mentes, após derrotá-los.\nO ladino percebe um grande número no chão. \n indicando que estão na sala: ', Sala)
    caminho = int(input(
   '\nQual caminho devemos seguir senhor?'
    '\n(Digite 1 para seguir o caminho vermelho ou 2 para o preto)\n'))
    while caminho < 1 or caminho > 2:
     caminho = int(input('\n- Por favor, meu senhor, pare de brincadeira e nos direcione para um caminho existente! \nDisse o Paladino\n\n(Digite 1 para seguir o caminho vermelho ou 2 para o preto)\n'))
    Sala = Sala + caminho
    Jogadas = Jogadas + 1
  elif Sala == 6:
    Sala= Sala + 2
    print('\nVocês entram numa sala vazia com um único corredor, o chão revela que a sala atual tem o número 6 \n"Seguimos em frente senhor." disse seu Paladino.')
  else:
    print('\nVocês atraveçam o portal estranho e viajam para outro lugar.')
    Sala = random.randint (1,5)
if Sala == 9:
  print ('\nVocês chegam a última sala e notam um grande 9 no chão.\nÉ um laboratório e no meio um grande portal ativo mostra um exército enorme de devoradores de mente, seu inventor, acreditando que eles estavam redirecionando o portal para a superficie do reino, grita para desativarem o portal.\nE atravéz de uma grande luta contra os devoradores de mentes que tentam lhes impedir, vocês conseguem finalmente desativar o portal, vencendo os devoradores.\n\n- Muito obrigado meu senhor. Apesar das mortes na batalha final, amanhã comemoraremos a nossa vitória. Hoje deixaremos nossos sobreviventes descansarem e honraremos a coragem daqueles que se foram por nós.\nDisse o Paladino\n.')
elif Jogadas >= 7:
 print("COLAR TEXTO AQUI")