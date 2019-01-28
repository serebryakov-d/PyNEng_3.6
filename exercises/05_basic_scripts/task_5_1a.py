# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#ip_cidr=input('IP address x.x.x.x/y:')
ip_cidr='10.20.34.25/28'

ip_s=ip_cidr.split('/')[0]
mask=int(ip_cidr.split('/')[1])

ip_int=[int(ip) for ip in ip_s.split('.')]
print(ip_int)
ip_bin_s=''.join(['{:08b}'.format(A) for A in ip_int])
print(ip_bin_s)

mask_bin_s=mask*'1'+(32-mask)*'0'
mask_s_l=[mask_bin_s[8*n:8*n+8] for n in range(4)]
mask_n_l=[int(S,2) for S in mask_s_l]

nw=[(ip_bin_s[n] AND mask_bin_s[n]) for n in range(31)]
print(nw)

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
print(nw_template.format(ip_int[0],ip_int[1],ip_int[2],ip_int[3]))
#print(nw_template.format(*ip_int))
print(mask_template.format(*mask_n_l,*mask_s_l))
