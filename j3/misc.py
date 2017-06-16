#!/usr/bin/env python
#
# j3.misc.py
#
# CHANGES: 
#   V1.0.0: 2017.02.01
#--------------------------------------------------  
def get_argv():
    import sys
    nargv = len(sys.argv)
    if nargv == 3:
      var = sys.argv[1]
      yr1 = sys.argv[2]
      yr2 = yr1
    elif nargv == 4:
      var = sys.argv[1]
      yr1 = sys.argv[2]
      yr2 = sys.argv[3]
    elif nargv == 1:
      var_list()
      eos()
    else:
      error(1)
      usage()
      eos()
    return(var,yr1,yr2)

def header(version):
    print '---------------------------'
    print ' get_j3.py', '  ', version
    print '---------------------------'

def setup():
    tr='DAILY'
    sr='HR'
    ver='V1.0'
    return(tr,sr,ver)

def var_name():
    var_names = ['LHF', 'SHF', 'SWR', 'LWR', 'NHF',\
            'ULWR', 'DLWR', 'TAUX', 'TAUY', 'FWF', 'EVAP', 'RAIN',\
            'SST', 'WND', 'UWND', 'VWND', 'QA', 'QS', 'DQ', 'TA10','DT']
    return(var_names)

def var_long_name():
    var_long_names = {'LHF':'Latent Heat Flux',\
                      'SHF':'Sensible Heat Flux',\
                      'SWR':'Net shortwave radiation',\
                      'LWR':'Net longwave radiation',\
                      'NHF':'Net heat flux',\
                      'ULWR':'Upward longwave radiation',\
                      'DLWR':'Downward longwave radiation',\
                      'TAUX':'Zonal component of momentum flux',\
                      'TAUY':'Meridional component of momentum flux',\
                       'FWF':'Freshwater flux',\
                      'EVAP':'Evaporation',\
                      'RAIN':'Precipitation',\
                       'SST':'Sea surface temperature',\
                       'WND':'Scalar wind speed',\
                      'UWND':'Zonal wind speed',\
                      'VWND':'Meridonal wind speed',\
                        'QA':'Air specifif humidity',\
                        'QS':'Saturated specifif humidity at surface',\
                        'DQ':'Humidity difference: QS minus QA',\
                      'TA10':'Air temperature',\
                        'DT':'Temperature difference: SST minus TA10'\
                     }
    return(var_long_names)

def var_list():
    print ' J-OFURO3 Variables:'
    var_names = var_name()
    var_long_names = var_long_name()
    for var in var_names:
       print ' ',var5(var), var_long_names[var]

def email():
     import sys
     print ' Enter your e-mail address (ex.,j-ofuro@xxx.jp) :'
     a = sys.stdin.readline()
     em = a.strip()
     return(em)

def filename(var,tr,sr,ver,year):
     fname = 'J-OFURO3_' + var + '_' + ver + '_' + tr + '_' + sr + '_' + year + '.nc' + '.gz'
     return(fname)

def var5(var):
     if len(var) == 5:
      var5=var
     elif len(var) == 4:
      var5=var+' '
     elif len(var) == 3:
      var5=var+'  '
     elif len(var) == 2:
      var5=var+'   '
     return(var5)

def get(tdir,em,files):
    from ftplib import FTP
    site = 'j-ofuro.scc.u-tokai.ac.jp'
    user = 'anonymous'
    key = em
    dir  = tdir
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
    for file in files:
      command='RETR ' + file
      f = open(file+'.gz', 'wb')
      print(command)
      ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()

def get2(tdir,em,files):
    import os
    from progressbar import ProgressBar,Percentage,Bar
    from ftplib import FTP

    def handleget2(block):
       pbar.update(pbar.currval + len(block))
       f.write(block)

    site = 'j-ofuro.scc.u-tokai.ac.jp'
    user = 'anonymous'
    key = em
    dir  = tdir
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
    ftps.sendcmd("TYPE i") 
    for file in files:
      if ftps.size(file) == 0:
        print "%s 0 bytes passing..." % file.filename
      else: 
        pbar=ProgressBar(widgets=[Percentage(), Bar()], maxval=ftps.size(file)).start()
        command='RETR ' + file
        f = open(file+'.gz', 'wb')
        ftps.retrbinary(command, handleget2 )
        pbar.finish() 
        print "Finished"

    ftps.quit()
    f.close()




def usage():
    print' USAGE : get_j3.py [ VVV YYYY [YYYY] ]'
    print'           VVV: variable name'
    print'          YYYY: year'
    print'          '
    print'          If you want to list all J-OFURO3 variables '
    print'          just ./get_j3.py (without argument)'
    print'          '

def error(nerr):
    if nerr == 1:
      print' ERROR : invalid input'
    else:
      print ' ERROR'

def eos():
    import sys
    print' EOS:'
    sys.exit()
