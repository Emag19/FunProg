# -*- coding: utf-8 -*-
"""
Created on Wed May  7 17:20:05 2025

@author: ahbpl
"""

ficheiro = open("viagem.txt","w")
dados= "999\n1005 0.9\n1013 3.47\n1015 0.3\n1027 2\n1033 1\n1120 5\n1155 4\n1271 27\n1291 6\n1308 1.7\n1372 8.4"
ficheiro.write(dados)
ficheiro.close()

ficheiro = open("viagem.txt","r")
trajetos = ficheiro.readlines()
ficheiro.close()

começo = float(trajetos.pop(0))
paragem = começo
medias = []
gastos = 0

for trajeto in trajetos:
    pt_paragem = trajeto.split()
    fim = float(pt_paragem[0])
    medias += [round(float(pt_paragem[1])*100/(fim-paragem),2)]
    gastos += float(pt_paragem[1])
    paragem = fim

m_tj = ""
for media in medias:
    m_tj += "\n"+str(media)
    
print("As médias de combustivel gasto (em 1L/100km) por ordem são:"+m_tj)
print("E a média total é {}.".format(round(gastos*100/(fim-começo),3)))