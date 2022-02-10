'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/2/8    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

day_range  =>天數
    default=100

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='TWSE_Index':
    # check_code , day_range
    API.TWSE_index( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='TWSE_Institutional_Investors_Day':
    # check_code , day_range
    API.TWSE_Institutional_investors( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='TWSE_Category_Index':
    # check_code , day_range
    API.TWSE_Category_index( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='OTC_Index':
    # check_code , day_range
    API.OTC_index( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='OTC_Institutional_Investors_Day':
    # check_code , day_range
    API.OTC_Institutional_investors( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='OTC_Category_Index':
    # check_code , day_range
    API.OTC_Category_index( sys.argv[1], sys.argv[2])
