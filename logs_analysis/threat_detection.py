import re
import log_reader
import utils
path = "/home/angelo/Escritorio/CURSO/Cibersecurity/Logs analysis and threat detection/data/sample_log_1.log"
path_2 = "/home/angelo/Escritorio/CURSO/Cibersecurity/Logs analysis and threat detection/data/sample_log_2.log"

# print(log_reader.read_logs(path))



regex_brute_force = re.compile(utils.brute_force_regex)
regex_port_scan = re.compile(utils.port_scan_regex)
regex_access_denied = re.compile(utils.access_denied_regex)
def detections_threat(logs_lines):
    #Almacen de amenazas
    threats_brute_force = []
    threats_port_scan = []
    threats_access_denied = []
    
    for log_line in logs_lines:
        value_brute_force = regex_brute_force.search(log_line)
        value_port_scan = regex_port_scan.search(log_line)
        value_access_denied = regex_access_denied.search(log_line)
        

        if value_brute_force:
             threat_brute_force_infomation = {
                 "Tpye" : "Brute Force",
                 "User" : value_brute_force.group(4),
                 "Time ocurred" : value_brute_force.group(1),
                 "IP" : value_brute_force.group(5),
                 "Port" : value_brute_force.group(6),
                 "Encryption" : value_brute_force.group(7),
                 "SSHD" : value_brute_force.group(2)
             }        
             threats_brute_force.append(threat_brute_force_infomation)
        if value_port_scan:
            threats_port_scan_information = {
                "Tpye" : "Port Scan",
                "Time ocurred" : value_port_scan.group(1),
                "SRC" : value_port_scan.group(6),
                "DST" : value_port_scan.group(7),
                "DPT" : value_port_scan.group(16),
                "PROTOCOL" : value_port_scan.group(14),
                "MAC Address" : value_port_scan.group(4)
            }
            threats_port_scan.append(threats_port_scan_information)
        if value_access_denied:
            threats_access_denied_information = {
                "Type" : "Access Denied",
                "User" : value_access_denied.group(4),
                "Time ocurred" : value_access_denied.group(1),
                "IP" : value_access_denied.group(5),
                "Port" : value_access_denied.group(6),
                "SSHD" : value_access_denied.group(2)
            }
            threats_access_denied.append(threats_access_denied_information)
    return threats_brute_force, threats_port_scan, threats_access_denied


