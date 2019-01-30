#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ip_cidr=argv[1]
#ip_cidr=input('IP address x.x.x.x/y:')
#ip_cidr='10.20.34.25/28'

ip_s=ip_cidr.split('/')[0]
mask=int(ip_cidr.split('/')[1])

ip_int=[int(ip) for ip in ip_s.split('.')]
ip_bin_s=''.join(['{:08b}'.format(A) for A in ip_int])

mask_bin_s=mask*'1'+(32-mask)*'0'
mask_s_l=[mask_bin_s[8*n:8*n+8] for n in range(4)]
mask_n_l=[int(S,2) for S in mask_s_l]

nw_bin_s=''.join([str(int(ip_bin_s[n])*int(mask_bin_s[n])) for n in range(32)])
nw_s_l=[nw_bin_s[8*n:8*n+8] for n in range(4)]
nw_n_l=[int(S,2) for S in nw_s_l]   #network in decimal

#define template with argument numbers 0-3
nw_template='''
Network:
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b} 
'''

mask_template='''
Mask:
{:<8} {:<8} {:<8} {:<8} 
{:<8} {:<8} {:<8} {:<8} 
'''
#print(nw_template.format(ip_int[0],ip_int[1],ip_int[2],ip_int[3]))
#print(nw_template.format(*ip_int))
print(nw_template.format(*nw_n_l))
print(mask_template.format(*mask_n_l,*mask_s_l))
