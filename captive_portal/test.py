
socket_poller = poller()

ip='192.168.4.1'
udps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udps.bind((ip,53))
udps.listen(5)
socket_poller.add(udps)

try:
    while True:
        socket_poller.poll(100)
        time.sleep(0.1)
