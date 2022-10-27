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
from epics import caget, caput, cainfo, PV
import os

#os.environ['EPICS_CA_ADDR_LIST'] = 'localhost 192.168.1.110 192.168.1.120'
#os.environ['EPICS_CA_ADDR_LIST'] = 'localhost 192.168.1.110'
os.environ['EPICS_CA_ADDR_LIST'] = '192.168.1.110'
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

def application(environ,start_response):
    status = '200 OK'
    html = '<html>\n' \
        '<head> <meta charset="UTF-8"/> <title>ISTTOK Status page</title>' \
        '<meta http-equiv="refresh" content="5"> </head>' \
        '<body>\n  <h1> ISTTOK Present Vaccum Condition </h1> \n' 
    RP1pv = PV('ISTTOK:central:RPump1-Pressure')
    if RP1pv.connect(timeout=0.2):
        RPpreAlarm = caget('ISTTOK:central:RPump1-Pressure.SEVR', as_string=True)
        RP1A = caget('ISTTOK:central:RPump1-Pressure.SEVR')
        RPump1press = RP1pv.get(as_string=True)
        TMPump1press = caget('ISTTOK:central:TMPump1-PressureAdmission', as_string=True)
        VVesselpress = caget('ISTTOK:central:VVessel-Pressure', as_string=True)
        rpiCurrentTime = caget('ISTTOK:central:CurrentTime', as_string=True)
        opState = caget('ISTTOK:central:OPSTATE.VAL', as_string=True)
        opReq = caget('ISTTOK:central:OPREQ.VAL', as_string=True)
        opReqN = caget('ISTTOK:central:OPREQ.VAL')
        pulseNum = caget('ISTTOK:central:PULSE-NUMBER', as_string=True)
        OnBattery = caget('ISTTOK:central:UPS-OnBattery', as_string=True)
        RPump1Info = cainfo("ISTTOK:central:RPump1-Pressure", print_out=False)
        if RP1A == 0:
            html += '<p>RPump1-Pressure: ' + RPump1press + ' mBar. ALARM Status:' +RPpreAlarm+' </p>'       
        else:
            html += '<h3 style="color: #FF0000">RPump1-Pressure: ' + RPump1press + ' mBar. ALARM Status:' +RPpreAlarm+' </h3>'       
        html += '<p>TMPump1-PressureAdmission: ' + TMPump1press + ' mBar </p>'       
        html += '<p>VVessel-Pressure: ' + VVesselpress + ' mBar </p>'       
        html += '<p>OPSTATE: ' + opState + ', UPS-OnBattery: '+ OnBattery+ '</p>'       
        html += '<p>OPREQ: ' + opReq + '</p>'       
        if opReqN == 0:
            html += '<p>Note: you can try to login to rpi-isttok machine and do: '       
            html += '<pre>caput ISTTOK:central:OPREQ START</pre> </p>'       
        html += '<p>PULSE-NUMBER: ' + pulseNum + ' </p>'       
        html += '<p>Rpi CurrentTime: ' + rpiCurrentTime + ' </p>'       
    else:
        html += '<h2 style="color: #FF0000">Sorry, cannot connect to EPICS.</h2>'

    html += '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html'),
            ('Content-Length', str(len(html)))]
    start_response(status,response_header)
    return [html.encode('UTF-8')]
#    html = bytes(html, encoding= 'utf-8')
#    html += '<p>RPump1-Pressure: ' + str(RPump1press) + ' mBar </p>'       
#    return [html]
#    RPump1press = caget('ISTTOK:vacuum:RPump1-Pressure')
#    RPump2press = caget('ISTTOK:vacuum:RPump2-Pressure')
 #   html += '<p>RPump2-Pressure: ' + str(RPump2press) + ' mBar </p>'       
#    TMPump1press = caget('ISTTOK:vacuum:TMPump1-PressureAdmission')
#    VVesselpress = caget('ISTTOK:vacuum:VVessel-Pressure')
#    RPump2press = caget('ISTTOK:central:RPump2-Pressure')
#    html += '<pre> ' + RPump1Info + '</pre>'       
