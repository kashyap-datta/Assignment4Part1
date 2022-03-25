import pathlib
import os
#import config
#from config import rootdir
#_thisdir = str(pathlib.Path(_nowcast_datagen).parent.absolute())
#DEFAULT_CATALOG   = rootdir+'/../CATALOG.csv'
#DEFAULT_DATA_HOME = rootdir+'/../data'
#print(DEFAULT_DATA_HOME)
#print(str(pathlib.Path("__file__").parent.absolute()))

#print(os.path.abspath(os.curdir))
DEFAULT_CATALOG   = (os.curdir)+'/../CATALOG.csv'
#print(DEFAULT_CATALOG)
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
print(ROOT_DIR+'/CATALOG.csv')