import re

def ValidIP(input:str):
    regex ="^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return True if re.search(regex,input) else False


def ARPQuery(ip):
    bin_ascii=''
    for c in 'ARPQ':
        bin_ascii += format(ord(c), '08b')
    bin_ip =''
    for n in ip.split('.'):
        bin_ip += format(int(n),'08b')
    return bin_ascii + bin_ip


def IP_Package(ori_ip,des_ip):
    package = ""
    for n in des_ip.split('.'):
        package += format(int(n),'08b')
    for n in ori_ip.split('.'):
        package += format(int(n),'08b')
    package += format(0,'08b') + format(0,'08b')
    return package    

# qr = input()
# k = ARPQuery(qr)
# print(k)
# print(len(k))
# print(f"{chr(int(k[0:8],2))}\n{chr(int(k[8:16],2))}\n{chr(int(k[16:24],2))}\n{chr(int(k[24:32],2))}")
# a = chr(int(k[0:8],2)) + chr(int(k[8:16],2)) + chr(int(k[16:24],2)) + chr(int(k[24:32],2))
# print(a)
# print(a == "ARPQ")
# b = f"{int(k[32:40],2)}.{int(k[40:48],2)}.{int(k[48:56],2)}.{int(k[56:64],2)}"
# print(b)
# print(b==qr)