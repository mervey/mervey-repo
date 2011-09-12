#!/usr/bin/python
# -*- coding: utf-8 -*-

#girdi=raw_input("Bir şeyler giriniz: ")
#girdi=str(girdi)
#girdi=girdi[::-1 ]
#print girdi

# yada

girdi=raw_input("Bir şeyler giriniz: ")
girdi=str(girdi)
girdi=list(girdi)
girdi.reverse()
girdi=''.join(girdi)
print girdi

#verilen stringi tersten yazan bulduğum iki yöntemide yazdım.
#Yaklaşık 15dk mı aldı.
