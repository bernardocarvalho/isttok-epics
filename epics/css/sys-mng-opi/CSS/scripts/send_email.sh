#!/bin/sh
echo "Subject: SYSTEM MANAGER APPLICATION" > /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
echo "" >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
caget TEST-MNGR-HOST:MON2-TEMP-CPU >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
date +"%FT%T" >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
echo "E-MAIL: opertok@ipfn.tecnico.ulisboa.pt" >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
echo "IPFN/IST" >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
echo "SYSTEM MANAGER APPLICATION" >> /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
sendmail pricardofc@gmail.com < /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/notifications/email.txt
