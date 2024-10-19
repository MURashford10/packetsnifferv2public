This is a python file that record packets sent to and from a system. It show the time and date that the capture was started and when the packets were individually captured.
When running it prompts the user for the host ip address to use for the sending and receiving filtering. It then asks which interface they would like to capture packets from.
It will keep running until the user stops it with Ctrl + C.

Expected Output

Packet capture session started at: 15:23:45

Time     | Direction  | Protocol   | Source IP       | Destination IP
---------------------------------------------------------------------------
15:23:45 | Receiving  | TCP        | 192.168.1.5     | 192.168.1.10
15:23:46 | Sending    | UDP        | 192.168.1.10    | 192.168.1.5
15:23:47 | Receiving  | ICMP       | 192.168.1.3     | 192.168.1.5
15:23:48 | Sending    | HTTP       | 192.168.1.8     | 192.168.1.5
15:23:49 | Receiving  | DNS        | 192.168.1.7     | 192.168.1.5
15:23:50 | Sending    | TCP        | 192.168.1.2     | 192.168.1.5
15:23:51 | Receiving  | UDP        | 192.168.1.6     | 192.168.1.5
15:23:52 | Sending    | HTTP       | 192.168.1.10    | 192.168.1.5
15:23:53 | Receiving  | TCP        | 192.168.1.5     | 192.168.1.12
15:23:54 | Sending    | ICMP       | 192.168.1.11    | 192.168.1.5
15:23:55 | Receiving  | TCP        | 192.168.1.5     | 192.168.1.14
15:23:56 | Sending    | DNS        | 192.168.1.5     | 8.8.8.8
15:23:57 | Receiving  | TCP        | 192.168.1.15    | 192.168.1.5
15:23:58 | Sending    | HTTP       | 192.168.1.20    | 192.168.1.5
15:23:59 | Receiving  | ARP        | 192.168.1.5     | 192.168.1.25
15:24:00 | Sending    | TCP        | 192.168.1.22    | 192.168.1.5
15:24:01 | Receiving  | UDP        | 192.168.1.5     | 192.168.1.30
