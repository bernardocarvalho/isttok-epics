#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# if you change this script "touch" it to reload by apache
# e.g touch /var/www/html/wsgi_isttok_status.py
"""
Created on December  8 16:34:35 2019
 https://tecadmin.net/install-apache-mod-wsgi-on-ubuntu-16-04-xenial

 Install:
 Include in  /etc/apache2/conf-available/mod-wsgi.conf :
 WSGIScriptAlias /isttok /var/www/html/wsgi_isttok_status.py
 and do:
 systemctl restart apache2
 
@author: bernardo carvalho@IPFN
"""
#
from epics import caget, caput, cainfo
import os

#os.environ['EPICS_CA_ADDR_LIST'] = 'localhost 192.168.1.110 192.168.1.120'
os.environ['EPICS_CA_ADDR_LIST'] = 'localhost 192.168.1.110'
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

def application(environ,start_response):
    status = '200 OK'
    RPump1press = caget('ISTTOK:central:RPump1-Pressure', as_string=True)
#    RPump2press = caget('ISTTOK:central:RPump2-Pressure')
    TMPump1press = caget('ISTTOK:central:TMPump1-PressureAdmission', as_string=True)
    VVesselpress = caget('ISTTOK:central:VVessel-Pressure', as_string=True)
#    RPump1press = caget('ISTTOK:vacuum:RPump1-Pressure')
#    RPump2press = caget('ISTTOK:vacuum:RPump2-Pressure')
#    TMPump1press = caget('ISTTOK:vacuum:TMPump1-PressureAdmission')
#    VVesselpress = caget('ISTTOK:vacuum:VVessel-Pressure')
    rpiCurrentTime = caget('ISTTOK:central:CurrentTime', as_string=True)
    opState = caget('ISTTOK:central:OPSTATE.VAL', as_string=True)
    pulseNum = caget('ISTTOK:central:PULSE-NUMBER', as_string=True)
    OnBattery = caget('ISTTOK:central:UPS-OnBattery', as_string=True)
# cainfo not working
    RPump1Info = cainfo("ISTTOK:central:RPump1-Pressure", print_out=False)
    html = '<html>\n' \
        '<head> <meta charset="UTF-8"/> <title>ISTTOK Status page</title>' \
        '<meta http-equiv="refresh" content="5"> </head>' \
        '<body>\n  <h1> ISTTOK Present Condition </h1> \n' 
#    html += '<p>RPump1-Pressure: ' + str(RPump1press) + ' mBar </p>'       
    html += '<p>RPump1-Pressure: ' + RPump1press + ' mBar </p>'       
 #   html += '<p>RPump2-Pressure: ' + str(RPump2press) + ' mBar </p>'       
    html += '<p>TMPump1-PressureAdmission: ' + TMPump1press + ' mBar </p>'       
    html += '<p>VVessel-Pressure: ' + VVesselpress + ' mBar </p>'       
    html += '<p>OPSTATE: ' + opState + ', UPS-OnBattery: '+ OnBattery+ '</p>'       
    html += '<p>Note: you can try to login to rpi-isttok machine and do: '       
    html += '<pre>caput ISTTOK:central:OPREQ START</pre> </p>'       
    html += '<p>PULSE-NUMBER: ' + pulseNum + ' </p>'       
    html += '<p>Rpi CurrentTime: ' + rpiCurrentTime + ' </p>'       
    html += '<pre> ' + RPump1Info + '</pre>'       
    html += '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html'),
            ('Content-Length', str(len(html)))]
    start_response(status,response_header)
    return [html.encode('UTF-8')]
#    html = bytes(html, encoding= 'utf-8')
#    return [html]
