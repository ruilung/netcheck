# netcheck

check if server:port is open or not

# argument
-s servername or -i inventory file   
-p port or -f ports file   
-t timeout seconds default is 3 seconds   

# example 1
python netcheck.py -s www.google.com -p 80

# result 1
C:\>python netcheck.py -s www.google.com -p 80   
====OK list====   
www.google.com:80 >> Port is open   
====NG list====   


# example 2
python netcheck.py -i inv.txt -p 80

# result 2
C:\>type inv.txt   
www.google.com   
www.yahoo.com   

C:\>python netcheck.py -i inv.txt -p 80   
====OK list====   
www.google.com:80 >> Port is open   
www.yahoo.com:80 >> Port is open   
====NG list====   

# example 3
python netcheck.py -s www.google.com -f pf.txt

# result 3
C:\>type pf.txt   
80   
81   
C:\>python netcheck.py -s www.google.com -f pf.txt   
====OK list====   
www.google.com:80 >> Port is open   
====NG list====   
www.google.com:81 >> Port is not open   

# example 4
python netcheck.py -i inv.txt -f pf.txt

# result 4
C:\>type inv.txt   
www.google.com   
www.yahoo.com   
C:\>type pf.txt   
80   
81   
C:\>python netcheck.py -i inv.txt -f pf.txt   
====OK list====   
www.google.com:80 >> Port is open   
www.yahoo.com:80 >> Port is open   
====NG list====   
www.google.com:81 >> Port is not open   
www.yahoo.com:81 >> Port is not open   
