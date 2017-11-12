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

# setup.py -- run once to install dependencies
# you need internet access to download the packages!

# wlan access
import network
import gc

ssid_ = 'FRITZBoxLeMa'
wp2_pass = '04974829851145306136'

sta_if = []


def do_connect():
    global sta_if
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid_, wp2_pass)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# connecting to WiFi
do_connect()
gc.collect()

# installing dependencies
# import upip
# upip.install('picoweb')
# gc.collect()
# upip.install('micropython-logging')
# gc.collect()
# upip.install('utemplate')
# gc.collect()
# upip.install('micropython-pkg_resources')
# gc.collect()
# upip.install('micropython-btreedb')
# gc.collect()

### ftp server for loading files
from ftp import ftpserver
ftp_server = ftpserver()
ftp_server.start_thread()

import captive_portal.__main__
captive_portal.__main__.main(host=sta_if.ifconfig()[0], port=80)
