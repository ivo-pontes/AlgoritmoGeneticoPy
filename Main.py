#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:08:52 2018

@author: Ivo Pontes Araújo, Harley Dias Quirino, Elvis Ribeiro
@organization: Universidade Federal do Tocantins - UFT
@project: Algoritmos Genéticos em Python
@class: Main
@license: MIT

The MIT License (MIT)

Copyright (c) Thu Mar 15 22:08:52 2018 Ivo Pontes Araújo

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
from Individuo import Individuo
from Produto import Produto
from AlgoritmoGenetico import AlgoritmoGenetico

if __name__ == '__main__':
    
    produtos = []
    produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    
    espacos = []
    valores = []
    nomes = []
    
    for produto in produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    
    limite = 3
    
    tamanho_populacao = 20
    taxa_mutacao = 0.01
    numero_geracoes = 100
    algoritmoGenetico = AlgoritmoGenetico(tamanho_populacao)
    
    
    resultado = algoritmoGenetico.resolver(taxa_mutacao,numero_geracoes, espacos, valores, limite)
    
    print("\nMelhor Conjunto de Produtos:\n")
    for i in range(len(produtos)):
        if resultado[i] == '1':
            print("Nome: %s R$ %s " % (produtos[i].nome, produtos[i].valor))
            
            
#    algoritmoGenetico.populacao_inicial(espacos, valores, limite)
#    
#    for ind in algoritmoGenetico.populacao:
#        algoritmoGenetico.fitness(ind)
#        
#    
#    algoritmoGenetico.ordenar_populacao()
#    algoritmoGenetico.melhor_individuo(algoritmoGenetico.populacao[0])
#    soma = algoritmoGenetico.somar_avaliacoes()
#    nova_populacao = []
#    probabilidade_mutacao = 0.01    
#    
#    #Construção da Nova Geração
#    for individuos in range(0, algoritmoGenetico.tamanho_populacao,2):
#        pai1 = algoritmoGenetico.selecionar_pai(soma)   
#        pai2 = algoritmoGenetico.selecionar_pai(soma)
#        
#        filhos = algoritmoGenetico.crossover(algoritmoGenetico.populacao[pai1],algoritmoGenetico.populacao[pai2])
#        nova_populacao.append(algoritmoGenetico.mutation(probabilidade_mutacao,filhos[0]))
#        nova_populacao.append(algoritmoGenetico.mutation(probabilidade_mutacao,filhos[1]))
#    
#    algoritmoGenetico.populacao = list(nova_populacao)
#        
#    for individuo in algoritmoGenetico.populacao:
#        algoritmoGenetico.fitness(individuo)
#    
#    algoritmoGenetico.ordenar_populacao()
#    algoritmoGenetico.melhor_individuo(algoritmoGenetico.populacao[0])
#    soma = algoritmoGenetico.somar_avaliacoes() 
#    
#    print("Melhor: %s" % algoritmoGenetico.melhor_solucao.cromossomo, "Valor: %s\n"  % algoritmoGenetico.melhor_solucao.nota_avaliacao)
#    
#    print("Soma das Avaliações %s: " % soma)
#    
#    print("Melhor solução para o problema: %s \n" % algoritmoGenetico.melhor_solucao.cromossomo,
#          "Nota = %s\n" % algoritmoGenetico.melhor_solucao.nota_avaliacao)
    
#    for i in range(algoritmoGenetico.tamanho_populacao):
#        print("*** Indivíduo %s ****\n" %i,
#              "Espaços = %s\n" % str(algoritmoGenetico.populacao[i].espacos),
#              "Valores = %s\n" % str(algoritmoGenetico.populacao[i].valores),
#              "Cromossomo = %s\n" % str(algoritmoGenetico.populacao[i].cromossomo),
#              "Nota = %s\n" % algoritmoGenetico.populacao[i].nota_avaliacao)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    individuo = Individuo(espacos, valores, limite)
#    print("Espaços = %s" % str(individuo.espacos))
#    print("Valores = %s" % str(individuo.valores))
#    print("Cromossomo = %s" % str(individuo.cromossomo))
#
#    print("\nComponentes da carga")
#    for i in range(len(produtos)):
#        if individuo.cromossomo[i] == '1':
#            print("\nNome: %s R$ %s " %(produtos[i].nome, produtos[i].valor))
#    
#    print("\n")
#    
#    algoritmoGenetico = AlgoritmoGenetico()
#    
#    
#    algoritmoGenetico.fitness(individuo)
#    print("Indivíduo 1\n")
#    print("Nota = %s" % individuo.nota_avaliacao)
#    print("Espaço Usado = %s" % individuo.espaco_usado)
#
#    individuo2 = Individuo(espacos, valores, limite)
#    algoritmoGenetico.fitness(individuo2)
#    print("Indivíduo 2\n")
#    print("Nota = %s" % individuo2.nota_avaliacao)
#    print("Espaço Usado = %s" % individuo2.espaco_usado)
#
#    algoritmoGenetico.crossover(individuo, individuo2)
#    
#    individuo = algoritmoGenetico.mutation(0.05, individuo)
#    individuo2 = algoritmoGenetico.mutation(0.05, individuo2)




    