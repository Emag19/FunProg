# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:12:20 2025

@author: ahbpl
"""

def verificar_bissexto(ano):
    if (ano%4==0) and not(ano%100==0) and (ano%400==0):
        return 1
    return 0

def verificar_dia(dia, mes, ano):
    meses = [31, 28+verificar_bissexto(ano), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dia <= meses[mes]

def main():
    data = input("Introduza a data no formato dd/mm/aaaa : ")
    dia, mes, ano = data.split("/")
    
    if verificar_dia(int(dia), int(mes), int(ano)) and int(mes) <= 12:
        print("Data válida.")
    else:
        print("Data inválida.")    

main()