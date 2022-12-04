#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:34:35 2018
 
@author: bernardo carvalho

https://pypi.org/project/influxdb/

http://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdb.DataFrameClient.write_points
"""

import epics
import time
import os
import sys
import json
from datetime import datetime

#from influxdb_client import InfluxDBClient

from influxdb import InfluxDBClient

import numpy as np
sys.path

os.environ['EPICS_CA_ADDR_LIST'] = '192.168.1.110'
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

client = InfluxDBClient('localhost', 8086,  'oper', 'opertok', 'epics_isttok')
client.create_database('epics_isttok')

#client = InfluxDBClient('http://127.0.0.1:8086', username='oper', password='opertok')

#def onChanges(pvname=None, value=None, char_value=None, **kw):
#    pass

SCAN_PERIOD = 15

opstate_pv = epics.PV('ISTTOK:central:OPSTATE')
vv_press_pv = epics.PV('ISTTOK:central:VVessel-Pressure')

vv_press_pv.get(timeout=10)

#client.get_list_database()
def on_opstate_change(pvname=None, value=None, char_value=None, timestamp=None, **kw):
    print('PV  opstate Changed! {} {} {}'.format(pvname, char_value, timestamp))
    dt = datetime.fromtimestamp(timestamp)
    json_body = [{
        "measurement": "central",
        "tags": {"OPSTATE": opstate_pv.char_value},
        "time": dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {"VVessel-Pressure": vv_press_pv.value}
        }]
    print(json_body)
    client.write_points(json_body)

def on_vv_press_change(pvname=None, value=None, char_value=None, timestamp=None, **kw):
    print('PV Changed! {} {} {}'.format(pvname, value, timestamp))
    #data = [{"measurement": "central", "tags": {"host": "server01"}, "time": "2009-11-10T23:00:00Z", "fields": {
    #        "value": value }}]
    dt = datetime.fromtimestamp(timestamp)
    #json_data = json.dumps(data)
    json_body = [
    {
        "measurement": "central",
        "tags": {},
        "time": dt.strftime('%Y-%m-%dT%H:%M:%SZ'), # "2009-11-10T23:00:00Z",
        "fields": {
            "VVessel-Pressure": value}
    }
    ]
    print(json_body)
    # convert to datetime
    # https://stackoverflow.com/questions/51014779/how-send-proper-timestamp-to-influxdb-with-influxdb-python
    # write_points(points, time_precision=None, database=None, retention_policy=None, tags=None, batch_size=None, protocol=u'json', consistency=None)

    client.write_points(json_body)
    #client.write('epics_isttok','central', fields={'value': value})

    #print('PV Changed! {} {} {}'.format(pvname, value, time.ctime()))


#vv_press_pv.add_callback(on_vv_press_change)

tmp1_press_admission_pv = epics.PV('ISTTOK:central:TMPump1-PressureAdmission')
rpump1_press_pv = epics.PV('ISTTOK:central:RPump1-Pressure')

opstate_pv.add_callback(on_opstate_change)

# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
while True:
    #print('Hello from the Python Demo Service')
    pv1_m_data = rpump1_press_pv.get_with_metadata()
    pv2_m_data = tmp1_press_admission_pv.get_with_metadata()
    pv3_m_data = vv_press_pv.get_with_metadata()
    # pv4_m_data = i
    opstate_pv.get()
    dt = datetime.fromtimestamp(pv1_m_data['timestamp'])
    json_body = [{
        "measurement": "central",
        "tags": {'OPSTATE': opstate_pv.char_value},
        "time": dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            "RPump1-Pressure": pv1_m_data['value'],
            "TMPump1-PressureAdmission": pv2_m_data['value'],
            "VVessel-Pressure": pv3_m_data['value']
        }
    }]
    print(json_body)
    client.write_points(json_body)
    time.sleep(SCAN_PERIOD)


#    valuePrimary2  = epics.caget('ISTTOK:central:RPump2-Pressure')
#valueChamber1  = epics.caget('ISTTOK:central:VVessel-Pressure')
#valueTMPadmission  = epics.caget('ISTTOK:central:TMPump1-PressureAdmission')
#now = time.ctime()
# Open database connection

# 19 | ISTTOK:central:VVessel-Pressure
#sql_chamber ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 5 " \
    "AND `smpl_time` >  addtime(now(),'-01:00:00') ORDER BY `smpl_time` DESC LIMIT 100;"
# 21 | ISTTOK:central:RPump1-Pressure
#sql_primary ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 6 " \
    "AND `smpl_time` >  addtime(now(),'-01:00:00') ORDER BY `smpl_time` DESC LIMIT 100;"
        # ORDER BY `smpl_time` DESC LIMIT 250;"
# Execute the SQL command
print("result sql1")
# Fetch all the rows in a list of lists.
print("result sql2")


