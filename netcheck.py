import socket
import argparse
'''
-s servername or -i inventory file
-p port or -f ports file
-t timeout seconds default is 3 seconds
'''
timeout=3
listOK=[]
listNG=[]

def portcheck(ip,port):
    global timeout,listOK,listNG
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    ip=ip.strip('\n')
    port=port.strip('\n')
    try:
        result = sock.connect_ex((ip, int(port)))
    except:
        s = "except="+ip + ":" + port + " >> Port is not open"
        listNG.append(s)
        return

    if result == 0:
        s = ip + ":" + port + " >> Port is open"
        listOK.append(s)
    else:
        s = ip + ":" + port + " >> Port is not open"
        listNG.append(s)

parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-s",help="server name")
group1.add_argument("-i",help="inventory file,  hostnames or IPs in echo line")

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-p",help="port number")
group2.add_argument("-f",help="port list file")

parser.add_argument("-t",help="timeout seconds")

args=parser.parse_args()


if args.t:
    timeout = int(args.t)

if args.i:
    if args.p:
        with open(args.i) as i:
            for server in i.readlines():
                portcheck(server, args.p)

    if args.f:
        i=open(args.i)
        f=open(args.f)
        portlist =f.readlines()
        for server in i.readlines():
            for port in portlist:
                portcheck(server,port)
        i.close()
        f.close()


    if (not args.f) and (not args.p):
        print "error argument"


if args.s:
    if args.p:
        portcheck(args.s,args.p)

    if args.f:
        with open(args.f) as f:
            for port in f.readlines():
                portcheck(args.s, port )

    if  (not args.f) and (not args.p):
        print "error argument"




print "====OK list===="
for l in listOK:
    print l
print "====NG list===="
for l in listNG:
    print l

