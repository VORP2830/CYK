def process_file(file):
  #Função de leitura do arquivo TXT
  with open(file) as f:
    lines = f.readlines()
    return_dict = {}
    for line in lines:
      split_ = line.split("=>") 
      left_ = split_[0].strip()
      right_ = split_[1].strip().replace(" ", "").replace("\n","")
      return_dict[left_] = []
      all_rules = right_.split("|")
      for rule_ in all_rules:
        return_dict[left_].append(rule_)
  return return_dict  

def CYK(palavra, gramatica):
    #Lista vazia para pega o estado inicial
    w = []
    #Primeiro pegamos a quantidade de letras na palavra
    n = len(palavra)
    #Criamos a tabela com base em quantas letras existem
    tabela = [['']*n for _ in range(n)]
    #Fazemos um loop com a quantidade de letras
    for i in range(n):
        #Um loop para pegar as chaves do dicionario
        for c in gramatica.keys():
            #Adiciona todos os estados na lista
            w.append(c)
            #Com a chave do dicionario iremos atras das regras
            for x in gramatica[c]:
                #Se a primeira letra da palavra for igual a regra do arquivo
                if palavra[i] == x: 
                    #Adiciona na tabela se ele n tiver
                    tabela[i][i] = c if not tabela[i][i] else tabela[i][i] + ',' + c
    #Loop que pula de dois em dois ate o numero de letras da palavra
    for l in range(2, n+1):
        #Loop que pega a quantidade de letras da palavra diminui do loop anterior e soma 1
        for i in range(n-l+1):  
            #A variavel j será gerada de acordo com o loop anterior adicionando l do outro loop e diminuindo 1
            j = i+l-1
            #Loop que pula com diferença de i em j
            for k in range(i, j):
                #Loop para ver todas as chaves do dicionario
                for c in gramatica.keys():
                    #Loop para ver todas as regras por chave do dicionario
                    for x in gramatica[c]:
                        #Se a regra tiver 2 letras
                        if len(x) == 2:
                            #Ver se o produto cartesiano e verdadeiro
                            if x in [m+n for m in tabela[i][k].split(',') for n in tabela[k+1][j].split(',')]:
                                #Se a regra da gramatica(S) não estiver na tabela 
                                if not c in tabela[i][j]:
                                    #Adiciona na tabela caso não tenha ainda se não adiciona outra letra
                                    tabela[i][j] = c if not tabela[i][j] else tabela[i][j] + ',' + c
    return w[0] in tabela[0][n-1] 

a = process_file('02.txt')
cyk = CYK('abaab', a)
if(cyk == True):
  print('A palavra pertence a gramatica')
else:
  print('A palavra não pertence a gramatica')