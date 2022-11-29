
ora=int(input("Hány órás visszaszámlálást tervezünk? "))
számla=0
számla=ora
while ora !=0:
    print(f"Visszasámlálás: {ora}")
    fuggesztes=input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    if fuggesztes == 'i':
        számla+=1
    ora-=1
    if ora == 0 and fuggesztes == 'i':
        ora+=1
print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {számla}.")