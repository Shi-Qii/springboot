'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/1/23    |       寶瑞       |  新增Institutional_investors_top

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
##                   三大法人  Institutional_investors                  
#########################################################################
塞選top30 上市法人買賣超
抓取最新的日期資訊
check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃
buy_sell    =>買超或賣超
    ex.buy=買超  sell=賣超
cond        =>特定條件 
    ex.Dealer、Investment_trust、Foreign_investors或是組合<Investment_trust+Dealer>
total_day   =>加總天數預設1天
'''
def Institutional_investors_top(check_code,market_type,buy_sell,cond,total_day=1):
    
    #判斷買超或賣超
    if buy_sell=='buy':
        buy_sell='desc'
    else:
        buy_sell='asc'
        
    #塞選top30 特定市場、法人買賣超、加總幾天 SQL
    Institutional_investors_top_SQL="select top 30 \
            b.Processing_date, \
            a.Industry_sector, \
            trim(a.Stock_num), \
            a.Stock_name, \
            c.Open_price, \
            c.Close_price, \
            round(b.Close_price-c.Close_price,2) as Up_down, \
            round((b.Close_price-c.Close_price)/c.Close_price,2) as Up_down_pct, \
            a.Foreign_investors, \
            a.Investment_trust, \
            a.Dealer, \
            a.Total_buysell \
        from ( \
            select  \
                a1.Stock_num, \
                a1.Stock_name, \
                a1.Industry_sector, \
                sum(a1.Foreign_investors) Foreign_investors, \
                sum(a1.Investment_trust) Investment_trust, \
                sum(a1.Dealer) Dealer, \
                sum(a1.Total_buysell) Total_buysell \
            from (   \
                select  \
                    a2.Stock_num, \
                    b2.Stock_name, \
                    b2.Industry_sector, \
                    round((a2.Foreign_investors/1000),1) as Foreign_investors,  \
                    round((a2.Investment_trust/1000),1) as Investment_trust,  \
                    round((a2.Dealer/1000),1) as Dealer,  \
                    round((a2.Total_buysell/1000),1) as Total_buysell  \
                from Institutional_investors a2 left join Stock_Category b2\
                on a2.Stock_num=b2.Stock_num \
                where  b2.Market_type='%s'  \
                and  a2.processing_date in \
                    (select distinct top %s a3.processing_date \
                        from Institutional_investors a3 \
                        where a3.Market_type='%s'  \
                        order by a3.processing_date desc \
                    ) \
            ) a1 \
            group by a1.Stock_num,a1.Stock_name,a1.Industry_sector \
            ) a,Every_Transaction b,Every_Transaction c \
        where a.Stock_num=b.Stock_num \
        and a.Stock_num=c.Stock_num \
        and  b.processing_date = \
            (select top 1 aa.processing_date \
                from Institutional_investors aa \
                where aa.Market_type='%s' \
                order by aa.processing_date desc \
            ) \
        and c.processing_date=dateadd(DD,-1,b.processing_date) \
        order by a.%s %s;"\
        %(market_type,total_day,market_type,market_type,cond,buy_sell)
        
    #進DB讀取資料存dataframe
    df=pd.read_sql(Institutional_investors_top_SQL,con=eng)
    
    #轉換dataframe to json
    result = df.to_json(orient = 'columns', force_ascii=False)
    print(check_code,'=',result)
    return result



'''
#########################################################################
##                 三大法人  個股Institutional_investors                 
#########################################################################
塞選特定期間法人買賣超狀況 
抓取最新的日期資訊
stock_num   =>股票代碼
day         =>天數
'''

def Individual_stock_Institutional_investors(check_code,stock_num,day):

    #塞選特定期間法人買賣超狀況
    Individual_stock_Institutional_investors_SQL="select top %s \
    a.Processing_date, \
    trim(a.Stock_num), \
    b.Stock_name, \
    round((a.Foreign_investors/1000),1) as Foreign_investors, \
    round((a.Investment_trust/1000),1) as Investment_trust, \
    round((a.Dealer/1000),1) as Dealer, \
    round((a.Total_buysell/1000),1) as Total_buysell \
    from Institutional_investors a,Stock_Category b \
    where  a.Stock_num=b.Stock_num \
    and a.Stock_num='%s' \
    order by a.Processing_date desc;" \
    %(day,stock_num)


    #進DB讀取資料存dataframe
    df=pd.read_sql(Individual_stock_Institutional_investors_SQL,con=eng)
    #轉換dataframe to json
    result = df.to_json(orient = 'columns', force_ascii=False)
    print(check_code,'=',result)
    return result