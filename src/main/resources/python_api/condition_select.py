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

year   =>年
month  =>月份

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Short_Revenue_Breakthrough_Long':
    # check_code , year , month
    API.Short_revenue_breakthrough_long( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1]=='Long_Revenue_Breakthrough_Short':
    # check_code , year , month
    API.Short_revenue_breakthrough_long( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
