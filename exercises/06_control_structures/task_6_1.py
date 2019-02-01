#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_addr=input('Enter dotted decimap IP address:')
#ip_addr='365.11.11.11'

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
