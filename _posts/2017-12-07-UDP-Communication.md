---
layout: post
title:  "How To Send and Receive UDP Data in Python"

date:   2017-12-07 10:58
categories: how-to python udp
---

UDP is a useful protocol to use to communicate between remote systems connected over TCP/IP. Python can communicate over UDP via its sockets library. I've had to develop UDP code from scratch several times now because I change jobs, lose the files, etc. Thus, I'm going to post a simple UDP example in Python with fully commented code so I can refer back to it later.

This application does both UDP transmit and receive and as a bonus it uses threads to do so. The main thread sets up the receive thread and then does the transmit. The receive thread will receive then echo back whatever it gets and the transmit thread will print whatever it gets. 

It's worth noting that using UDP or TCP to communicate between threads is a pretty legitimate communication method (from what I'm told). Or maybe it was between processes? Either way, this code works and should serve as a good example of simple UDP communication in both directions.

## Python Code ##

{% highlight python %}
#!/usr/bin/python

import socket
from threading import Thread
from time import sleep
import sys

exit = False

def rxThread(portNum):
    global exit
    
    #Generate a UDP socket
    rxSocket = socket.socket(socket.AF_INET, #Internet
                             socket.SOCK_DGRAM) #UDP
                             
    #Bind to any available address on port *portNum*
    rxSocket.bind(("",portNum))
    
    #Prevent the socket from blocking until it receives all the data it wants
    #Note: Instead of blocking, it will throw a socket.error exception if it
    #doesn't get any data
    
    rxSocket.setblocking(0)
    
    print "RX: Receiving data on UDP port " + str(portNum)
    print ""
    
    while not exit:
        try:
            #Attempt to receive up to 1024 bytes of data
            data,addr = rxSocket.recvfrom(1024) 
            #Echo the data back to the sender
            rxSocket.sendto(str(data),addr)

        except socket.error:
            #If no data is received, you get here, but it's not an error
            #Ignore and continue
            pass

        sleep(.1)
    
def txThread(portNum):
    global exit
    
    
def main(args):    
    global exit
    print "UDP Tx/Rx Example application"
    print "Press Ctrl+C to exit"
    print ""
    
    portNum = 8000
   
    udpRxThreadHandle = Thread(target=rxThread,args=(portNum,))    
    udpRxThreadHandle.start()
        
    sleep(.1)
    
    #Generate a transmit socket object
    txSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    #Do not block when looking for received data (see above note)
    txSocket.setblocking(0) 
   
    print "Transmitting to 127.0.0.1 port " + str(portNum)
    print "Type anything and press Enter to transmit"
    while True:
        try:
             #Retrieve input data 
            txChar = raw_input("TX: ")
            
            #Transmit data to the local server on the agreed-upon port
            txSocket.sendto(txChar,("127.0.0.1",portNum))
            
            #Sleep to allow the other thread to process the data
            sleep(.2)
            
            #Attempt to receive the echo from the server
            data, addr = txSocket.recvfrom(1024)
            
            print "RX: " + str(data) 

        except socket.error,msg:    
            #If no data is received you end up here, but you can ignore
            #the error and continue
            pass   
        except KeyboardInterrupt:
            exit = True
            print "Received Ctrl+C... initiating exit"
            break
        sleep(.1)
         
    udpRxThreadHandle.join()
        
    return

if __name__=="__main__":
    main(sys.argv[1:0])     

{% endhighlight %}

## Example Output ##

> UDP Tx/Rx Example application  
> Press Ctrl+C to exit  
>   
> RX: Receiving data on UDP port 8000  
>   
> Transmitting to 127.0.0.1 port 8000  
> Type anything and press Enter to transmit  
> TX: test  
> RX: test  
> TX: testing  
> RX: testing  
> TX: hello world  
> RX: hello world  
> TX: Received Ctrl+C... initiating exit  

## Blocking Sockets ##

Often in multi-threaded programming you'll *want* a blocking socket so that you can let other tasks run until there's data available for you to play with. You can modify the RX thread to do so:

{% highlight python %}

def rxThread(portNum):
    global exit
    
    #Generate a UDP socket
    rxSocket = socket.socket(socket.AF_INET, #Internet
                             socket.SOCK_DGRAM) #UDP
                             
    #Bind to any available address on port *portNum*
    rxSocket.bind(("",portNum))
    
    #Prevent the socket from blocking until it receives all the data it wants
    #Note: Instead of blocking, it will throw a socket.error exception if it
    #doesn't get any data
    
    rxSocket.settimeout(.1)
    
    print "RX: Receiving data on UDP port " + str(portNum)
    print ""
    
    while not exit:
        try:
            #Attempt to receive up to 1024 bytes of data
            data,addr = rxSocket.recvfrom(1024) 
            #Echo the data back to the sender
            rxSocket.sendto(str(data),addr)
        except socket.timeout:
            pass
        except socket.error:
            #If no data is received, you get here, but it's not an error
            #Ignore and continue
            pass
    


{% endhighlight %}


clientsocket.settimeout(5)

## Resources ##

* [Python Socket Library Documentation](https://docs.python.org/2/library/socket.html)





