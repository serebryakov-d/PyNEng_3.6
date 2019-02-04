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

ip_addr=input('Enter dotted decimap IP address:')
#ip_addr='65.11.11.11.45'

ip_l=ip_addr.split('.')
digit_num=True
for N in ip_l:
    digit_num*=N.isdigit()

if (len(ip_l)==4) and digit_num:
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
else:
    result='Incorrect IPv4 address'

print(result)
