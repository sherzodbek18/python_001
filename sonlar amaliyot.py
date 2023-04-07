#       Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
  
    #  Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
a = int(input( ' Istagan sonni kiriting :\n>>> ' ))
c = a**2
x = a**3
print(f"{a} ning kvadrati {c} ga teng \n{a} ning kubi {x} ga teng")
  
    #  Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
b = int(input( ' Yoshingiz nechida ?\n>>> ' ))
v = 2023 - int(b)
print(f" Siz {v} yilda tug`ilgansiz !") 
   
  
   #  Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
w = float(input( ' Birinchi sonni kiriting : ' ))
e = float(input( ' Ikkinchi sonni kiriting : ' ))
r = float(w) + float(e)
z = float(w) - float(e)
o = float(w) * float(e)
d = float(w) / float(e)
print(w , ' + ' , e , ' = ' , r)
print(w , ' - ' , e , ' = ' , z)
print(w , ' * ' , e , ' = ' , o)
print(w , ' / ' , e , ' = ' , d)   