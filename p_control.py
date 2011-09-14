#!/usr/bin/python
# -*- coding: utf-8 -*-

parametreler=[ ]
while True:

    p=input("Fonksiyon parametresini girin: ")
    print "Fonksiyon parametrelerinin hepsini girdiyseniz 'ç' yazın!!"
    if p=='ç':
        break
    parametreler.append(p)
for _p in parametreler:
    if isinstance(_p,basestring)!=True:
         print "False"
         break

else:print"True"

#yarım saat-1 saat arası bi zamanımı aldı. 
#parametreleri girdiğimizde eğer içlerinden biri string değilse False hepsi string ise True yazıyor.
#isinstance içinde basestring yerine str de kullanabilirdim ama o zaman unicode değerleri false olarak veriyor. basestring tüm string türleri için true döndürdü iyi oldu.

