#!/usr/bin/python
# -*- coding: utf-8 -*-

listeler=[ ]

while True:
    liste=str(raw_input("bir şeyler giriniz(Örn:abcd): "))
    print "yeterli sayıda liste girdiyseniz 'bitti' yazın!!"

    if liste=='bitti':
       break
    listeler.append(liste)
    print listeler

tmp=listeler[0        ]
for i in range(0,len(listeler)):
    tmp=list(set(list(listeler[i]))&set(list(tmp)))
print tmp

#1.5-2 saat civarında yaptım.
