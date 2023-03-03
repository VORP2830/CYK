# CYK

# A função process_file
A função process_file(file) lê um arquivo de texto file e retorna um dicionário onde as chaves são os símbolos não-terminais e os valores são listas de regras produzidas por esses símbolos, lidas a partir do arquivo.

# A função CYK
A função CYK(palavra, gramatica) implementa o algoritmo CYK para verificar se uma dada palavra palavra pertence a uma gramática representada por um dicionário gramatica no formato retornado pela função process_file. A função retorna True se a palavra pertence à gramática e False caso contrário.

# O algoritmo
O algoritmo CYK funciona através da construção de uma tabela de símbolos não-terminais que podem gerar as subpalavras de palavra em todas as posições possíveis. O processo é dividido em duas etapas. Na primeira etapa, a tabela é preenchida para subpalavras de tamanho 1. Na segunda etapa, a tabela é preenchida para subpalavras de tamanho maior que 1, construindo a partir das subpalavras já preenchidas anteriormente. Ao final, verifica-se se o símbolo inicial da gramática é capaz de gerar a palavra completa.

Segue abaixo uma descrição mais detalhada de cada função e de suas entradas e saídas:
# Função process_file(file)
Entrada

    file: nome do arquivo de texto a ser lido.
    

Saída

    return_dict: um dicionário em que as chaves são símbolos não-terminais da gramática lida do arquivo e os valores são listas de regras produzidas por esses símbolos.

# Função CYK(palavra, gramatica)
Entradas

    palavra: uma string representando a palavra a ser verificada se pertence à gramática.
    gramatica: um dicionário representando a gramática no formato retornado pela função process_file.

Saída

    True se a palavra pertence à gramática, False caso contrário.
    
# Exemplo de uso

