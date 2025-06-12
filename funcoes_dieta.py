import random

###############################################################################
#                                Dieta Otimizada                              #
###############################################################################

#Indivíduo

def gene_dieta(valor_max):
    """Sorteia um valor para uma caixa no problema das caixas 
    não-binárias (usado também para o problema da dieta)
    
    Args: A quantidade máxima de porções por alimento.
    """
    valores_possiveis = range(valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene

#Função objetivo

def funcao_objetivo_dieta(candidato, data, restricoes, valores_maximos):
    """Computa a função objetivo no problema das dietas otimizadas.

    Args:
      candidato: uma lista contendo os valores das porções de cada alimento da dieta diária.
      data: o dataset contendo as informações nutricionais dos alimentos.
      restricoes: uma lista de lista com a informação para cada alimento de: 
      [valor_minimo, valor_maximo, media_do_intervalo].
      valores_maximos: os maiores valores de cada nutriente para penalizar as dietas fora dos intervalos.
    """

    #Código para retornar os valores de cada "nutriente" (caloria, sódio, gorduras, etc) em um indivíduo qualquer (que representa uma dieta com várias porções de alimentos distintos)
    nutrientes_dieta = [0]*len(data.columns[4:])
    indice = 0

    for nutriente in data.columns[4:]: #data.columns = lista dos "nutrientes"
        coluna_nutriente = data[nutriente].values

        for porcao, valor in zip(candidato, coluna_nutriente): #indivíduo é uma lista com porções (de 0 a 3) de alimentos
            nutrientes_dieta[indice] += porcao*valor #obtemos quantos valores para o "nutriente" temos para cada alimento
        
        indice+=1

    fitness = 0
    for valor_nutriente, restricao, maximo_nutriente in zip(nutrientes_dieta, restricoes, valores_maximos):
        distancia = abs(valor_nutriente - restricao[2]) #distancia do nosso indivíduo por valor de nutrientes da média (restricao[2]) do intervalo permitido - essa média é o valor ideal para o nutriente

        if valor_nutriente < restricao[0] or valor_nutriente > restricao[1]: #se for menor que o mínimo ou maior que o máximo estipulados, punimos!
            fitness += (maximo_nutriente * distancia) #punição
            ###OBS: Se der ruim depois - demorar pra convergir ou sla, adicionamos 44 multiplicando a punição do fitnes
        else:
            fitness += distancia
    
    return (fitness, )

#Seleção

def selecao_mista(population, k, tamanho_torneio):
   '''Realiza a seleção pautando-se em dois operadores distintos: 
   Seleção por torneio e Seleção por Amostragem Universal Estocástica (SUS)
   
   Args:
    population: uma lista contendo as dietas candidatas (indivíduos do problema)
    k: número de indivíduos a serem selecionados
    tamanho_torneio: número que representa o tamanho do torneio
   '''
   k1 = k // 2
   k2 = k - k1
    
   selected1 = tools.selTournament(population, k=k1, tournsize=tamanho_torneio)
   selected2 = tools.selStochasticUniversalSampling(population, k=k2)
    
   return selected1 + selected2