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
elif sys.argv[1]=='Cash_Flow_Statement':
    # check_code , market_type , year , season
    API.Cash_flow_statement( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1]=='Cash_Flow_Statement_Season':
    # check_code , market_type , year , season
    API.Cash_flow_statement_season( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1]=='Comprehensive_Income':
    # check_code , market_type , year , season
    API.Comprehensive_income( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1]=='Comprehensive_Income_Season':
    # check_code , market_type , year , season
    API.Comprehensive_income_season( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1]=='Balance_Sheet':
    # check_code , market_type , year , season
    API.Balance_sheet( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])