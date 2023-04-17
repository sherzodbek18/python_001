#  Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for c in cars :
 if c == 'gm' :
    print(c.upper())
 else :
    print(c.capitalize())

   #  Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
for c in cars :
 if c != 'gm' :
    print(c.capitalize())
 else :
    print(c.upper())
 
   #  Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
a = input('Login isminigizni kiriting :') 

if a.lower() == 'admin' :
    print(' "Xush kelibsiz, Admin. Foydalanuvchilar ro`yxatini ko`rasizmi?" ')
else:
    print(f"Xush kelibsiz, {a}!")
     
   #  Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
w = input('Birinchi sonni kiriting :')   
e = input('Ikkinchi sonni kiriting :')   

if w == e :
    print(' Sonlar teng ekan ! ')

   #  Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
r = int(input('Ixtiyoriy sonni kiriting :'))

if r > 0 :
    print('Musbat son ekan !')
else :
    print('Manfiy son ekan !')    

   #  Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
p = int(input('Ixtiyoriy sonni kiriting :'))

if p > 0 :
    print(p**2)
else :
    print('Musbat son kiriting !')    
   