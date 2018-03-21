#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:41:02 2018

@author: Ivo Pontes Araújo, Harley Dias Quirino, Elvis Ribeiro
@organization: Universidade Federal do Tocantins - UFT
@project: Algoritmos Genéticos em Python
@class: AlgoritmoGenetico
@license: MIT

The MIT License (MIT)

Copyright (c) Sat Mar 17 15:41:02 2018 Ivo Pontes Araújo

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from random import random
from Individuo import Individuo

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        print("Algoritmo Genético\n")
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0 #melhor solução = maior nota e no limite
        
    def populacao_inicial(self, espacos, valores, limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))
        self.melhor_solucao = self.populacao[0]
        
    def ordenar_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def somar_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    def visualizar_geracao(self):
        melhor = self.populacao[0]
        print("G: %s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                                melhor.nota_avaliacao,
                                                                melhor.espaco_usado,
                                                                melhor.cromossomo))
        
    def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos):
        self.populacao_inicial(espacos, valores, limite_espacos)
        
        #Primeira Avaliação
        #Criar População Inicial
        for individuo in self.populacao:
            self.fitness(individuo)
        
        self.ordenar_populacao()
        self.visualizar_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.somar_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                #Selcionar 2 Pais
                pai1 = self.selecionar_pai(soma_avaliacao) 
                pai2 = self.selecionar_pai(soma_avaliacao)
    
                #Criar Filhos através de CrossOver
                filhos = self.crossover(self.populacao[pai1],self.populacao[pai2])
                #Criar Nova Populacao com Mutação
                nova_populacao.append(self.mutation(taxa_mutacao, filhos[0]))
                nova_populacao.append(self.mutation(taxa_mutacao, filhos[1]))
            
            self.populacao = list(nova_populacao)
            
            #Nova Avaliação com Novos Indivíduo(população)
            for individuo in self.populacao:
                self.fitness(individuo)
                
            self.ordenar_populacao()
            self.visualizar_geracao()
                
            melhor = self.populacao[0]
            self.melhor_individuo(melhor)
         
        print("\nMelhor Solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao, self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.espaco_usado, self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo
    
    #Utilização do Método da Roleta
    def selecionar_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    """
    Função de Avaliação - Fitness
    Tem a função de ser a medida de qualidade que mensura como o cromossomo
    resolve o problema.
    Verifica-se se a solução é aceitável e se pode ser utilzada para a evolução.
    """
    def fitness(self, individuo):
        #print("\nFunção de Avaliação\n")
        nota = 0 #Nota da Avalização é o Somatório dos Valores da Carga
        soma_espacos = 0
        
        for i in range(len(individuo.cromossomo)):
            if individuo.cromossomo[i] == '1':
                nota += individuo.valores[i]
                soma_espacos +=  individuo.espacos[i]
        
        
        if soma_espacos > individuo.limite_espacos:
            nota = 1
        
        individuo.nota_avaliacao = nota
        individuo.espaco_usado = soma_espacos
        
        
    """
    Crossover - Reprodução - Cruzamento
    Combina pedaços do cromossomo de dois progenitores, gerando filhos mais 
    aptos, e consequentemente, as populações de novas gerações tendem a evoluir.
    O Crossover representa a reprodução sexuada, pois cada filho terá informações
    que vêm dos dois pais, pois a reprodução assexuada, cada filho é idêntico a 
    seu progenitor.
    Método utliza operação de crossover de um ponto.
    """
    def crossover(self, individuo1, individuo2):
        #print("Função de cruzamento - Crossover")        
        corte = round(random() * len(individuo1.cromossomo))
        
        #Cortar até o ponto de corte para o cromossomo do filho
        filho1 = individuo2.cromossomo[0:corte] + individuo1.cromossomo[corte::]
        filho2 = individuo1.cromossomo[0:corte] + individuo2.cromossomo[corte::]
        
        filhos = [Individuo(individuo1.espacos, individuo1.valores, individuo1.limite_espacos, individuo1.geracao + 1),
                  Individuo(individuo1.espacos, individuo1.valores, individuo1.limite_espacos, individuo1.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
        
        
    """
    Mutation - Mutação
    A mutação cria diversiade mudando aleatoriamente os genes dos indivíduos
    """
    def mutation(self, taxa_mutacao, individuo):
        #print("\nFunção de mutação - Mutation\n")
        #print("Antes %s " % individuo.cromossomo)
        for i in range(len(individuo.cromossomo)):
            if random() < taxa_mutacao:
                if individuo.cromossomo[i] == '1':
                    individuo.cromossomo[i] = '0'
                else:
                    individuo.cromossomo[i] = '1'
        #print("Depois %s " % individuo.cromossomo)
        return individuo
        
        
        
        
        
        
        
        
        
        
        
        
        