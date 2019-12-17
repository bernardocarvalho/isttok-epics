# https://tecadmin.net/install-apache-mod-wsgi-on-ubuntu-16-04-xenial
# Include in  /etc/apache2/conf-available/mod-wsgi.conf :
# WSGIScriptAlias /isttok /var/www/html/wsgi_isttok_status.py
# and 
# systemctl restart apache2
#
#import epics
from epics import caget, caput, cainfo
import os

os.environ['EPICS_CA_ADDR_LIST'] = 'localhost 192.168.1.110'
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

def application(environ,start_response):
    status = '200 OK'
    RPump1press = caget('ISTTOK:central:RPump1-Pressure')
    RPump2press = caget('ISTTOK:central:RPump2-Pressure')
    TMPump1press = caget('ISTTOK:central:TMPump1-PressureAdmission')
    VVesselpress = caget('ISTTOK:central:VVessel-Pressure')
    rpiCurrentTime = caget('ISTTOK:central:CurrentTime')
    opState = caget('ISTTOK:central:OPSTATE.VAL')
    pulseNum = caget('ISTTOK:central:PULSE-NUMBER')
    html = '<html>\n' \
           '<body>\n' \
           ' <h1> ISTTOK Present Condition </h1> \n' 
    html += '<p>RPump1-Pressure: ' + str(RPump1press) + ' mBar </p>'       
    html += '<p>RPump2-Pressure: ' + str(RPump2press) + ' mBar </p>'       
    html += '<p>TMPump1-PressureAdmission: ' + str(TMPump1press) + ' mBar </p>'       
    html += '<p>VVessel-Pressure: ' + str(VVesselpress) + ' mBar </p>'       
    html += '<p>OPSTATE: ' + str(opState) + ' </p>'       
    html += '<p>PULSE-NUMBER: ' + str(pulseNum) + ' </p>'       
    html += '<p>Rpi CurrentTime: ' + str(rpiCurrentTime) + '  </p>'       
    html += '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    html = bytes(html, encoding= 'utf-8')
    return [html]
