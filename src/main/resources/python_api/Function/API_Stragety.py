'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/4/17    |       寶瑞       |  Inital
###################################################################
'''


#共用模組
import pandas as pd
from sqlalchemy import create_engine
import sys
import io

#CMD轉換編碼使用，不可以在jupyter下執行，只能在.py下執行
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#連線DB
db = create_engine('mssql+pymssql://sa:password@127.0.0.1:1433/Financial?charset=utf8' ,pool_pre_ping=True) 
eng = db.connect()

'''
#########################################################################
##                  公司三力檢查 Company_Power             
#########################################################################
'''

'''
#獲利能力
近5年<20季>股東權益報酬率>15%  ROE
stock_num   =>股票代碼
ratio       =>大於多少ROE
'''
def Company_power_ROE(check_code,stock_num,ratio=15):
    ROE_SQL="SELECT TOP 20 YEAR,SEASON,ROE \
                        FROM FINANCIAL_RATIO_SEASON \
                        WHERE STOCK_NUM='%s' \
                        ORDER BY YEAR DESC,SEASON DESC" \
                        %(stock_num)
    ROE=pd.read_sql(ROE_SQL,con=eng)

    Value=len(ROE[ROE.ROE > ratio])
    
    if Value==20:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)

#償債能力
'''
1.近3年<12季>營業現金流皆>0，且穩定成長
stock_num   =>股票代碼
ratio       =>大於多少
'''
def Company_power_CFO(check_code,stock_num,ratio=0):
    
    CFO_SQL="SELECT TOP 12 YEAR,SEASON,CFO \
                            FROM CASH_FLOW_STATEMENT_SEASON \
                            WHERE STOCK_NUM='%s' \
                            ORDER BY YEAR DESC,SEASON DESC" \
                            %(stock_num)

    CFO=pd.read_sql(CFO_SQL,con=eng)

    Value=len(CFO[CFO.CFO > ratio])

    if Value==12:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)
    
#償債能力
'''
2.近3年<12季現金比率皆>25%
stock_num   =>股票代碼
ratio       =>大於多少
'''
def Company_power_Cash_debt_ratio(check_code,stock_num,ratio=25):
    CASH_DEBT_RATIO_SQL="SELECT top 12 YEAR,SEASON,CASH_DEBT_RATIO \
                        FROM FINANCIAL_RATIO_SEASON \
                        WHERE STOCK_NUM='%s' \
                        ORDER BY YEAR DESC,SEASON DESC" \
                        %(stock_num)
    CASH_DEBT_RATIO=pd.read_sql(CASH_DEBT_RATIO_SQL,con=eng)


    Value=len(CASH_DEBT_RATIO[CASH_DEBT_RATIO.CASH_DEBT_RATIO > ratio])

    if Value==12:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)


#償債能力
'''
3.近3年<12季負債比率皆<60%
stock_num   =>股票代碼
ratio       =>小於多少
'''
def Company_power_Total_debt_asset_ratio(check_code,stock_num,ratio=60):
    TOTAL_DEBT_ASSET_RATIO_SQL="SELECT top 12 YEAR,SEASON,TOTAL_DEBT_ASSET_RATIO \
                        FROM FINANCIAL_RATIO_SEASON \
                        WHERE STOCK_NUM='%s' \
                        ORDER BY YEAR DESC,SEASON DESC" \
                        %(stock_num)
    TOTAL_DEBT_ASSET_RATIO=pd.read_sql(TOTAL_DEBT_ASSET_RATIO_SQL,con=eng)

    Value=len(CASH_DEBT_RATIO[CASH_DEBT_RATIO.CASH_DEBT_RATIO < ratio])

    if Value==12:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)
    
#現金能力
'''
1.近8年<32季>盈餘品質皆>100%
stock_num   =>股票代碼
ratio       =>大於多少
'''
def Company_power_Rev_net_income_mar_ratio(check_code,stock_num,ratio=100):
    REVENUE_NET_INCOME_MARGIN_RATIO_SQL="SELECT top 8 A.YEAR,AVG(A.REVENUE_NET_INCOME_MARGIN_RATIO) REVENUE_NET_INCOME_MARGIN_RATIO \
                                        FROM ( \
                                        SELECT TOP 32 YEAR,SEASON,REVENUE_NET_INCOME_MARGIN_RATIO \
                                        FROM FINANCIAL_RATIO_SEASON \
                                        WHERE STOCK_NUM='%s' \
                                        ORDER BY YEAR DESC,SEASON DESC) A \
                                        GROUP BY A.YEAR \
                                        ORDER BY A.YEAR DESC" \
                                        %(stock_num)
    
    REVENUE_NET_INCOME_MARGIN_RATIO=pd.read_sql(REVENUE_NET_INCOME_MARGIN_RATIO_SQL,con=eng)

    Value=len(REVENUE_NET_INCOME_MARGIN_RATIO[REVENUE_NET_INCOME_MARGIN_RATIO.REVENUE_NET_INCOME_MARGIN_RATIO > ratio])
    
    if Value==8:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)
    
#現金能力
'''
2.近8年<32季>自由現金流皆>0
stock_num   =>股票代碼
ratio       =>大於多少
'''
def Company_power_Free_cf(check_code,stock_num,ratio=0):
    FREE_CF_SQL="SELECT top 8 A.YEAR,AVG(A.FREE_CF) FREE_CF \
                FROM ( \
                SELECT TOP 32 YEAR,SEASON,CFO+CFI FREE_CF  \
                FROM CASH_FLOW_STATEMENT \
                WHERE STOCK_NUM='%s' \
                ORDER BY YEAR DESC,SEASON DESC) A \
                GROUP BY A.YEAR \
                ORDER BY A.YEAR DESC" \
                %(stock_num)
    FREE_CF=pd.read_sql(FREE_CF_SQL,con=eng)

    Value=len(FREE_CF[FREE_CF.FREE_CF > ratio])

    if Value==8:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)
    
#現金能力
'''
3.近8年<32季>現金活水率(每股自由現金流÷每股現金股利)皆>0
stock_num   =>股票代碼
ratio       =>大於多少
'''
def Company_power_Retained_cash(check_code,stock_num,ratio=0):

    RETAINED_EARNINGS_CASH_SQL="SELECT TOP 8 YEAR,SUM(RETAINED_EARNINGS_CASH) RETAINED_EARNINGS_CASH \
                                FROM STOCK_DIVIDEN \
                                WHERE STOCK_NUM='%s' \
                                GROUP BY YEAR \
                                ORDER BY YEAR DESC" \
                                %(stock_num)
    RETAINED_EARNINGS_CASH=pd.read_sql(RETAINED_EARNINGS_CASH_SQL,con=eng)

    PER_SHARE_FREE_CF_SQL="SELECT A.YEAR,SUM(A.PER_SHARE_FREE_CF) PER_SHARE_FREE_CF \
                            FROM ( \
                            SELECT TOP 32 YEAR,SEASON,PER_SHARE_FREE_CF \
                            FROM FINANCIAL_RATIO_SEASON \
                            WHERE STOCK_NUM='%s' \
                            ORDER BY YEAR DESC,SEASON DESC) A \
                            GROUP BY A.YEAR \
                            ORDER BY A.YEAR DESC" \
                            %(stock_num)
    PER_SHARE_FREE_CF=pd.read_sql(PER_SHARE_FREE_CF_SQL,con=eng)

    tmp=RETAINED_EARNINGS_CASH.merge(PER_SHARE_FREE_CF,on='YEAR')

    tmp['result']=tmp.PER_SHARE_FREE_CF/tmp.RETAINED_EARNINGS_CASH


    Value=len(tmp[tmp.result > ratio])

    if Value==8:
        Result='True'
    else:
        Result='Fasle'

    df=pd.DataFrame(data=[[Result,Value]],columns=['Result','Value'])

    result = df.to_json(orient = 'records', force_ascii=False)

    print(result)
