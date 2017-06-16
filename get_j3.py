#!/usr/bin/env python
#
# get_j3.py ---a script to download J-OFURO3 netCDF
#
# USAGE:
#   get_j3  VVV YYYY [YYYY]
#
# CHANGES: 
#   V1.0.0: 2017.02.01
#--------------------------------------------------  
version = 'V1.1.0'
#--------------------------------------------------  
import sys
from j3 import misc

defaults = misc.setup()
misc.header(version)
argvs = misc.get_argv()
var=argvs[0]
yr1=argvs[1]
yr2=argvs[2]
em = misc.email()
tr=defaults[0]
sr=defaults[1]
ver=defaults[2]
tdir='./J-OFURO3/' + tr + '/' + sr + '/' + var 
year = int(yr1)
fnames = []
while year <= int(yr2):
  yr = str(year)
  fname = misc.filename(var,tr,sr,ver,yr)
  fnames.append(fname)
  year += 1
misc.get2(tdir,em,fnames)

