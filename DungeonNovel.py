import random
Jogadas = 0
Sala = 1
SalasIniciais = 1,2,3,4,5,7,8
caminho = 0

print('COLAR TEXTO AQUI')
while (Sala != 9) and (Jogadas <7):
  if Sala in SalasIniciais:
    print('COLAR TEXTO AQUI', Sala)
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