import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()
count = 0

while len(hrac_volby) <= 2 and len(pocitac_volby) <= 2:
    hrac_ = random.randint(1,3)
    pocitac_ = random.randint(1,3)
    hrac_volby.append(moznosti[hrac_ - 1])
    pocitac_volby.append(moznosti[pocitac_ - 1])
   
print(hrac_volby)
print(pocitac_volby)