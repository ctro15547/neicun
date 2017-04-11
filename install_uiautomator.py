import subprocess
import getopt
import sys
opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:")

try:
	import urllib3
except:
	child = subprocess.Popen('python -m pip install urllib3 -i https://pypi.douban.com/simple')
	child.wait()

try:
	import uiautomator
except:
	child = subprocess.Popen('python -m pip install uiautomator -i https://pypi.douban.com/simple')
	child.wait()