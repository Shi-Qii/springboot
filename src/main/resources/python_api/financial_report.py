'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/3/17    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

stock_num   =>股票代號
month  =>月份

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Financial_Ratio':
    # check_code , stock_num
    API.Financial_ratio( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Financial_Ratio_Season':
    # check_code , stock_num
    API.Financial_ratio_season( sys.argv[1], sys.argv[2])
