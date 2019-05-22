# -*- coding: utf-8 -*-
"""Desafio_rato_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s78bWw9_NFv7Gu0SIeODdGxpmTi1yk1H
"""

apps=[]
nomes=[]
categorias=[]
avaliacao=[]

sizes=[]
tamanhos=[]
maiores_cats=[]
dict= {}
lista=['1','2','3','4','5']

with open("googleplaystore.csv",'r', encoding="utf-8") as file:
    texto=file.readlines()
    texto=texto[1:]
    for linha in texto:
        app=linha.split(",")
        apps.append(app)

"""**1 - Quantos aplicativos existem? **"""

for nome in apps: nomes.append(nome[0])   
print(len(nomes))
print(len(set(nomes)))

"""**2 - Quais são as categorias**"""

with open("googleplaystore.csv",'r', encoding="utf-8") as file:
    for app in file.readlines(): categorias.append(app.split(',')[1])
    
    categorias.remove('Category')
    print(len(set(categorias)))

"""**3 - Qual a maior avaliação**"""

with open("googleplaystore.csv",'r', encoding="utf-8") as file:
    avaliacao=[]
    avaliac=[]

    for app in file.readlines():
        avaliacao.append(app.split(',')[2])
        
lista=['1','2','3','4','5']
for av in avaliacao:
    num=av[0]
    if num in lista:
        avaliac.append(av)

        
avaliac.remove('19')
maxi=max(avaliac, key=float)
print(maxi)

"""**4 - Qual aplicativo com maior tamanho?**"""

with open("googleplaystore.csv",'r', encoding="utf-8") as file:
    for app in file.readlines(): tamanhos.append(app.split(',')[4])
    
    lista=['1','2','3','4','5','6','7','8','9']
    for app in tamanhos:
        pri=app[0]
        last=app[-1]
        if pri in lista:
            if (last=='M'):
                sizes.append(app[:-1])
                        
    maxi=max(size,key=float)
    print(maxi+" MB")

"""**5 - Qual a categoria com mais aplicativos? **"""

with open("googleplaystore.csv","r",encoding="utf-8") as file:

    
    for app in file.readlines():
        maiores_cats.append(app.split(',')[1])
        
    
    cnt, item = 0, ''
    for app in maiores_cats:
        dict[app] = dict.get(app, 0)+1
        
        if dict[app] >= cnt :
            cnt, item = dict[app], app
print(maiores_cats.count("FAMILY"),(item))

"""**6 - Qual a média de avaliação em cada categoria?**"""

print(categorias)
print(avaliac)
