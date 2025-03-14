import re
brute_force_regex = "\[(\d{2}/\d{2}/\d{4}:\d{2}:\d{2}:\d{2})\]\s*server\s*sshd\[(\d{1,5})\]:\s*(Failed password for)\s*(\w+)\s*from\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*port\s*(\d{1,5})\s*(\w+)"

port_scan_regex = "\[(\d{2}/\d{2}/\d{4}:\d{2}:\d{2}:\d{2})\]\s*server\s*kernel:\s*IN=(\w+)\s*OUT=(\w*)\sMAC=([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})\s*SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*DST=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*LEN=(\d{1,3})\s*TOS=(0x\d{2})\s*PREC=(0x\d{2})\s*TTL=(\d{1,3})\s*ID=(\d{1,5})\s*(DF)?\s*PROTO=(\w+)\s*SPT=(\d{1,5})\s*DPT=(\d{1,5})\s*WINDOW=(\d{1,5})\s*RES=(0x\d{2})\s*(\w+)?\s*URGP=(\d{1,2})"

access_denied_regex = "\[(\d{2}/\d{2}/\d{4}:\d{2}:\d{2}:\d{2})\]\s*server\s*sshd\[(\d{1,5})\]:\s*(Invalid)\s*user (\w+)\s*from\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*port (\d{1,5})"
