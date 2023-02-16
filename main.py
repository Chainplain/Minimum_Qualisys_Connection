from QualisysConnector import Qualisys_con
import time
import socket
def bytesToHexString(bs):
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X ' % b for b in bs])

TCP_IP = '192.168.1.104'
UDP_IP_port = ('192.168.1.100', 6666)
TCP_PORT = 22221
# threading.main_thread()

here_qualisys_con = Qualisys_con(TCP_IP, TCP_PORT, UDP_IP_port)
time.sleep(1)




here_qualisys_con. start_capture()
here_qualisys_con. start_listening()

for i in range(100):
    print('Now is ' + str(i))
    print('Received data is: ' + bytesToHexString( here_qualisys_con. receive_data) )
    print('Received data in list is: ', here_qualisys_con.read_6DEuler_LittleEndian())
    print('Received times: ' + str (here_qualisys_con. read_count))
    here_qualisys_con.read_count = 0
    time.sleep(1)


# here_qualisys_con. stop_listening()
print('Happy ending!')



