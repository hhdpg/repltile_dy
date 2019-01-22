import operator as op
with open('C:/usr/BMS.txt','r') as f:
    data = f.readlines() # txt中所有字符串读入data
    mysql_data = []
    for line in data:
        s = line.strip('\n')
        mysql_data.append(s)
    # print(mysql_data)
PMS_data = {'plc': 100.0, 'tim': '1547546025938', 'vla': 232.2, 'vbc': 384.6, 'comErr': 0, 'slt': 121.92, 'pmf': 50.0, 'pfc': 99.87, 'sla': 121.92, 'vlb': 232.0, 'slc': 121.92, 'qla': 1.0, 'pfb': 99.98, 'pfa': 99.99, 'mamd': 162.48, 'ilb': 12.64, 'plb': 100.0, 'ila': 32.54, 'qlb': 1.0, 'plt': 66.7, 'md': 82.62, 'vlc': 230.0, 'pla': 100.0, 'vab': 383.2, 'ilc': 56.35, 'pft': 99.45, 'qlc': 1.0, 'qlt': 1.0, 'vca': 382.4, 'slb': -121.92}
PCS_data = {'pcf': 0.0, 'qaf': 0.0, 'bsh': 0, 'pdc': 35.32, 'bds': 0, 'pos': 0, 'fre_c': 0.0, 'pgs': 1, 'idc': -62.65, 'icf': 0.0, 'pss_b1': 0, 'bsl': 1, 'vab': 0.0, 'pbf': 0.0, 'ptf': 28.0, 'dep': 0.0, 'pss_b2': 0, 'pff': 0.0, 'qbf': 0.0, 'pss_b0': 1, 'deq': 0.0, 'stf': 0.0, 'qcf': 0.0, 'psl': 0, 'vdc': 725.0, 'err': '0164186400050008001800000007001515A80001', 'ibf': 0.0, 'pss': 1, 'vca': 0.0, 'paf': 0.0, 'tim': '1547602173071', 'pft': 0, 'qtf': 0.0, 'iaf': 0.0, 'ceq': 0.007778, 'bcs': 0, 'cep': 0.008532, 'fre_b': 0.0, 'vbc': 0.0, 'comErr': 0, 'pat': 45.3, 'pqc': 0.0, 'ppc': 28.0, 'pam': 0, 'fre_a': 0.0}
BMS_data = {'bsi': 1, 'vcmax': 733.0, 'ctminc': 4, 'cyc': 4000, 'ctmin': 28.8, 'bss': 1, 'cev': {'4': 3.326, '2': 3.321, '3': 3.42, '1': 3.32, '5': 3.334}, 'rech': 1, 'bat': 35.5, 'cvminc': 2, 'bsd': 1, 'cap': 108, 'soh': 98, 'res': 98000, 'ctmaxc': 3, 'bnc': 0, 'comErr': 0, 'cvmax': 3.4, 'tim': '1547602891060', 'cvmaxc': 1, 'bsc': 1, 'vdcmin': 610.2, 'ctmax': 40.1, 'idcmax': -55.55, 'cur': 55.65, 'vol': 720.0, 'bse': 0, 'recl': 32464, 'bsa': 0, 'soc': 61, 'bir': 30000, 'icmax': 66.66, 'cvmin': 3.34, 'bsp': 0, 'bndc': 0, 'cet': {'4': 27.8, '2': 25.5, '3': 26.8, '1': 28.8, '5': 25.7}}
redis_data = []
for a in BMS_data:
    # print(a)
    redis_data.append(a)
aaa =[]
# print(mysql_data)
# print(redis_data)
for m in mysql_data:
    for r in redis_data:
        # print(r)
        if op.eq(m,r):
            # print(m)
            aaa.append(m)
print(aaa)
for r in redis_data:
    tag = False
    for a in aaa:
        if r == a:
            tag = False
d = list(set(redis_data).difference(set(aaa)))
for dd in d:
    print(dd)