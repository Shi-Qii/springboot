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
計算長短期營收成長率

!!呼叫方式
check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃


#個股呼叫方式
check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃
stock_num   =>股票代碼


!!default   
long_month    =>長期計算幾個月份 預設12
short_month   =>短期計算幾個月份  預設3

'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Ind_Monthly_Revenue_Short_Long':
    API.Individual_stock_monthly_revenue_short_long(sys.argv[1],sys.argv[2], sys.argv[3])
elif sys.argv[1]=='Listed_Monthly_Revenue_Short_Long':
    API.Monthly_revenue_short_long(sys.argv[1],sys.argv[2])