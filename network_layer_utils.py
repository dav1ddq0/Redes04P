import re

handler = None

def check_PackageCondition(host):
    for packet in host.packets:
        if packet.mac_des != None:
            setupFrameFromPacket(packet, host)
            host.remove_packet(packet)

def checkARP(host, des_mac, bits):
    if len(bits) == 64: #cumple el formato de 4 bytes ARPR | ARPQ 4bytes IP
        ip = get_ip_from_bin(bits[32:]) # convert bits chunk to {}.{}.{}.{} ip format 
        word = get_ascii_from_bin(bits[0:32]) # convert
        if word == 'ARPQ':
            handler.send_frame(host.name, des_mac, ARPResponse(ip), handler.time)
        if word == 'ARPR':
            for packet in host.packets:
                if packet.des_ip == ip:
                    packet.mac_des = host.mac
            check_PackageCondition(host)     



def is_ip_packet(data):
    if len(data) > 88:
        payload_size = int(data[80:88],2) *8
        payload = data[88:]
        return payload_size == len(payload)
    return False

def search_ip(host, des_mac, des_ip):
    q = ARPQuery(des_ip)
    handler.send_frame(host.name, des_mac, q, handler.time)

# obtein ip format {Int}.{Int}.{Int}.{Int} from bits chunk where 1byte(8bits) represent a number from ip
def get_ip_from_bin(binIP):
    a = f"{int(binIP[0:8],2)}.{int(binIP[8:16],2)}.{int(binIP[16:24],2)}.{int(binIP[24:32],2)}"
    return a

def get_bin_from_ip(ip):
    bin_ip =''
    for n in ip.split('.'):
        bin_ip += format(int(n),'08b')
    return bin_ip

def get_ascii_from_bin(bits):
    return chr(int(bits[0:8],2)) + chr(int(bits[8:16],2)) + chr(int(bits[16:24],2)) + chr(int(bits[24:32],2))

def setupFrameFromPacket(packet, host):
    data = ip_package(packet.ori_ip,packet.des_ip, packet.data)
    handler.send_frame(host.name, packet.mac_des, data, handler.time)

def ValidIP(input:str):
    regex ="^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return True if re.search(regex,input) else False


def get_bin_from_ascii(word):
    bin_ascii=''
    for c in word:
        bin_ascii += format(ord(c), '08b')
    return bin_ascii

def ARPQuery(ip):
    return get_bin_from_ascii('ARPQ') + get_bin_from_ip(ip)

def ARPResponse(ip):
    return get_bin_from_ascii('ARPR') + get_bin_from_ip(ip)

def bin_ip(ip):
    result= ""
    for n in ip.split('.'):
        result += format(int(n),'08b')
    return result

def ip_package(ori_ip,des_ip, payload, ttl=0, protocol=0):
    package = ""
    package += bin_ip(des_ip) + bin_ip(ori_ip)
    package += format(ttl,'08b') + format(protocol, '08b')
    package += format(len(payload)//8, '08b')
    package += payload
    return package    

# def send_arp(origen, destiny_mac, ip, mode):
#     data = ''
#     if mode == 'q':
#         data = ARPQuery(ip)
#         handler.send_frame(origen, destiny_mac, data, handler.time)
#     else:
#         data = ARPResponse
#         handler.send_frame(origen, destiny_mac, data, handler.time) 
