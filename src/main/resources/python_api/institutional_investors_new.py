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
抓取三大法人資訊，以DB內最新日期為準

!!呼叫方式
check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃
buy_sell    =>買超或賣超
    ex.buy=買超  sell=賣超
cond        =>特定條件
    ex.Dealer、Investment_trust、Foreign_investors或是組合<Investment_trust+Dealer>
total_day   =>加總天數預設1天


#個股三大法人呼叫方式
check_code  =>檢查碼
    ex.代號
stock_num   =>股票代碼
    ex.1110
day         =>天數
    ex.1,2,3,5
'''


#導入API
import Function.API_new as API

#導入sys
import sys


if sys.argv[1]=='Listed_Foreign_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Dealer_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Dealer_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Dealer_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Trust_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Trust_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Total_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Total_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Dealer_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Trust_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Foreign_Trust_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Total_Buy':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='OTC_Total_Sell':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4])
elif sys.argv[1]=='Listed_Foreign_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Dealer_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Dealer_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Dealer_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Trust_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Foreign_Trust_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Trust_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Total_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Listed_Total_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Dealer_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Trust_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Foreign_Trust_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Trust_Dealer_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Total_Buy_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='OTC_Total_Sell_Day':
    API.Institutional_investors_top(sys.argv[1],sys.argv[2], sys.argv[3] ,sys.argv[4] ,sys.argv[5])
elif sys.argv[1]=='Ind_Institutional_Investors_Day':
    #個股三大法人
    API.Individual_stock_Institutional_investors(sys.argv[1],sys.argv[2], sys.argv[3])
