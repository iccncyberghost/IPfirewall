
there are 5 python files in this directory
pye.py -------> here we defined some functiones that we need

pythonpackets.py ------> this is a sniffer that captures trafic and gives you all information about sniffed frames

sniff_and_filter_gui.py ---> this one is a tkinter treeview that shows you 200 captured frames and there statues (Accepted/Rejected) but it does not realy reject frames it only shows if that frame is allowed or not, and as a solution we decided to use the already existing firewall in linux wich called iptables to filter packets but this time by using a python script called block.py

block.py ----> this one needs to be placed in crontab wich execute some programs automatically on regular basis.

to add an ip to the not allowed list there is a funtion in sniff_and_filter_gui.py called not_allowed_ip() it returns a list of ip addresses just add the ip you want to ban to that list

pysahrk.py -----> for the first part the script that reads from a wirshark capture, you can edit the rules but editing the 2 lines

if l[0]=='179'andl[1]=='19':
if packet.tcp.dstport=='80'

thanks for using ip-firewall 

