#!/usr/bin/python
# -*- coding: utf-8 -*-


#kendimeNot: set() harika bişi:)
#15dk aldı.

list1=list(raw_input("Bir şeyler giriniz(Örn;abcd123): "))
list2=list(raw_input("Bir şeyler daha giriniz(Örn;124abf): "))

# sadece list1'in list2'den farkını istiyorsak

print list(set(list1)-set(list2))

# iki listedede ortak olmayan tüm elemanları istiyorsak

print list(set(list1)-set(list2))+list(set(list2)-set(list1))


