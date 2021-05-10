# <center>Informe Redes04P Capa de Red ParteI</center>
<center>David Orlando De Quesada Oliva C311</center>

<center>Javier Domínguez C312</center>

Ejecutar:

```
python main.py -f file.txt
```

para ejecuar el proyecto

En network_layer_utils.py están la mayoría de los métodos que vamos a usar para esta capa de red.

Dado que ahora los host tiene un IP y una máscara de subred representamos con la class Host que tenemos en objs.py esa información con las siguientes propiedades:

```
self.ip
self.mask
```

Las cuales van a estar inicialmente en None hasta que se le asigne con el comando ip

Un host además tiene una lista de packets donde va a guardar temporalmente todos los paquetes que aún no se han mandado esperando que llegue la repsuesta de un ARPQ para saber la mac de la pc que le corresponde con el ip al cual quiere enviar dicho paquete. De la forma en que se realizó si por ejemplo tienes varios paquetes en espera que van a un mismo ip destino una vez que le llegue un ARPR y sepa la mac todos los paquetes que tienen el mismo ip destino que van desde eso host automáticamente cogen esa mac sin tener que esperar por si propio ARPR pues daría la misma aunque esos frames se siguen enviando igual lo que se ignoran y los paquetes podrían enviarse mucho 

Además creamos un nuevo fichero _payload.txt  en host el cual va a ir guardando los datos recibido por esa pc en la cada de red

Al enviar un paquete con el comando send_packet ocurre lo siguiente :

- El host que va a enviar el packet crea una instancia de Packet con el método add_packet el cual recibe el ip destino y la data que quiere enviar el paquete en binario
- add_packet crea una instancia de Packet con la mac_ori como la mac del host a enviar el packet, el ip destino el que se le paso como parametro , el ip origen el del host a enviar el packet , la data como data que se le pasó como parámetro y se deja la mac de destino en None pues se desconoce inicialmente.
- Luego que se agrega el packet a la lista de packet sin enviar del host, el cual permanece ahí hasta que se conozca la mac del destino, se enviá un frame especial ARPQ el cual se manda con mac destino FFFF para que llegue a todo el mundo y le responderá solo el host que tenga ip igual al que se manda oculto en el frame respondiendo con un frame especial ARPR de respuesta.
- Una vez que llegue al host que debe enviar el packet el frame especial ARPR con la mac correspondiente al ip del packet entonces se procede a enviar el packet 
- Se crea un ip packet con el método en network_layer_utils.py ip_package  el cual forma una data de la 8 bytes para el ip destino 8 byte para el ip origen 1 byte con 0 que representa ttl y 1 byte con 0 que representa el protocol
- ese ip_packet creado se encapsula en un frame como data y se envia a la mac destino obtenida previamente por el ARPR 
- una vez que llegue ese frame al destino se obteine el payload que estaba dentro del ip_packet y se escribe en el log_payload poniendo el ip desde donde se le envió ese payload



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

 

