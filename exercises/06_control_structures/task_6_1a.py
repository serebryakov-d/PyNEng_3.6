#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#ip_addr=input('Enter dotted decimap IP address:')
ip_addr='365.11.11.11'
ip_l=ip_addr.split('.')
dotted=False
if 

ip1=int(ip_addr.split('.')[0])
if ip1 >= 1 and ip1 <= 223:
    result='unicast'
elif ip1 >= 224 and ip1 <= 239:
    result='multicast'
elif ip_addr=='255.255.255.255':
    result='local broadcast'
elif ip_addr=='0.0.0.0':
    result='unassigned'
else:
    result='unused'

print(result)
