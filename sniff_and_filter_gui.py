import socket 
import struct
import binascii
import os
import pye
from tkinter import *
from tkinter import ttk

# if operating system is windows

statu=""
if os.name == "nt":
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    s.bind(("YOUR_INTERFACE_IP",0))
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
   
# if operating system is linux
else:
    s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

# create loop

root = Tk()
    
tv = ttk.Treeview(root,height = 33,selectmode = "extended")


tv.heading('#0' , text='ID')
tv.configure(column=('#packets','#statu'))
tv.heading('#packets' , text='packets')
tv.heading('#statu' , text='statu')
tv.column("#packets",minwidth=0,width=1200)
tv.column("#statu",minwidth=0,width=100)
tv.column("#0",minwidth=0,width=40)


def not_allowed_ip():
    a=["157.240.195.17","172.217.18.228","192.168.1.1"]
    return(a)


for k in range(200):

    # Capture packets from network
    pkt=s.recvfrom(65565)


    # extract packets with the help of pye.unpack class 
    unpack=pye.unpack()

    ch=""
    n=1
    for i in unpack.eth_header(pkt[0][0:14]).iteritems():
        a,b=i
        ch=ch+str("{} : {} | ".format(a,b),)
    for i in unpack.ip_header(pkt[0][14:34]).iteritems():
        a,b=i
        if a=="Total Length" or a=="Source Address" or a=="Destination Address" :
            ch=ch+ str("{} : {} | ".format(a,b),)
        if a=="Source Address":
            if str(b) in not_allowed_ip():
                statu="rejected"
            else:
                statu="accepted"
		  
    tv.insert('' , 'end' , '#{}'.format(str(k)) , text=str(k))
    tv.set('#{}'.format(str(k)), '#packets' , ch)
    
    tv.set('#{}'.format(str(k)), '#statu' , statu)
tv.pack()
root.mainloop()

