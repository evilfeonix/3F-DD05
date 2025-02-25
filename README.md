# 3F-DD05

if you're look for an advanced ddosing tool, 3F-DD05, created by evilfeonix, is your right choice.

Your altimate tool for conducting both UDP flooding and SYN flooding Distributed DOS attack

**3F-DD05** allow you to conduct DDOS attack with different spoofed IP addresses, Making it a little bit challanging for their security to detect and prevent them from the attack.

# Features
- Uses different spoofed IP addresses to send traffics to the target.
- All UDPflooding and SYNflooding ddosing attack.
- Allow sending of raw data over TCP protocol.
- Uses python threading to send multiple traffics.

  > **Important: we're not responsible for any misuse or damages caused by this program, use it at your own risk!**

# Difference
The Difference between UDP flooding and SYN flooding ddosing attack.

| Attack type  | Protocol | Description
--------------:|-----:|------------
| SYN Flooding  | TCP  | Synflooding attack was always successful
| UDP Flooding  | UDP  | Udpflooding attack not always success due to some devices ignore incoming udp traffic

# Installation
## Termux
- _To run 3F-DD05 in termux, you will need to root your device_

```
pkg install tsu -y
```
```
pkg install python3 -y
```
```
git clone https://github.com/evilfeonix/3F-DD05.git
```
```
cd 3F-DD05
```
```
tsu -c "python3 ddos.py"
```

## Kali Linux
```
git clone https://github.com/evilfeonix/3F-DD05.git
```
```
cd 3F-DD05
```
```
sudo python3 ddos.py
```

# Goal of this program
Goal of this program is to flood target server, or particular running service with thousands of trafics, making the target unaccessible by overwhoming them

# Watch the full video on youtube
A little video that will guide you through out using this tool, click the below link the watch full tutorial, and also subscribe to our youtube channel.

### Wireshack
Captured packet sent by **3F-DD05** using Wireshack:

![3F-DD05 v1.0](https://github.com/evilfeonix/3F-DD05/blob/main/pcap.jpg)


# Support US 
Support us by following us!,

Also star and fork our repositories.


### License

[GNU General Public License v3.0](https://github.com/evilfeonix/3F-DD05/blob/main/LICENSE)

<div align=center>

Happy DDOSing 🏴‍☠️🏴‍☠️🏴‍☠️

<div>
