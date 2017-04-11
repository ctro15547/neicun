import subprocess

try:
	import urllib3
except:
	child = subprocess.Popen('pip install urllib3 -i https://pypi.douban.com/simple')
	child.wait()

try:
	import uiautomator
except:
	child = subprocess.Popen('pip install uiautomator -i https://pypi.douban.com/simple')
	child.wait()