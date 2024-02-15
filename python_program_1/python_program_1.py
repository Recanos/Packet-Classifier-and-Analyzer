import csv
from scapy.all import *

def classify_packets(packets):
    streams = {}
    for packet in packets:
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst

            if TCP in packet:
                port_src = packet[TCP].sport
                port_dst = packet[TCP].dport
            elif UDP in packet:
                port_src = packet[UDP].sport
                port_dst = packet[UDP].dport
            else:
                continue

            stream_key = (ip_src, ip_dst, port_src, port_dst)

            if stream_key in streams:
                streams[stream_key]['packets'] += 1
                streams[stream_key]['bytes'] += len(packet)
            else:
                streams[stream_key] = {'packets': 1, 'bytes': len(packet)}

    return streams

def write_to_csv(streams):
    with open("data.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for stream, info in streams.items():
            writer.writerow([stream[0], stream[1], stream[2], stream[3], info['packets'], info['bytes']])

def capture_live_packets(packet_count, interface):
    captured_packets = sniff(count=packet_count, iface=interface)
    return captured_packets

while True:
    print('Выберите действие:')
    print(' 1. Прочитать пакеты из pcap файла')
    print(' 2. Захватить пакеты из сетевого интерфейса')
    print(' 3. Выход')

    change = input("Введите цифру:")

    if change == '1' or change == '2': 

        if change == '1':
            pcap_file = input("Введите имя файла с расширением (Пример: example.pcap):")
            try:
                packets = rdpcap(pcap_file)
                streams = classify_packets(packets)
                write_to_csv(streams)
                print('Пакеты классифицированы, результат записан в "data.csv"')
            except FileNotFoundError:
                print(f"Ошибка: Файл '{pcap_file}' не найден.")

        elif change == '2':
            change = input("Захватить пакеты у определённого сетевого интерфейса? [y/n]:")
            if change == 'y':
                interface = input('Введите имя сетевого интерфейса (Пример: Ethernet):')
            elif change == 'n':
                interface = None
            else:
                print("Введён неверный символ, попробуйте ещё раз")
                

            packet_count = int(input("Количество пакетов для классификации:"))
            try:
                captured_packets = capture_live_packets(packet_count, interface)
                streams = classify_packets(captured_packets)
                write_to_csv(streams)
                print('Пакеты классифицированы, результат записан в "data.csv"')
            except Exception as e:
                print("Произошла ошибка при захвате пакетов:", e)
        
    elif change == '3':
        break
    else:
        print("Введите число от 1 до 3")