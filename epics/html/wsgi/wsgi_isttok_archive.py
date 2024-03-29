#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:34:35 2018
 
@author: joao_loureiro/bernardo carvalho
add EPICS path to /etc/apache2/envvars

"""

import epics
import time
import os

os.environ['MPLCONFIGDIR'] = '/var/www/html/matplotlib'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter

import mpld3
from mpld3 import plugins, utils

import numpy as np
import MySQLdb

os.environ['EPICS_CA_ADDR_LIST']= '192.168.1.110 192.168.1.152'
os.environ['EPICS_CA_AUTO_ADDR_LIST']= 'NO'

def format_tick_labels(x, pos):
    return f"{x:5.2g}"
     
class HelloWorld(mpld3.plugins.PluginBase):  # inherit from PluginBase
    """Hello World plugin"""
    
    JAVASCRIPT = """
    mpld3.register_plugin("helloworld", HelloWorld);
    HelloWorld.prototype = Object.create(mpld3.Plugin.prototype);
    HelloWorld.prototype.constructor = HelloWorld;
    function HelloWorld(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };
    
    HelloWorld.prototype.draw = function(){
        // FIXME: this is a very brittle way to select the y-axis element
        var ax = this.fig.axes[0].elements[1];

        // see https://github.com/mbostock/d3/wiki/Formatting#d3_format
        // for d3js formating documentation
        ax.axis.tickFormat(d3.format(",.3e"));

        // TODO: use a function for tick values that
        // updates when values pan and zoom
        //ax.axis.tickValues([1,100,1000]);

        // HACK: use reset to redraw figure
        this.fig.reset(); 
    }
    """
    def __init__(self):
        self.dict_ = {"type": "helloworld"}

style_tooltip = """
<style>
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 800px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 1s;
}

.tooltip .tooltiptext::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
</style>
"""

def text_with_tooltip(text, tooltip):
    html = '<div class="tooltip">'+text+'\n'\
           '  <span class="tooltiptext">'+tooltip+'</span></div>'
    return html


def application(environ,start_response):
    status = '200 OK'
    valuePrimary1  = epics.caget('ISTTOK:central:RPump1-Pressure')
#    valuePrimary2  = epics.caget('ISTTOK:central:RPump2-Pressure')
    valueChamber1  = epics.caget('ISTTOK:central:VVessel-Pressure')
    valueTMPadmission  = epics.caget('ISTTOK:central:TMPump1-PressureAdmission')
    now = time.ctime()
    # Open database connection
#    db = MySQLdb.connect(host = "192.168.1.152",user = "report", passwd="$report", db = "archive")
    db = MySQLdb.connect(host = "192.168.1.100",user = "report", passwd="$report", db = "archive")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # channel_id =5 | ISTTOK:central:VVessel-Pressure
    sql_chamber ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 5 " \
                "AND `smpl_time` >  addtime(now(),'-01:00:00') ORDER BY `smpl_time` DESC LIMIT 100;"

#    sql_chamber ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 5 ORDER BY `smpl_time` DESC LIMIT 250;"
    # 21 | ISTTOK:central:RPump1-Pressure
    sql_primary ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 6 " \
                "AND `smpl_time` >  addtime(now(),'-01:00:00') ORDER BY `smpl_time` DESC LIMIT 100;"

#    sql_primary ="SELECT `smpl_time`, `float_val` FROM `sample` WHERE `channel_id` = 6 ORDER BY `smpl_time` DESC LIMIT 250;"
    # Execute the SQL command
    cursor.execute(sql_chamber)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    
    data_chamber = []
    for row in results:
        data_chamber.append([row[0],row[1]])
        
    # Execute the SQL command
    cursor.execute(sql_primary)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    
    data_primary = []
    for row in results:
        data_primary.append([row[0],row[1]])
    
    # disconnect from server
    db.close()
    #
    data_chamber = np.array(data_chamber)
    data_primary = np.array(data_primary)
    fig,axr = plt.subplots(1, sharex=True)
    
    axr.set_yscale('log')
    axr.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    axr.semilogy(data_chamber[:,0],data_chamber[:,1], color='red')
    axr.set_ylim(1e-8, 1e-4)

    # axr.legend(['Tokamak Chamber', 'Primary pump'], loc =2)
    axr.legend(['Tokamak Chamber'], loc='upper left')
    axr.set_xlabel('Time', fontsize = 15)
    axr.set_ylabel('TMP1Pressure/mbar', fontsize = 15, color = 'red')
    ax2 = axr.twinx() 
    ax2.plot(data_primary[:,0],data_primary[:,1], color='blue')
    ax2.set_ylabel('Rpump Pressure/mbar', fontsize = 15, color = 'blue')
    ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.3e'))
    ax2.set_ylim(1e-4, 1e-2)
    fig.set_size_inches(12,5, forward=True)
    fig.tight_layout()
    ax_fmt = HelloWorld()
    mpld3.plugins.connect(fig, ax_fmt)
    html2 = mpld3.fig_to_html(fig)
    html = '<html>\n' \
           '<head>' \
           '<title>ISTTOK EPICS WSGI Page</title>' \
           '</head>\n' \
           '<body>\n' \
           '<div>'+style_tooltip+'</div>\n'\
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'mod_wsgi EPICS ISTTOK info Page\n' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n' \
           ' '+text_with_tooltip('Rpump1 pressure: '+ '{0:.3e}'.format(valuePrimary1)+ ' mBar','ISTTOK:central:RPump1-Pressure')+'\n' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n' \
           ' '+text_with_tooltip('Turbopump 1 admission pressure: '+ '{0:.3e}'.format(valueTMPadmission)+ ' mBar','ISTTOK:central:TMPump1-PressureAdmission')+'\n' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n' \
           ' '+text_with_tooltip('Tokamak Vessel pressure: '+ '{0:.3e}'.format(valueChamber1)+ ' mBar','ISTTOK:central:VVessel-Pressure')+'\n' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n' \
           'Current Time: ' +now+ '\n' \
           '</div><center>\n'+html2 +'</center>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    html = bytes(html, encoding= 'utf-8')
    return [html]

#'</div><center>\n'+html2.encode('utf8')+'</center>\n' \
#           '<p> sys path: ' + os.environ['PATH'] + '</p>' \
