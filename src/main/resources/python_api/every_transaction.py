'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/3/13    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

Industry_sector   =>類股名稱
Market_type     =>市場
day_range  =>天數
    default=100
'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Industry_Sector_Every_Transaction':
    # check_code , Industry_sector , Market_type
    API.Industry_sector_every_transaction( sys.argv[1], sys.argv[2], sys.argv[3])
elif sys.argv[1]=='Ind_Every_Transaction':
    # check_code , stock_num , day_range default=100
    API.Ind_every_transaction( sys.argv[1], sys.argv[2], sys.argv[3])
