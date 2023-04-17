   #  Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Sherzodbek' , 'Nurlan' , 'Bekmurod' , 'Xumoyun' , 'Ravshan']

for ism in ismlar :
    print(f" Salom {ism} ") 

   #  Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
a = len(ismlar)
print(f"Kod {a} marta takrorlandi !")

   #  10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_son = list(range(10 + 1 , 100 , 2 ))
for toq in toq_son :
    print(f" {toq ** 3}")
print(toq_son)

   #  Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
print('6 ta eng sevimli kinolaringizni kiriting :')

w = input('1 chi sevimli kinoingizni kiriting :')
e = input('2 chi sevimli kinoingizni kiriting :')
r = input('3 chi sevimli kinoingizni kiriting :')
z = input('4 chi sevimli kinoingizni kiriting :')
o = input('5 chi sevimli kinoingizni kiriting :')
d = input('6 chi sevimli kinoingizni kiriting :')

kinolar = []

kinolar.append(w)
kinolar.append(e)
kinolar.append(r)
kinolar.append(z)
kinolar.append(o)
kinolar.append(d)

print(kinolar)   
 
kinolar1 = []  

print('5 ta eng sevimli kinolaringizni kiriting !')

for s in range(5):
    kinolar1.append(input(f" {s+1} chi kinoingizni kiriting : "))

print(kinolar1)

   #  Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odamlar = []
v = int(input('Bugun nechta odam bilan suhbatlashdingiz ? >>>'))

for u in range(v) :
    odamlar.append(input(f" {u+1} - suhbat qilgan odamingiz kim edi : "))
print(odamlar)


