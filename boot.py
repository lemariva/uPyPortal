# Copyright [2017] [Mauro Riva <lemariva@mail.com> <lemariva.com>]
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

# boot.py -- run on boot-up
from uos import uname

access_point_name = 'Free-WiFi'
ap_if = None


def do_acess_point():
    global ap_if
    if uname().machine == 'ESP32 module with ESP32': # Wemos ESP-WROOM-32
        import network
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(True)
        ap_if.config(essid=access_point_name, authmode=network.AUTH_OPEN)
    elif  uname().machine == 'WiPy with ESP32': # Wipy 2.0
        import pycom
        from network import WLAN
        pycom.heartbeat(False)
        ap_if = WLAN(mode=WLAN.AP, ssid=access_point_name)
    ap_if.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '192.168.4.1'))


do_acess_point()


import captive_portal.__main__
captive_portal.__main__.main(host=ap_if.ifconfig()[0], port=80)
