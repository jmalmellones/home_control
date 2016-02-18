"""
    Home Control. Controlling a smart home.
    Copyright (C) 2016 Jose Miguel Almellones Cabello

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import time
import urllib2
import json

config_file = 'home_control.json'
config = json.load(open(config_file))

vera_ip = config['vera_ip']

termo = {"id": 4, "nombre": "termo"}
luz_salon = {"id": 27, "nombre": "luz salon"}


def endpoint_switch_power(ip, device):
    return "http://" + ip + ":3480/data_request?id=lu_action&output_format=json&DeviceNum=" + str(device["id"]) + \
           "&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue="


def encender(dispositivo):
    url = endpoint_switch_power(vera_ip, dispositivo) + "1"
    response = urllib2.urlopen(url)
    html = response.read()
    print html


def apagar(dispositivo):
    url = endpoint_switch_power(vera_ip, dispositivo) + "0"
    response = urllib2.urlopen(url)
    html = response.read()
    print html


if __name__ == "__main__":
    while True:
        apagar(luz_salon)
        time.sleep(30)  # 30 seconds
        encender(luz_salon)
        time.sleep(30)  # 30 seconds
