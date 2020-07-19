import pyshark
cap = pyshark.FileCapture('C:\\Users\\M.B\\Desktop\\testcaptur1.pcapng')
i=1
for packet in cap:
    print('*********************packet',i,'**************************************')
    i+=1
    l=packet.ip.src.split('.')
    print(packet)
    if packet.ip.src=='127.0.0.1':
        print('decision >>>>>>>>>>accept')
        continue
    else:
        if l[0]=='179'and l[1]=='19':
            if packet.tcp.dstport=='80':
                print('decision >>>>>>>>>>accept')
                continue
        print('decision>>>>>>>>>>>>drop')
