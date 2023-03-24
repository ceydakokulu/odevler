import numpy as np
import random

#soru1) Manuel değerleri el ile girerek 3 boyutlu bir array oluşturup bir değişkene atayın.
#Ardından 3 boyutlu olup olmadığına bakmak için dimension'ını kontrol edin
a= np.array([[[2,3,4],
              [5,6,7],
              [8,9,10]]])
print(a)
print(a.ndim)

#soru2) 34, 40, 46, 52... 112 şeklinde devam eden 1 boyutlu bir array oluşturun.
b= np.arange(34,118,6)
print(b)

#soru3) 50-500 arasında lineer artış gösteren 91 tane tam sayıdan oluşan bir array oluşturun.(dtype'ı int olsun)
c= np.linspace(50,500,91, dtype=int)
print(c)

#soru4) 100(10**2) ile 10000(10**5) arasında logaritmik artış gösteren 8 sayıdan oluşan bir array oluşturun.
d= np.logspace #yapamadım
print(d)

#soru5) 0-8 arasındaki ardışık tam sayılardan oluşan(0 ve 8 dahil toplam 9 değer) 3x3 shape'inde bir matris oluşturun.
e= np.arange(0,9).reshape(3,3)
print(e)

#soru6) 6x6 formatında bir sıfır matrisi oluşturun. (dtype'ı int olsun)
f= np.zeros((6,6), dtype='int')
print(f)

#soru7) 4x4 formatında bir bir matrisi oluşturun. (dtype'ı int olsun)
g= np.ones((4,4), dtype=int)
print(g)

#soru8) 8x8 formatında bir birim matris oluşturun. (Sadece sol köşegeni 1 geri kalan değerleri 0 olan matris'e birim matris deniyor.) (dtype'ı int olsun)
h= np.eye(8, dtype=int)
print(h)

#soru9) 5x5 formatında bir köşegen matrisi oluşturun (Sadece sol üstten sağ alta doğru olan köşegendeki değerleri 3 olsun diğer bütün değerleri 0)
#(Bunu henüz görmediniz ama birim matrise benziyor, sadece köşegen değerleri 1 değil 3 olacak. Bir şeyler düşünün)
j= np.zeros((5,5))
for i in range(5):
    j[i,i]=3
print(j)

#soru10) np.random modülünden uygun fonksiyonu kullanarak 0-1 arasında toplam 6 tane değerden oluşan 1 boyutlu bir array oluşturun.
k= np.random.rand(6)
print(k)

#soru11) np.random modülünden uygun fonksiyonu kullanarak 50-100 arasındaki(50 ve 100 dahil) tam sayılardan 10 tanesiyle oluşan
# (5,2) shape'inde bir array oluşturun. Ardından bu arrayin shape'ini kontrol edin.
l= np.random.randint(50,101,(5,2))
print(l)
print(l.shape)

#soru12) np.random modülünden uygun fonksiyonu kullanarak 100-1000(1000 dahil değil) arasındaki tam sayılardan rastgele 50 tanesinden oluşan
# (2,5,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in dimension'ını(boyutunu) ve shape'ini kontrol edin.
m= np.random.randint(100,1000, (2,5,5))
print(m)
print(m.ndim)
print(m.shape)

#soru13) np.random modülünden uygun fonksiyonu kullanarak 0-100(0 ve 100 dahil) arasındaki tam sayılardan 10 tane seçerek bir array oluşturun.
# Bu array'in maximum, mininmum değerlerine ve bu değerlerin indexlerine bakın.
n= np.random.randint(0,101,10)
print(n)
print(n.max())
print(n.min())
print(n.argmax())
print(n.argmin())

#soru14) np.random modülünden uygun fonksiyonu kullanarak 300-500(300 ve 500 dahil) arasındaki tam sayılardan 20 tane seçerek
# (2,2,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in içindeki 20 tam sayı arasından maximum ve minimum değerleri
# manuel olarak tespit edin ve indexleme yaparak çekmeye çalışın.
o= np.random.randint(300,501, (2,2,5))
print(o)
#yani bu sürekli degisir diye düsünüyorum su an bende cıkan sonuclar bunlar
#[[[345 336 405 421 343]
# [492 458 411 365 419]]

# [[458 414 390 311 326]
# [449 395 406 454 500]]]
print(o[1,1,4])
print(o[1,0,3])

#soru15) 0-50(50 dahil) arasındaki ardışık tam sayılardan oluşan bir array oluşturun. Ardından bu arrayin 20. ve 35. indexleri arasındaki
# değerleri 500'e eşitleyin ve yeni oluşan array'i ekrana yazdırarak broadcasting işleminin yapılıp yapılmadığını test edin.
p= np.arange(51)
print(p)
print(p[21:35])
p[21:35]= 500
print(p)