#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#ip_addr=input('Enter dotted decimap IP address:')
#ip_addr='65.11.11.11.45'

correct_ip=False
while correct_ip==False:
    ip_addr=input('Enter dotted decimal IP address:')
    ip_l=ip_addr.split('.')

    digit_num=True
    for N in ip_l:
        digit_num*=N.isdigit()

    try:
        digit_val=True
        for N in ip_l:
            digit_val*=(int(N) in range(0,256))
    
        if (len(ip_l)==4) and digit_num and digit_val:
            ip1=int(ip_addr.split('.')[0])
            if ip1 >= 1 and ip1 <= 223:
                result='unicast'
                correct_ip=True
            elif ip1 >= 224 and ip1 <= 239:
                result='multicast'
                correct_ip=True
            elif ip_addr=='255.255.255.255':
                result='local broadcast'
                correct_ip=True
            elif ip_addr=='0.0.0.0':
                result='unassigned'
                correct_ip=True
            else:
                result='unused'
                correct_ip=True
        else:
            result='Incorrect IPv4 address'
            print(result)
    except ValueError:
        result='Incorrect IPv4 address'
        print(result)

print(result)

