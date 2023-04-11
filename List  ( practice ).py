#    Quyidagi mashqlarni bajaring:
     
    #  ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiritinism    
ismlar = ' Sherzodbek ' , ' Bekmurod ' , ' Nurlan ' 
   
    #  Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(f" Salom {ismlar[2]} , bugun choyxona bormi ? \n{ismlar[1]}, choyxonaga boramizmi ? ")
        
    #  sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [ -10 , 10 , 55 , -22 , 5.1 , 79.1 , 45 , 77 , 99 ]
sonlar2 = []
    #  Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar2 = sonlar.pop(6)
# sonlar2 = sonlar.pop(7)
sonlar2 = sonlar.pop()
sonlar[3] = 5
sonlar[5] = 89.1
sonlar[0] = sonlar[1]
sonlar[2] = sonlar[4]

print(sonlar)
print(sonlar2)
   
    #  t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = [ ' Amir Temur' , ' Alisher Navoiy ' , ' Muhammad Zahriddin Bobur ' ]
z_shaxslar = [ ' Abdikulov sherzodbek ' , ' Fozilov Bekmurod ' , ' Sidiqov Nurlan ' ]
t = t_shaxslar.pop(2)
z = z_shaxslar.pop(2)
   #  Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f" Men tarixiy shaxslardan {t_shaxslar[0]} bilan,\n zamonaviy shaxslardan esa {z_shaxslar[1]} bilan \n suhbat qilishni istardim .")
print(" Men tarixiy shaxslardan " + t +  "bilan,\n zamonaviy shaxslardan esa " + z + " bilan \n suhbat qilishni istardim " )   

   #  friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('Sherzodbek')
friends.append('Nurlan')
friends.append('Bekmurod')
friends.append('Toshpo`lat')
friends.append('Xumoyun')
friends.append('Ravshan')
friends.append('Shahzodbek')
friends.append('Sohib')
friends.append('Shod')

print(friends)
         
   #  Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends = ['Sherzodbek', 'Nurlan', 'Bekmurod', 'Toshpo`lat', 'Xumoyun', 'Ravshan', 'Shahzodbek', 'Sohib', 'Shod']
friends.remove('Sohib')
friends.remove('Shod')
friends.remove('Toshpo`lat')

print(friends)
   #  Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, 'Ozoda')
friends.insert(5, 'E`zoza')
friends.insert(9, 'Zilola')

print(friends)
   #  Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append('Nurlanbek')
mehmonlar.append('Bekmurod')
#mehmonlar = friends.pop(0)

print(mehmonlar)

  