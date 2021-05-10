# Redes04P

Dado que ahora los host tiene un IP y una máscara de subred representamos con la class Host que tenemos en objs.py esa información con las siguientes propiedades:

```
self.ip
self.mask
```

Las cuales van a estar inicialmente en None hasta que se le asigne con el comando ip

Un host adem

Además creamos un nuevo fichero _payload.txt  en host el cual va a ir guardando los datos recibido por esa pc en la cada de red

Al enviar un paquete con el comando send_packet ocurre lo siguiente :

- El host que va a enviar el packet crea una instancia

En network_layer_utils.py están la mayoría de los métodos que vamos a usar para esta capa de red.



ARP Protocol:

Para mandar una sennal de ARP le entramos un ip para formar la data de ese frame 

En caso que sea ARPQ formamos la data del frame con 8 bytes de la siguiente forma:

'ARPQ' llevamos cada caracter a su código ASCII A = 65,  R = 82,  P=80,  Q=81 lo llevamos a binario y formamos concatenando el valor en ASCII de cada uno la siguiente cadena:

```
'01000001010100100101000001010001'
```

Luego dado el ip de entrada de la forma {a}.{b}.{c}.{d} donde a.b.c.d son enteros con valor [0,255] llevamos a binario cada uno y concatenamos la cadena de bits anterior con esta 

Esto lo hacemos con los siguientes métodos:

Dado un ip lo llevo a su representación en binario

```
def get_bin_from_ip(ip):
    bin_ip =''
    for n in ip.split('.'):
        bin_ip += format(int(n),'08b')
    return bin_ip
```

Dado una cadena de letras doy en binario la concatenaciónde del ascii de letra:

```
def get_bin_from_ascii(word):
    bin_ascii=''
    for c in word:
        bin_ascii += format(ord(c), '08b')
    return bin_ascii
```

 

