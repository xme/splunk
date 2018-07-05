getiocmisp
==========

getiocmisp is a [Splunk](https://www.splunk.com) custom search command that helps to extract IOCs from a [MISP](http://misp-project.org/) instance.

![alt text](https://blog.rootshell.be/wp-content/uploads/2017/10/splunk-misp-1-1024x729.png)

getiocmisp relies on PyMISP. PyMISP requires Python 3 but only Python 2.7 is available in the Splunk environment. 
The script getiocmips.py is a wrapper and calls get-ioc-misp.py. This is best to keep your Splunk instance clean.

Prerequisites
=============
1. Install Python 3 on the Splunk server
2. Install PyMISP (see https://github.com/MISP/PyMISP)

Installation
============

1. Copy get-ioc-misp.py & mispconfig.py in /usr/local/bin

2. Edit mispconfig.py and specify your MISP URL and authorization key

3. Copy getiocmisp.py in /opt/splunk/etc/apps/<yourapp>/bin/

4. Copy the commands.conf or change the existing one in /opt/splunk/etc/apps/<yourapp>/local/

4. Restart Splunk

Usage
=====
See https://blog.rootshell.be/wp-content/uploads/2017/10/
