'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/4/17    |       寶瑞       |            inital
###################################################################
'''

'''
參數:

check_code  =>檢查碼
    ex.代號
stock_num   =>股票代碼

'''


#導入API
import Function.API_Stragety as API_S

#導入sys
import sys


if sys.argv[1]=='Company_Power_ROE':
    # check_code  , stock_num
    API_S.Company_power_ROE( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_CFO':
    # check_code , stock_num
    API_S.Company_power_CFO( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_Cash_Debt_Ratio':
    # check_code , stock_num
    API_S.Company_power_Cash_debt_ratio( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_Total_Debt_Asset_Ratio':
    # check_code , stock_num
    API_S.Company_power_Total_debt_asset_ratio( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_Rev_Net_Income_Mar_Ratio':
    # check_code , stock_num
    API_S.Company_power_Rev_net_income_mar_ratio( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_Free_Cf':
    # check_code , stock_num
    API_S.Company_power_Free_cf( sys.argv[1], sys.argv[2])
elif sys.argv[1]=='Company_Power_Retained_Cash':
    # check_code , stock_num
    API_S.Company_power_Retained_cash( sys.argv[1], sys.argv[2])