#     Quyidagi mashqlarni bajaring:
    #  Quyidagi o'zgaruvchilarni yarating: 
    #  kocha="Bog'bon"
    #  mahalla="Sog'bon"
    #  tuman="Bodomzor" 
    #  viloyat="Samarqand"
    #  Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
    #  Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"
print(kocha + ' ko`chasi, ' + mahalla + ' mahallasi, ' + tuman + ' tumani, ' + viloyat + ' viloyati' )

    #  Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
#a = input('Qaysi ko`chada iste`qomat qilasiz :')
#s = input('Qaysi  mahallada iste`qomat qilasiz :')
#d = input('Qaysi  tumanda iste`qomat qilasiz :')
#f = input('Qaysi  viloyatda iste`qomat qilasiz :')
#print( a + ' ko`chasi, \n ' + s + ' mahallasi, \n ' + d + ' tumani, \n ' + f + ' viloyati .' )

    #  Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing

    #  Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = ' Bog`bon ko`chasi, Sog`bon mahallasi, Bodomzor tumani, Samarqand viloyati '
    
    #  manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(f"  upper metodidan foydalandim :\n {manzil.upper()}  \n  title metodidan foydalandim : \n {manzil.title()}  \n  capitalize metodidan foydalandim : \n {manzil.capitalize()}  \n  lower metodidan foydalandim : \n {manzil.lower()}")
