import subprocess
import sys

def install(package):
    print 'installing', package
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def install_wmi()
    install('wmi')
    install('pywin32')