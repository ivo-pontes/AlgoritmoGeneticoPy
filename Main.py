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
from matplotlib import pyplot
from Produto import Produto
from AlgoritmoGenetico import AlgoritmoGenetico

import sys
sys.path.append('$HOME/anaconda3/lib/python3.6/site-packages/')

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
    
    
    pyplot.plot(algoritmoGenetico.lista_solucoes)
    pyplot.title("Acompanhamento dos valores")
    pyplot.show()



    