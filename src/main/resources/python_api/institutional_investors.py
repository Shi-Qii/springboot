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
buy_sell    =>買超或賣超
    ex.buy=買超  sell=賣超
cond        =>特定條件
    ex.Dealer、Investment_trust、Foreign_investors或是組合<Investment_trust+Dealer>
day         =>天數
    ex.1,2,3,5
'''


#導入API
import Function.API as API

#導入sys
import sys


if sys.argv[1]=='Listed_Foreign_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Dealer_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Dealer_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Dealer_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Trust_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Trust_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Total_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Total_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Dealer_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Trust_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Trust_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Total_Buy':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Total_Sell':
    # check_code , market_type , buy_sell , cond
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Dealer_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Dealer_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Dealer_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Trust_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Trust_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Total_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Total_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Dealer_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Trust_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Trust_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Total_Buy_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Total_Sell_Day':
    # check_code , market_type , buy_sell , cond ,day
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Ind_Institutional_Investors_Day':
    # check_code , stock_num ,day
    API.Individual_stock_institutional_investors(sys.argv[1],sys.argv[2], sys.argv[3])
