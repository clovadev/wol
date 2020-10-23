import socket
import struct


def wake_on_lan(ip_addr: str, mac_addr: str):
    mac_addr = mac_addr.split(":")
    mac_encode = struct.pack("BBBBBB", int(mac_addr[0], 16), int(mac_addr[1], 16),
                             int(mac_addr[2], 16), int(mac_addr[3], 16),
                             int(mac_addr[4], 16), int(mac_addr[5], 16))

    # 매직패킷은 16진수 FF FF FF FF FF FF + 대상 컴퓨터의 MAC ADDRESS를 16번 나열한 102Bytes 패킷
    magic_packet = b'\xFF' * 6 + mac_encode * 16

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(magic_packet, (ip_addr, 9))
    sock.close()


if __name__ == '__main__':
    ip = '220.72.33.255'
    mac = {'desktop': 'A8:5E:45:E2:AF:F0'}
