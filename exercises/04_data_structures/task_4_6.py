# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
route_l = ospf_route.split()
print(route_l)
print("{:19} {:>19}".format('Protocol:','OSPF'))
print("{:19} {:>19}".format('Prefix:',route_l[1]))
print("{:19} {:>19}".format('AD/Metric:',route_l[2]))
print("{:19} {:>19}".format('Next-Hop:',route_l[4][0:-1]))
print("{:19} {:>19}".format('Last update:',route_l[5][0:-1]))
print("{:19} {:>19}".format('Outbound interface:',route_l[6]))

