# Nmap Inventory (10.0.0.0/16)

Source XML: `/tmp/nmap-10.0.0.0_16-aggressive-full.xml`
Scan command: `nmap -A -T4 -sS -p- -Pn --max-retries 1 --min-rate 1000 -iL /tmp/nmap-10.0.0.0_16.hosts -oA /tmp/nmap-10.0.0.0_16-aggressive-full`
Scanner: nmap 7.94SVN
Start: Mon Dec 29 05:21:28 2025
End: Mon Dec 29 05:26:05 2025
Elapsed: 277.28 seconds
Summary: Nmap done at Mon Dec 29 05:26:05 2025; 9 IP addresses (9 hosts up) scanned in 277.28 seconds

## Summary
| IP | Hostnames | Status | MAC | OS Guess (accuracy) | Distance | Uptime (s) | Open TCP Ports |
|---|---|---|---|---|---|---|---|
| 10.0.0.100 | _gateway (PTR) | up | 0A:8B:E9:DA:DE:9D | Linux 4.15 - 5.8 (100) | 1 | 2080808 | 1 |
| 10.0.10.89 | WAN-ACCESS-02.techyes.local (PTR) | up | 0C:0C:D4:E2:00:03 | - | 1 | - | 0 |
| 10.0.14.166 | INT-DIST-01.techyes.local (PTR) | up | 0C:96:32:3A:00:0F | - | 1 | - | 0 |
| 10.0.24.128 | TECHYES-CORE-01.techyes.local (PTR) | up | 0C:0E:F4:5B:00:00 | Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (100) | 1 | 2150212 | 7 |
| 10.0.128.117 | OOB-ADMIN.techyes.local (PTR) | up | - | Linux 2.6.32 (100) | 0 | 2897095 | 8 |
| 10.0.139.119 | TECHYES-CORE-02.techyes.local (PTR) | up | 0C:81:B0:FA:00:00 | Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (100) | 1 | 2150212 | 5 |
| 10.0.162.74 | DATA-LS-01.techyes.local (PTR) | up | 0C:D6:B7:B4:00:00 | Cisco 836, 890, 1751, 1841, 2800, or 2900 router (IOS 12.4 - 15.1) (100) | 1 | - | 1 |
| 10.0.244.64 | INT-ACCESS-02.techyes.local (PTR) | up | 0C:DD:FF:9E:00:03 | - | 1 | - | 0 |
| 10.0.252.116 | - | up | 0C:66:91:BE:00:00 | Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (100) | 1 | 2150211 | 3 |

## Host 10.0.0.100 (_gateway (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.0.100 mac=0A:8B:E9:DA:DE:9D
- Hostnames: _gateway (PTR)
- Distance: 1
- Uptime: 2080808 seconds (lastboot Fri Dec  5 03:25:03 2025)
- Times: srtt=625 rttvar=209 timeout=100000
- TCP sequence: index=258 difficulty=Good luck! values=931FC4E3,E00289E3,74777A59,98B4B174,FD0F21A6,38C230FC
- IPID sequence: class=All zeros values=0,0,0,0,0,0
- TCP TS sequence: class=1000HZ values=7C065C7D,7C065CE1,7C065D46,7C065DAA,7C065E0E,7C065E74
- Extraports: state=closed count=65534; reason=reset count=65534 proto=tcp ports=1-52,54-65535

**OS**
- Match: Linux 4.15 - 5.8 (accuracy 100, line 67250)
- Class: type=general purpose vendor=Linux family=Linux gen=4.X accuracy=100 cpe=cpe:/o:linux:linux_kernel:4
- Class: type=general purpose vendor=Linux family=Linux gen=5.X accuracy=100 cpe=cpe:/o:linux:linux_kernel:5

**Trace**
- ttl=1 rtt=0.62 ipaddr=10.0.0.100 host=_gateway

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 53 | tcp | open | syn-ack | 64 | domain | dnsmasq | 2.80 | - | probed | 10 | - | cpe:/a:thekelleys:dnsmasq:2.80 | dns-nsid: <br>  bind.version: dnsmasq-2.80 |

## Host 10.0.10.89 (WAN-ACCESS-02.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.10.89 mac=0C:0C:D4:E2:00:03
- Hostnames: WAN-ACCESS-02.techyes.local (PTR)
- Distance: 1
- Times: srtt=1926 rttvar=889 timeout=100000
- Extraports: state=closed count=65535; reason=reset count=65535 proto=tcp ports=1-65535

**OS**
- Class: -

**Trace**
- ttl=1 rtt=1.93 ipaddr=10.0.10.89 host=WAN-ACCESS-02.techyes.local

**Ports (open)**
- -

## Host 10.0.14.166 (INT-DIST-01.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.14.166 mac=0C:96:32:3A:00:0F
- Hostnames: INT-DIST-01.techyes.local (PTR)
- Distance: 1
- Times: srtt=2505 rttvar=1584 timeout=100000
- Extraports: state=closed count=65535; reason=reset count=65535 proto=tcp ports=1-65535

**OS**
- Class: -

**Trace**
- ttl=1 rtt=2.51 ipaddr=10.0.14.166 host=INT-DIST-01.techyes.local

**Ports (open)**
- -

## Host 10.0.24.128 (TECHYES-CORE-01.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.24.128 mac=0C:0E:F4:5B:00:00
- Hostnames: TECHYES-CORE-01.techyes.local (PTR)
- Distance: 1
- Uptime: 2150212 seconds (lastboot Thu Dec  4 08:08:19 2025)
- Times: srtt=929 rttvar=296 timeout=100000
- TCP sequence: index=264 difficulty=Good luck! values=4A9BC419,5CCB4FAC,60B6255B,EA90476B,4E4541BC,1BB33E22
- IPID sequence: class=Incremental values=483A,483C,4843,4845,4848,484C
- TCP TS sequence: class=1000HZ values=80296273,802962D7,8029633C,802963A0,80296404,8029646A
- Extraports: state=closed count=65528; reason=reset count=65528 proto=tcp ports=1-21,24-66,68-110,112-829,831-12344,12346-40040,40042-65535

**OS**
- Match: Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (accuracy 100, line 41512)
- Class: type=router vendor=Juniper family=JUNOS gen=8.X accuracy=100 cpe=cpe:/o:juniper:junos:8
- Class: type=switch vendor=Juniper family=JUNOS gen=9.X accuracy=100 cpe=cpe:/o:juniper:junos:9
- Class: type=switch vendor=Juniper family=JUNOS gen=10.X accuracy=100 cpe=cpe:/o:juniper:junos:10
- Class: type=router vendor=Juniper family=JUNOS gen=11.X accuracy=100 cpe=cpe:/o:juniper:junos:11

**Trace**
- ttl=1 rtt=0.93 ipaddr=10.0.24.128 host=TECHYES-CORE-01.techyes.local

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | tcp | open | syn-ack | 64 | ssh | OpenSSH | 7.2 | protocol 2.0 | probed | 10 | - | cpe:/a:openbsd:openssh:7.2 | ssh-hostkey: <br>  1024 42:5b:d4:2a:39:9e:f4:84:ff:5d:37:68:6c:89:30:df (DSA)<br>  2048 df:34:ee:82:52:33:fe:20:cb:a6:95:6a:d5:99:6e:1e (RSA)<br>  256 62:e7:ad:18:09:97:2d:83:45:7b:35:74:7b:c9:5e:cd (ECDSA)<br>  256 d9:0e:ce:75:ef:87:d3:17:d1:40:9a:8a:94:5c:85:2d (ED25519) |
| 23 | tcp | open | syn-ack | 64 | telnet | Openwall GNU/*/Linux telnetd | - | - | probed | 10 | - | cpe:/o:linux:linux_kernel | - |
| 67 | tcp | open | syn-ack | 64 | tcpwrapped | - | - | - | probed | 8 | - | - | - |
| 111 | tcp | open | syn-ack | 64 | rpcbind | - | 2-4 | RPC #100000 | probed | 10 | - | - | rpcinfo: <br>  program version    port/proto  service<br>  100000  2,3,4        111/tcp   rpcbind<br>  100000  2,3,4        111/udp   rpcbind<br>  100000  3,4          111/tcp6  rpcbind<br>  100000  3,4          111/udp6  rpcbind<br>  100003  2,3         2049/tcp   nfs<br>  100003  2,3         2049/udp   nfs<br>  100005  1,3         6666/tcp   mountd<br>  100005  1,3         6666/udp   mountd<br> |
| 830 | tcp | open | syn-ack | 64 | ssh | OpenSSH | 7.2 | protocol 2.0 | probed | 10 | - | cpe:/a:openbsd:openssh:7.2 | ssh-hostkey: <br>  1024 42:5b:d4:2a:39:9e:f4:84:ff:5d:37:68:6c:89:30:df (DSA)<br>  2048 df:34:ee:82:52:33:fe:20:cb:a6:95:6a:d5:99:6e:1e (RSA)<br>  256 62:e7:ad:18:09:97:2d:83:45:7b:35:74:7b:c9:5e:cd (ECDSA)<br>  256 d9:0e:ce:75:ef:87:d3:17:d1:40:9a:8a:94:5c:85:2d (ED25519) |
| 12345 | tcp | open | syn-ack | 64 | http | lighttpd | 1.4.32 | - | probed | 10 | - | cpe:/a:lighttpd:lighttpd:1.4.32 | http-server-header: lighttpd/1.4.32<br>http-title: REST-API explorer |
| 40041 | tcp | open | syn-ack | 64 | unknown | - | - | - | table | 3 | - | - | - |

## Host 10.0.139.119 (TECHYES-CORE-02.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.139.119 mac=0C:81:B0:FA:00:00
- Hostnames: TECHYES-CORE-02.techyes.local (PTR)
- Distance: 1
- Uptime: 2150212 seconds (lastboot Thu Dec  4 08:08:19 2025)
- Times: srtt=1074 rttvar=570 timeout=100000
- TCP sequence: index=260 difficulty=Good luck! values=C69722DE,29E3CCAD,5D93C583,7053AF2B,7E9FD008,980EB245
- IPID sequence: class=Incremental values=4219,421E,4220,4226,4227,422C
- TCP TS sequence: class=1000HZ values=802962EE,80296352,802963B6,8029641B,8029647F,802964E5
- Extraports: state=closed count=65530; reason=reset count=65530 proto=tcp ports=1-21,23-66,68-110,112-829,831-40040,40042-65535

**OS**
- Match: Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (accuracy 100, line 41512)
- Class: type=router vendor=Juniper family=JUNOS gen=8.X accuracy=100 cpe=cpe:/o:juniper:junos:8
- Class: type=switch vendor=Juniper family=JUNOS gen=9.X accuracy=100 cpe=cpe:/o:juniper:junos:9
- Class: type=switch vendor=Juniper family=JUNOS gen=10.X accuracy=100 cpe=cpe:/o:juniper:junos:10
- Class: type=router vendor=Juniper family=JUNOS gen=11.X accuracy=100 cpe=cpe:/o:juniper:junos:11

**Trace**
- ttl=1 rtt=1.07 ipaddr=10.0.139.119 host=TECHYES-CORE-02.techyes.local

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | tcp | open | syn-ack | 64 | ssh | OpenSSH | 7.2 | protocol 2.0 | probed | 10 | - | cpe:/a:openbsd:openssh:7.2 | ssh-hostkey: <br>  1024 40:ec:de:40:a3:65:7b:34:f6:f4:6e:48:67:90:e9:99 (DSA)<br>  2048 34:fa:89:7a:98:59:17:69:c7:79:b6:af:99:17:c2:7a (RSA)<br>  256 e6:9c:11:fb:0c:b6:db:59:34:81:8f:3e:60:82:ad:eb (ECDSA)<br>  256 d5:df:3f:17:57:3d:18:26:0c:72:7f:ca:56:4e:7f:2e (ED25519) |
| 67 | tcp | open | syn-ack | 64 | tcpwrapped | - | - | - | probed | 8 | - | - | - |
| 111 | tcp | open | syn-ack | 64 | rpcbind | - | 2-4 | RPC #100000 | probed | 10 | - | - | rpcinfo: <br>  program version    port/proto  service<br>  100000  2,3,4        111/tcp   rpcbind<br>  100000  2,3,4        111/udp   rpcbind<br>  100000  3,4          111/tcp6  rpcbind<br>  100000  3,4          111/udp6  rpcbind<br>  100003  2,3         2049/tcp   nfs<br>  100003  2,3         2049/udp   nfs<br>  100005  1,3         6666/tcp   mountd<br>  100005  1,3         6666/udp   mountd<br> |
| 830 | tcp | open | syn-ack | 64 | ssh | OpenSSH | 7.2 | protocol 2.0 | probed | 10 | - | cpe:/a:openbsd:openssh:7.2 | ssh-hostkey: <br>  1024 40:ec:de:40:a3:65:7b:34:f6:f4:6e:48:67:90:e9:99 (DSA)<br>  2048 34:fa:89:7a:98:59:17:69:c7:79:b6:af:99:17:c2:7a (RSA)<br>  256 e6:9c:11:fb:0c:b6:db:59:34:81:8f:3e:60:82:ad:eb (ECDSA)<br>  256 d5:df:3f:17:57:3d:18:26:0c:72:7f:ca:56:4e:7f:2e (ED25519) |
| 40041 | tcp | open | syn-ack | 64 | unknown | - | - | - | table | 3 | - | - | - |

## Host 10.0.162.74 (DATA-LS-01.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.162.74 mac=0C:D6:B7:B4:00:00
- Hostnames: DATA-LS-01.techyes.local (PTR)
- Distance: 1
- Times: srtt=3366 rttvar=2574 timeout=100000
- TCP sequence: index=261 difficulty=Good luck! values=EB304C4,E88395A4,8778FC5E,E1BAB8E5,DB720A9C,FD6CDAA2
- IPID sequence: class=Randomized values=D65B,C18F,F890,C062,8D83,C158
- TCP TS sequence: class=none returned (unsupported) values=-
- Extraports: state=closed count=65534; reason=reset count=65534 proto=tcp ports=1-22,24-65535

**OS**
- Match: Cisco 836, 890, 1751, 1841, 2800, or 2900 router (IOS 12.4 - 15.1) (accuracy 100, line 16365)
- Class: type=router vendor=Cisco family=IOS gen=12.X accuracy=100 cpe=cpe:/h:cisco:836_router, cpe:/h:cisco:890_router, cpe:/h:cisco:1751_router, cpe:/h:cisco:2800_router, cpe:/o:cisco:ios:12
- Class: type=router vendor=Cisco family=IOS gen=15.X accuracy=100 cpe=cpe:/h:cisco:1841_router, cpe:/h:cisco:2900_router, cpe:/o:cisco:ios:15
- Class: type=WAP vendor=Cisco family=IOS gen=12.X accuracy=100 cpe=cpe:/o:cisco:ios:12.4
- Class: type=WAP vendor=Cisco family=IOS gen=15.X accuracy=100 cpe=cpe:/h:cisco:aironet_1141n, cpe:/h:cisco:aironet_3602i, cpe:/o:cisco:ios:12.4, cpe:/o:cisco:ios:15.3
- Class: type=WAP vendor=Cisco family=IOS gen=15.X accuracy=100 cpe=cpe:/o:cisco:ios:15.2

**Trace**
- ttl=1 rtt=3.37 ipaddr=10.0.162.74 host=DATA-LS-01.techyes.local

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | tcp | open | syn-ack | 255 | telnet | Cisco router telnetd | - | - | probed | 10 | - | cpe:/a:cisco:telnet<br>cpe:/o:cisco:ios | - |

## Host 10.0.244.64 (INT-ACCESS-02.techyes.local (PTR))

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.244.64 mac=0C:DD:FF:9E:00:03
- Hostnames: INT-ACCESS-02.techyes.local (PTR)
- Distance: 1
- Times: srtt=1780 rttvar=796 timeout=100000
- Extraports: state=closed count=65535; reason=reset count=65535 proto=tcp ports=1-65535

**OS**
- Class: -

**Trace**
- ttl=1 rtt=1.78 ipaddr=10.0.244.64 host=INT-ACCESS-02.techyes.local

**Ports (open)**
- -

## Host 10.0.252.116 (-)

**Basics**
- Status: up (reason=arp-response ttl=0)
- Addresses: ipv4=10.0.252.116 mac=0C:66:91:BE:00:00
- Hostnames: -
- Distance: 1
- Uptime: 2150211 seconds (lastboot Thu Dec  4 08:08:20 2025)
- Times: srtt=1008 rttvar=180 timeout=100000
- TCP sequence: index=262 difficulty=Good luck! values=87BF3CEE,D136DDC8,637AEA0B,EB097EE3,A6B573C6,9A0CC680
- IPID sequence: class=Incremental values=3800,3804,3807,380B,3810,3812
- TCP TS sequence: class=1000HZ values=80295E6F,80295ED3,80295F38,80295F9C,80296000,80296066
- Extraports: state=closed count=65532; reason=reset count=65532 proto=tcp ports=1-66,68-110,112-40040,40042-65535

**OS**
- Match: Juniper Networks J2320 or MX5-T router; or EX2200, EX3200, EX4200, or EX8200 switch (JUNOS 8.5 - 11.2) (accuracy 100, line 41512)
- Class: type=router vendor=Juniper family=JUNOS gen=8.X accuracy=100 cpe=cpe:/o:juniper:junos:8
- Class: type=switch vendor=Juniper family=JUNOS gen=9.X accuracy=100 cpe=cpe:/o:juniper:junos:9
- Class: type=switch vendor=Juniper family=JUNOS gen=10.X accuracy=100 cpe=cpe:/o:juniper:junos:10
- Class: type=router vendor=Juniper family=JUNOS gen=11.X accuracy=100 cpe=cpe:/o:juniper:junos:11

**Trace**
- ttl=1 rtt=1.01 ipaddr=10.0.252.116 host=-

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 67 | tcp | open | syn-ack | 64 | tcpwrapped | - | - | - | probed | 8 | - | - | - |
| 111 | tcp | open | syn-ack | 64 | rpcbind | - | 2-4 | RPC #100000 | probed | 10 | - | - | rpcinfo: <br>  program version    port/proto  service<br>  100000  2,3,4        111/tcp   rpcbind<br>  100000  2,3,4        111/udp   rpcbind<br>  100000  3,4          111/tcp6  rpcbind<br>  100000  3,4          111/udp6  rpcbind<br>  100003  2,3         2049/tcp   nfs<br>  100003  2,3         2049/udp   nfs<br>  100005  1,3         6666/tcp   mountd<br>  100005  1,3         6666/udp   mountd<br> |
| 40041 | tcp | open | syn-ack | 64 | unknown | - | - | - | table | 3 | - | - | - |

## Host 10.0.128.117 (OOB-ADMIN.techyes.local (PTR))

**Basics**
- Status: up (reason=user-set ttl=0)
- Addresses: ipv4=10.0.128.117 mac=-
- Hostnames: OOB-ADMIN.techyes.local (PTR)
- Distance: 0
- Uptime: 2897095 seconds (lastboot Tue Nov 25 16:41:10 2025)
- Times: srtt=87 rttvar=17 timeout=100000
- TCP sequence: index=260 difficulty=Good luck! values=C72E03F,7C8498C9,6FEF495D,31B0F450,6DEB2EC,D16ADD36
- IPID sequence: class=All zeros values=0,0,0,0,0,0
- TCP TS sequence: class=1000HZ values=ACAE1B94,ACAE1BF8,ACAE1C5C,ACAE1CC0,ACAE1D24,ACAE1D88
- Extraports: state=closed count=65526; reason=reset count=65526 proto=tcp ports=1-21,23-3388,3390-4329,4331-4821,4823-5200,5202-5900,5902-44320,44324-65535

**OS**
- Match: Linux 2.6.32 (accuracy 100, line 55742)
- Class: type=general purpose vendor=Linux family=Linux gen=2.6.X accuracy=100 cpe=cpe:/o:linux:linux_kernel:2.6.32

**Ports (open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | tcp | open | syn-ack | 64 | ssh | OpenSSH | 9.6p1 Ubuntu 3ubuntu13.14 | Ubuntu Linux; protocol 2.0 | probed | 10 | - | cpe:/a:openbsd:openssh:9.6p1<br>cpe:/o:linux:linux_kernel | ssh-hostkey: <br>  256 72:a5:c3:31:68:be:ab:44:f9:05:3b:56:6f:ee:91:70 (ECDSA)<br>  256 22:5e:6d:68:12:7e:b6:d1:f0:f0:b0:5e:20:fc:c4:93 (ED25519) |
| 3389 | tcp | open | syn-ack | 64 | ms-wbt-server | xrdp | - | - | probed | 10 | - | cpe:/a:jay_sorg:xrdp | - |
| 4330 | tcp | open | syn-ack | 64 | dey-sapi | - | - | - | table | 3 | - | - | - |
| 5201 | tcp | open | syn-ack | 64 | iperf3 | - | - | - | probed | 10 | - | - | - |
| 5901 | tcp | open | syn-ack | 64 | vnc | VNC | - | protocol 3.8 | probed | 10 | - | - | vnc-info: <br>  Protocol version: 3.8<br>  Security types: <br>    None (1)<br>  WARNING: Server does not require authentication |
| 44321 | tcp | open | syn-ack | 64 | pmcd | - | - | - | table | 3 | - | - | - |
| 44322 | tcp | open | syn-ack | 64 | pmcdproxy | - | - | - | table | 3 | - | - | fingerprint-strings: <br>  GetRequest: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 204<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for URL</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html><br>  HTTPOptions: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 208<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for OPTIONS</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html><br>    HTTP/1.1 200 OK<br>    Connection: Keep-Alive<br>    Content-Length: 0<br>    Access-Control-Allow-Methods: GET, PUT, HEAD, POST, TRACE, OPTIONS<br>    Access-Control-Max-Age: 86400<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>  RTSPRequest: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 208<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:26 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for OPTIONS</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html> |
| 44323 | tcp | open | syn-ack | 64 | pmwebapi | - | - | - | table | 3 | - | - | fingerprint-strings: <br>  GetRequest: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 204<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for URL</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html><br>  HTTPOptions: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 208<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for OPTIONS</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html><br>    HTTP/1.1 200 OK<br>    Connection: Keep-Alive<br>    Content-Length: 0<br>    Access-Control-Allow-Methods: GET, PUT, HEAD, POST, TRACE, OPTIONS<br>    Access-Control-Max-Age: 86400<br>    Date: Mon, 29 Dec 2025 05:25:21 GMT<br>  RTSPRequest: <br>    HTTP/1.1 400 Bad Request<br>    Connection: Keep-Alive<br>    Access-Control-Allow-Origin: *<br>    Access-Control-Allow-Headers: Accept, Accept-Language, Content-Language, Content-Type<br>    Access-Control-Max-Age: 86400<br>    Content-Length: 208<br>    Content-Type: text/html<br>    Date: Mon, 29 Dec 2025 05:25:26 GMT<br>    <html><br>    <head><title>400 Bad Request</title></head><br>    <body><br>    <h1>400 Bad Request</h1><br>    <p><b>unknown servlet</b>: no handler for OPTIONS</p><hr><br>    <p><small><i>pmproxy/6.2.0</i></small></p><br>    </body><br>    </html> |

**Ports (non-open)**
| Port | Proto | State | Reason | TTL | Service | Product | Version | Extra Info | Method | Conf | Tunnel | CPEs | Scripts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4822 | tcp | filtered | no-response | 0 | - | - | - | - | - | - | - | - | - |
