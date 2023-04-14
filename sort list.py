#  O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = [ 'Amerika' , 'Turkiya' , 'Fransiya' , 'Argentina' , 'Shvetsariya' , 'Golandiya' , 'Germaniya' , 'Shvetsiya' , 'Vengirya' ]

print(davlatlar)

   #  Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

   #  sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

   #  sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar , reverse = True))

   #  Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

   #  reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()

print(davlatlar)

   #  sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()

print(davlatlar)

davlatlar.sort(reverse = True)

print(davlatlar)
   #  120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar_juft = list(range(120 , 1200 +2 , 2 ))

print(sonlar_juft)

   #  Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar_juft))

   #  Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
a = max(sonlar_juft) - min(sonlar_juft)

print(a)

   #  Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar_juft))

   #  Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
sonlar_juft1 = sonlar_juft[:]
o = sonlar_juft1[ 0 : 20 ] 
k = sonlar_juft1[ 271 : 291 ]
e = sonlar_juft[ 521 : 541 ]

print(o)
print(k)
print(e)

print(len(o))
print(len(k))
print(len(e))

   #  taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh' , 'xonim' , 'manti' , 'chuchvara' , 'lag`mon' , 'lapsha']

   #  nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
   
   #  yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('osh')
nonushta.remove('lag`mon')
nonushta.remove('lapsha')
nonushta.append('Saryog`')
nonushta.insert(0 , 'Shirin choy')
nonushta.append('Issiq non')

   #  Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(nonushta)
print(taomlar)  
   
   #  Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = ( 'Shirin choy', 'xonim', 'manti', 'chuchvara', 'Saryog`', 'Issiq non' )
nonushta[0] = 'qaymoq va non'    

#TypeError: 'tuple' object does not support item assignment <<< Mana shunday ko`rinishdagi xatolik beradi chunki tuple ko`rnishdagi listlarga o`zgartirish kiritib bo`lmaydi !  