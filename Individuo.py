#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:00:10 2018

@authors: Ivo Pontes Araújo, Harley Dias Quirino, Elvis Ribeiro
@organization: Universidade Federal do Tocantins - UFT
@project: Algoritmos Genéticos em Python
@class: Indivíduo
@license: MIT

The MIT License (MIT)

Copyright (c) Thu Mar 15 22:00:10 2018 Ivo Pontes Araújo

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

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.geracao = geracao
        self.nota_avaliacao = 0
        self.cromossomo = [] #Lista vazia
        self.espaco_usado = 0
        
        #Inicialização Aleatória dos Produtos
        for i in range(len(espacos)):
            if random() < 0.5: #random retorna de 0 a 1
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
        #print(self.cromossomo)