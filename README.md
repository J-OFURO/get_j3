# get_j3
Command line tool for downloading J-OFURO3 data set
------------------------------------

 *USAGE :*  
     `get_j3.py [ VVV YYYY1 [TR] ]`  
     `get_j3.py [ VVV YYYY1 [YYYY2] [TR] ]`  
           VVV: variable name  
         YYYY1: year  
         YYYY2: if you want to get files for multiple years, please set year of end  
            TR: temporal resolution (CLM / MONTHLY / DAILY)  
       
         If you want to list all J-OFURO3 variables  
          just ./get_j3.py (without argument)  
          


衛星観測に基づく海面フラックスデータセットJ-OFURO3のダウンロードツール  

 *使い方:*  
     `get_j3.py [ VVV YYYY1 [TR] ]`  
     `get_j3.py [ VVV YYYY1 [YYYY2] [TR] ]`  
           VVV: 変数名  
         YYYY1: 年（4桁）  
         YYYY2: 複数年のファイルをダウンロードしたい場合は、期間の終わりの年を指定  
            TR: 時間解像度 (CLM / MONTHLY / DAILY)  
  
　　　　　引数なしでJ-OFURO3の変数のリストを表示

