#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

girdi=str(raw_input("string giriniz: "))

for i in range(len(girdi)+1):
    for c in itertools.combinations(girdi, i):
        print c

#burada itertools'un kendi kombinasyon fonksiyonu kullanılıyor. Bu kombinasyon fonk. string ve kaçlı kombinasyon istendiği yazıldığında
#örneğin combinations("abcd",2) dediğimizde ab ac ad bc bd cd değerlerini geri döndürüyor.
#en üstteki for döngüsüyle (s,0), (s,1) şeklinde olası tüm kombinasyonları yazdırıyor.
#itertools içerisindeki kombinasyon fonksyinuna baktım tam anladım diyemem.
#modül kullanılarak oldukça basit oldu:) Eğer fonksiyonu kendimin yazmamı isterseniz tekrar yazarım.
#kodu yazması oldukça kısa sürdü ancak itertools'un combinations fonksiyonu kurcalayıp anlamaya çalıştığım için yaklaşık 1 saatimi aldı.
