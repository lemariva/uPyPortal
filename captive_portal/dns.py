# Copyright [2017] [Mauro Riva <lemariva@mail.com> <lemariva.com>]
#
# Credits
# Based on: http://www.tranquilidadtecnologica.com/2006/04/servidor-fake-dns-en-python.html
# mirror: http://code.activestate.com/recipes/491264-mini-fake-dns-server/
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

import socket
import select
import time
import _thread
import gc
from . import config

DEBUG = True


def dbg(msg, msg_=""):
    global DEBUG
    if DEBUG:
        print (str(msg) + str(msg_))

class DNSQuery:
    def __init__(self, data):
        self.data = data
        self.domain = ''
        tipo = (data[2] >> 3) & 15   # Opcode bits
        if tipo == 0:                     # Standard query
            ini = 12
            lon = data[ini]
            while lon != 0:
                self.domain += data[ini + 1:ini + lon + 1].decode('utf-8') + '.'
                ini += lon + 1
                lon = data[ini]
        dbg("searched domain:" + self.domain)

    def answer(self, ip):
        if self.domain:
            packet  = self.data[:2] + b'\x81\x80'
            packet += self.data[4:6] + self.data[4:6] + b'\x00\x00\x00\x00'   # Questions and Answers Counts
            packet += self.data[12:]                                          # Original Domain Name Question
            packet += b'\xC0\x0C'                                             # Pointer to domain name
            packet += b'\x00\x01\x00\x01\x00\x00\x00\x3C\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
            packet +=  bytes(map(int, ip.split('.')))                         # 4bytes of IP
        return packet

# A simple utility class to wait for incoming data to be
# read on a socket.
class poller:
    def __init__(self):
        self.poller = select.poll()
        self.targets = {}

    def add(self, socket = None):
        if not socket:
            return
        self.poller.register(socket, select.POLLIN)
        self.targets[socket.fileno()] = socket

    def remove(self, socket = None):
        if not socket:
            return
        self.poller.unregister(socket)
        del(self.targets[socket.fileno()])

    def poll(self, ip, timeout = 100):
        ready = self.poller.poll(timeout)
        for one_ready in ready:
            target = self.targets.get(one_ready[0].fileno(), None)
            if target:
                try:
                    data, sender = target.recvfrom(1024)
                    p = DNSQuery(data)
                    if any(word in p.domain for word in config.DNS_ANSWERS):
                        target.sendto(p.answer(ip), sender)
                        dbg('Replying: {:s} -> {:s}'.format(p.domain, ip))
                    #else:
                    #    dbg('Avoid responding: {:s} -> {:s}'.format(p.domain, ip))
                except Exception as e:
                    dbg('Exception occurs: ' + str(e))

class DNSServer():
    def __init__(self, host, port):
        self.ip = host
        self.udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_poller = poller()

    def start_listening(self):
        self.udps.bind(('',53))
        self.socket_poller.add(self.udps)

    def start_thread(self, arg):
        try:
            self.start_listening()
            while True:
                self.socket_poller.poll(self.ip, 100)
                time.sleep(1)
                gc.collect()    # avoid memory leak ?
        except KeyboardInterrupt as e:
             print ('DNSServer stopped: ' + str(e))
             self.udps.close()

    def start(self):
        dbg("* DNS seerver running on separated thread\n")
        _thread.start_new_thread(self.start_thread, ('',))
