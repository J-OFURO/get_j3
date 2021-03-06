#!/usr/bin/env python2
#
# get_j3.py ---a script to download J-OFURO3 netCDF
#
# USAGE:
#   get_j3  VVV YYYY [YYYY]
#
# CHANGES: 
#   V1.3.0: 2017.11.15
#   V1.2.0: 2017.09.28
#   V1.0.0: 2017.02.01
#--------------------------------------------------  
version = 'V1.3.0'
#--------------------------------------------------  
import sys
from j3 import misc

defaults = misc.setup()
misc.header(version)
tr=defaults[0]
sr=defaults[1]
ver=defaults[2]
argvs = misc.get_argv()
var=argvs[0]
yr1=argvs[1]
yr2=argvs[2]
tr =argvs[3]
em = misc.email()
tdir='./J-OFURO3/' + tr + '/' + sr + '/' + var 
year = int(yr1)
fnames = []
while year <= int(yr2):
  yr = str(year)
  fname = misc.filename(var,tr,sr,ver,yr)
  print(fname)
  fnames.append(fname)
  year += 1
misc.get2(tdir,em,fnames)

