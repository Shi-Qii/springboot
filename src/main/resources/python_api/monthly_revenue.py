'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/1/23    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃
stock_num   =>股票代碼

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Ind_Monthly_Revenue_Short_Long':
    # check_code , market_type , stock_num
    API.Individual_stock_monthly_revenue_short_long( sys.argv[1], sys.argv[2], sys.argv[3])
elif sys.argv[1]=='Listed_Monthly_Revenue_Short_Long':
    # check_code , market_type
    API.Monthly_revenue_short_long( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Ind_Monthly_Revenue_Mon':
    #check_code , stock_num
    API.Individual_stock_monthly_revenue( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Listed_Monthly_Revenue':
    # check_code , market_type
    API.Monthly_revenue( sys.argv[1], sys.argv[2])