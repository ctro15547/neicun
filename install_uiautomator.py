import subprocess
import getopt
import sys
opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:")

try:
	import urllib3
except:
	child = subprocess.Popen('python -m pip install urllib3 --trusted-host 10.75.22.30 -i http://10.75.22.30:8088/123/')
	child.wait()

try:
	import uiautomator
except:
	child = subprocess.Popen('python -m pip install uiautomator --trusted-host 10.75.22.30 -i http://10.75.22.30:8088/123/')
	child.wait()
