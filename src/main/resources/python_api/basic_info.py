'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/3/22    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

stock_num   =>股票代碼

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Basic_Info':
    # check_code  , stock_num
    API.Basic_info( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Important_Subsidiary':
    # check_code , stock_num
    API.Important_subsidiary( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Oversea_Company':
    # check_code , stock_num
    API.Oversea_company( sys.argv[1], sys.argv[2])

