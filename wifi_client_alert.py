#!/usr/bin/python3
import subprocess
#import /opt/splunk/etc/apps/framework/contrib/splunk-sdk-python/splunklib ##FLAGFLAG

# Name:    wifi_client_alert.py
# Date:    1/13/16
# Purpose: This will send an alert when a new client accepts a DHCP address
# NOTE: 
#
###########################################################################
# FUNCTIONS
###########################################################################
def SPLUNK_SEARCH():
   arg1 = "'sourcetype=asus host=192.168.1.1 DHCPACK'"
#   subprocess.Popen([r"/opt/splunk/bin/splunk search 'sourcetype=asus host=192.168.1.1 DHCPACK'"])
   subprocess.call(["/opt/splunk/bin/splunk","search","'sourcetype=asus","DHCPACK'"])
#   call(["ls","-l","/etc/resolv.conf"]) ##FLAGFLAG

#def ALERT():
   

###########################################################################
# MAIN
###########################################################################
SPLUNK_SEARCH()
