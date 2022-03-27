'''
##################################################################
##                            修改履歷
##################################################################
==================================================================
##     日期       |      修改者      |            內容
==================================================================
##  2022/1/23    |       寶瑞       |  新增Institutional_investors_top
##  2022/1/29    |       寶瑞       |  新增Institutional_investors_top
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
            trim(a.Stock_num) as Stock_num, \
            a.Stock_name, \
            b.Open_price, \
            b.Close_price, \
            round(b.Close_price-c.Close_price,2) as Up_down, \
            round(((b.Close_price-c.Close_price)/c.Close_price)*100,3) as Up_down_pct, \
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
                from Institutional_investors a2 left join Stock_Category b2 \
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
        and c.processing_date = (select top 1 aa.processing_date \
            from Institutional_investors aa \
            where aa.Market_type='%s' \
            and aa.processing_date <> b.processing_date \
            order by aa.processing_date desc \
        ) \
        order by a.%s %s;" \
        %(market_type,total_day,market_type,market_type,market_type,cond,buy_sell)
    #進DB讀取資料存dataframe
    df=pd.read_sql(Institutional_investors_top_SQL,con=eng)
    
    #轉換dataframe to json
    result = df.to_json(orient = 'records', force_ascii=False)
    #print(check_code,'=',result)
    print(result)
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

def Individual_stock_institutional_investors(check_code,stock_num,day):

    #塞選特定期間法人買賣超狀況
    Individual_stock_Institutional_investors_SQL="select top %s \
    a.Processing_date, \
    trim(a.Stock_num) as Stock_num, \
    b.Stock_name, \
    c.Close_price, \
    round((a.Foreign_investors/1000),1) as Foreign_investors, \
    round((a.Investment_trust/1000),1) as Investment_trust, \
    round((a.Dealer/1000),1) as Dealer, \
    round((a.Total_buysell/1000),1) as Total_buysell \
    from Institutional_investors a,Stock_Category b ,Every_Transaction c \
    where  a.Stock_num=b.Stock_num \
    and a.Stock_num=c.Stock_num \
    and a.Processing_date=c.Processing_date \
    and a.Stock_num='%s' \
    order by a.Processing_date desc ;" \
    %(day,stock_num)

    #進DB讀取資料存dataframe
    df=pd.read_sql(Individual_stock_Institutional_investors_SQL,con=eng)
    #轉換dataframe to json
    result = df.to_json(orient = 'records', force_ascii=False)
    #print(check_code,'=',result)
    print(result)
    return result


'''
#########################################################################
##                   長短期營收成長率  個股                   
#########################################################################
計算長短期營收成長率

check_code  =>檢查碼
    ex.代號

stock_num   =>股票代碼

default
month_range => 取出月份數預設60個月

old default   
long_month    =>長期計算幾個月份 預設12
short_month   =>短期計算幾個月份  預設3

'''

def Individual_stock_monthly_revenue_short_long(check_code,stock_num,month_range=60):
    #塞選特定期間法人買賣超狀況
    Individual_stock_monthly_revenue_short_long_SQL="select top %s trim(a.Stock_num) as Stock_num, \
    b.Stock_name, \
    a.Year, \
    a.Month, \
    a.Mon_earn, \
    a.Short_earn, \
    a.Short_earn_last, \
    a.Growth_short, \
    a.Long_earn, \
    a.Long_earn_last, \
    a.Growth_long \
    from Long_Short_Revenue a left join Stock_Category b \
    on a.Stock_num=b.Stock_num \
    where  a.stock_num='%s' \
    order by a.stock_num asc,a.year desc,a.month desc" \
                                                    %(month_range,stock_num)


    #進DB讀取資料存dataframe
    df=pd.read_sql(Individual_stock_monthly_revenue_short_long_SQL,con=eng)

    #取出月股價
    Price_SQL="select top %s DATEPART(Year, a.Processing_date)-1911 Year, \
    DATEPART(Month, a.Processing_date) Month, \
    round(avg(a.close_price),2) Price \
    from Every_Transaction a \
    where a.Stock_num='%s' \
    group by DATEPART(Year, a.Processing_date), DATEPART(Month, a.Processing_date) \
    order by Year desc , Month desc ;" \
              %(int(month_range)+1,stock_num)
    df_price=pd.read_sql_query(Price_SQL,con=eng)


    #合併表格
    df=pd.merge(df, df_price, on=['Year','Month'],how='left')


    #轉換dataframe to json
    result = df.to_json(orient = 'records', force_ascii=False)
    #print(check_code,'=',result)
    print(result)



def Individual_stock_monthly_revenue_short_long_old(check_code,stock_num,long_month=12,short_month=3):

    long_month_tmp=long_month*2
    Individual_stock_Ronthly_revenue_short_long_SQL="select trim(a.Stock_num) as Stock_num, \
        b.Stock_name, \
        trim(str(a.Year)) Year, \
        trim(str(a.Month)) Month, \
        a.Mon_earn, \
        a.Last_year_mon_earn, \
        a.Growth_year \
        from Monthly_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where  CONCAT(a.Year, a.Month/10) in ( \
        select distinct top %s CONCAT(a1.year, a1.Month/10) \
        from Monthly_Revenue a1 \
        order by CONCAT(a1.year, a1.Month/10) desc) \
        and a.Stock_num='%s' \
        order by a.Stock_num desc,a.year desc,a.Month desc;" \
        %(long_month_tmp,stock_num)
    df=pd.read_sql(Individual_stock_Ronthly_revenue_short_long_SQL,con=eng)

    #長期 12個月  短期 3個月
    for i in range(1,long_month):
        df['Mon_earn_'+str(i)]=df['Mon_earn'].shift(-i)
        df['Last_year_mon_earn_'+str(i)]=df['Last_year_mon_earn'].shift(-i)

    #短期3個月相加
    tmp_short=df['Mon_earn']
    tmp_short_last=df['Last_year_mon_earn']
    for i in range(1,short_month):
        tmp_short=tmp_short+df['Mon_earn_'+str(i)]
        tmp_short_last=tmp_short_last+df['Last_year_mon_earn_'+str(i)]

    #長期12個月相加
    tmp_long=df['Mon_earn']
    tmp_long_last=df['Last_year_mon_earn']
    for i in range(1,long_month):
        tmp_long=tmp_long+df['Mon_earn_'+str(i)]
        tmp_long_last=tmp_long_last+df['Last_year_mon_earn_'+str(i)]

    #運算長短年增率
    df['Short_earn']=tmp_short
    df['Short_earn_last']=tmp_short_last
    df['Growth_short']=round((tmp_short/tmp_short_last-1)*100,1)

    df['Long_earn']=tmp_long
    df['Long_earn_last']=tmp_long_last
    df['Growth_long']=round((tmp_long/tmp_long_last-1)*100,1)

    df=df[['Stock_num','Stock_name','Year','Month','Mon_earn','Last_year_mon_earn','Growth_year','Short_earn','Short_earn_last','Growth_short', \
           'Long_earn','Long_earn_last','Growth_long']]

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   長短期月營收                    
#########################################################################
計算長短期營收成長率

check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃
year =>年份
    ex.111
month =>月份
    ex.1


old default   
long_month    =>長期計算幾個月份 預設12
short_month   =>短期計算幾個月份  預設3

'''

def Monthly_revenue_short_long(check_code,market_type,year,month):
    #塞選特定期間法人買賣超狀況
    Monthly_revenue_short_long_SQL="select  a.Year, \
    a.Month, \
    trim(a.Stock_num) as Stock_num, \
    b.Stock_name, \
    a.Mon_earn, \
    a.Short_earn, \
    a.Short_earn_last, \
    a.Growth_short, \
    a.Long_earn, \
    a.Long_earn_last, \
    a.Growth_long \
    from Long_Short_Revenue a left join Stock_Category b \
    on a.Stock_num=b.Stock_num \
    where a.year=%s \
    and a.month=%s \
    and a.Market_type='%s' \
    order by a.stock_num asc,a.year desc,a.month desc;" \
                                   %(year,month,market_type)


    #進DB讀取資料存dataframe
    df=pd.read_sql(Monthly_revenue_short_long_SQL,con=eng)

    #取出最新股價
    Price_SQL="select trim(a.Stock_num) as Stock_num, \
        a.Close_price \
        from Every_Transaction a \
        where a.Processing_date in ( \
        select top 1 Processing_date \
        from Every_Transaction \
        where Market_type='%s' \
        order by Processing_date desc) \
        and a.Market_type='%s';" \
              %(market_type,market_type)
    df_price=pd.read_sql_query(Price_SQL,con=eng)



    #合併表格
    df=pd.merge(df, df_price.iloc[:,:3], on='Stock_num',how='left')

    #轉換dataframe to json
    result = df.to_json(orient = 'records', force_ascii=False)
    #print(check_code,'=',result)
    print(result)
    return result



    #合併表格
    df=pd.merge(df, df_price.iloc[:,:3], on='Stock_num',how='left')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


def Monthly_revenue_short_long_old(check_code,market_type,long_month=12,short_month=3):

    long_month_tmp=long_month*2

    Individual_stock_Ronthly_revenue_short_long_SQL="select trim(a.Stock_num) as Stock_num, \
        b.Stock_name, \
        trim(str(a.Year)) Year, \
        trim(str(a.Month)) Month, \
        a.Mon_earn, \
        a.Last_year_mon_earn, \
        a.Growth_year \
        from Monthly_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where  CONCAT(a.Year, a.Month/10) in ( \
        select distinct top %s CONCAT(a1.year, a1.Month/10) \
        from Monthly_Revenue a1 \
        order by CONCAT(a1.year, a1.Month/10) desc) \
        and b.Market_type='%s' \
        order by a.Stock_num asc,a.year desc,a.Month desc;" \
        %(long_month_tmp,market_type)

    df=pd.read_sql(Individual_stock_Ronthly_revenue_short_long_SQL,con=eng)

    #長期 12個月  短期 3個月
    for i in range(1,long_month):
        df['Mon_earn_'+str(i)]=df['Mon_earn'].shift(-i)
        df['Last_year_mon_earn_'+str(i)]=df['Last_year_mon_earn'].shift(-i)

    #短期3個月相加
    tmp_short=df['Mon_earn']
    tmp_short_last=df['Last_year_mon_earn']
    for i in range(1,short_month):
        tmp_short=tmp_short+df['Mon_earn_'+str(i)]
        tmp_short_last=tmp_short_last+df['Last_year_mon_earn_'+str(i)]

    #長期12個月相加
    tmp_long=df['Mon_earn']
    tmp_long_last=df['Last_year_mon_earn']
    for i in range(1,long_month):
        tmp_long=tmp_long+df['Mon_earn_'+str(i)]
        tmp_long_last=tmp_long_last+df['Last_year_mon_earn_'+str(i)]

    #運算長短年增率
    df['Short_earn']=tmp_short
    df['Short_earn_last']=tmp_short_last
    df['Growth_short']=round((tmp_short/tmp_short_last-1)*100,1)

    df['Long_earn']=tmp_long
    df['Long_earn_last']=tmp_long_last
    df['Growth_long']=round((tmp_long/tmp_long_last-1)*100,1)

    df=df[['Stock_num','Stock_name','Year','Month','Mon_earn','Last_year_mon_earn','Growth_year','Short_earn','Short_earn_last','Growth_short', \
           'Long_earn','Long_earn_last','Growth_long']]

    #抓取最大月份，並且重新reset index
    df=df[(df['Month']==df['Month'].head(1).values[0]) & (df['Year']==df['Year'].head(1).values[0])].reset_index()
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)
    return result


'''
#########################################################################
##                   個股-月營收                    
#########################################################################
月營收

check_code  =>檢查碼
    ex.代號
stock_num   =>股票代碼

month_range=>月份數
default=12

'''
def Individual_stock_monthly_revenue(check_code,stock_num,month_range=12):

    #取出營收
    Individual_stock_monthly_revenue_SQL="select trim(a.Stock_num) as Stock_num, \
    b.Stock_name, \
    a.Year, \
    a.Month, \
    a.Mon_earn, \
    a.Last_mon_earn, \
    a.Growth_mon, \
    a.Last_year_mon_earn, \
    a.Growth_year, \
    a.Total_earn, \
    a.Last_total_earn, \
    a.Grow_total_earn, \
    a.Comment \
    from Monthly_Revenue a left join Stock_Category b \
    on a.Stock_num=b.Stock_num \
    where  CONCAT(a.Year, a.Month/10) in ( \
    select distinct top %s CONCAT(a1.year, a1.Month/10) \
    from Monthly_Revenue a1 \
    order by CONCAT(a1.year, a1.Month/10) desc ) \
    and a.Stock_num='%s' \
    order by a.Stock_num,a.year desc,a.month desc ; " \
    %(month_range,stock_num)
    df=pd.read_sql(Individual_stock_monthly_revenue_SQL,con=eng)

    #取出月股價
    Price_SQL="select top %s DATEPART(Year, a.Processing_date)-1911 Year, \
    DATEPART(Month, a.Processing_date) Month, \
    round(avg(a.close_price),2) Price \
    from Every_Transaction a \
    where a.Stock_num='%s' \
    group by DATEPART(Year, a.Processing_date), DATEPART(Month, a.Processing_date) \
    order by Year desc , Month desc ;" \
    %(int(month_range)+1,stock_num)
    df_price=pd.read_sql_query(Price_SQL,con=eng)


    #合併表格
    df=pd.merge(df, df_price, on=['Year','Month'],how='left')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)
    #return result


'''
#########################################################################
##                   月營收                    
#########################################################################
月營收

check_code  =>檢查碼
    ex.代號
market_type =>市場別
    ex.上市、上櫃

year=>年份

month=>月份

'''

def Monthly_revenue(check_code,market_type,year,month):

    Monthly_revenue_SQL="select trim(a.Stock_num) as Stock_num, \
        b.Stock_name, \
        trim(str(a.Year)) Year, \
        trim(str(a.Month)) Month, \
        a.Mon_earn, \
        a.Last_mon_earn, \
        a.Growth_mon, \
        a.Last_year_mon_earn, \
        a.Growth_year, \
        a.Total_earn, \
        a.Last_total_earn, \
        a.Grow_total_earn, \
        a.Comment \
        from Monthly_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where a.Year=%s \
        and a.month=%s \
        and a.Market_type='%s' \
        order by a.Stock_num,a.month desc; " \
                        %(year,month,market_type)
    df=pd.read_sql(Monthly_revenue_SQL,con=eng)

    #取出最新股價
    Price_SQL="select trim(a.Stock_num) as Stock_num, \
        a.Close_price \
        from Every_Transaction a \
        where a.Processing_date in ( \
        select top 1 Processing_date \
        from Every_Transaction \
        where Market_type='%s' \
        order by Processing_date desc) \
        and a.Market_type='%s';" \
              %(market_type,market_type)
    df_price=pd.read_sql_query(Price_SQL,con=eng)



    #合併表格
    df=pd.merge(df, df_price.iloc[:,:3], on='Stock_num',how='left')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)
    #return result



def Monthly_revenue_old(check_code,market_type):

    Monthly_revenue_SQL="select trim(a.Stock_num) as Stock_num, \
        b.Stock_name, \
        trim(str(a.Year)) Year, \
        trim(str(a.Month)) Month, \
        a.Mon_earn, \
        a.Last_mon_earn, \
        a.Growth_mon, \
        a.Last_year_mon_earn, \
        a.Growth_year, \
        a.Total_earn, \
        a.Last_total_earn, \
        a.Grow_total_earn, \
        a.Comment \
        from Monthly_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where  CONCAT(a.Year, a.Month/10) in ( \
        select distinct top 1 CONCAT(a1.year, a1.Month/10) \
        from Monthly_Revenue a1 \
        order by CONCAT(a1.year, a1.Month/10) desc ) \
        and b.Market_type='%s' \
        order by a.Stock_num,a.month desc; " \
                        %(market_type)
    df=pd.read_sql(Monthly_revenue_SQL,con=eng)

    #取出最新股價
    Price_SQL="select trim(a.Stock_num) as Stock_num, \
        a.Close_price \
        from Every_Transaction a \
        where a.Processing_date in ( \
        select top 1 Processing_date \
        from Every_Transaction \
        where Market_type='%s' \
        order by Processing_date desc) \
        and a.Market_type='%s'" \
              %(market_type,market_type)
    df_price=pd.read_sql_query(Price_SQL,con=eng)



    #合併表格
    df=pd.merge(df, df_price.iloc[:,:3], on='Stock_num',how='left')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)
    #return result



'''
#########################################################################
##                   上市、上櫃大盤指數                    
#########################################################################
大盤指數

day_range  =>天數
    default=100

'''

def TWSE_index(check_code,day_range=100):
    TWSE_index_SQL="select top %s \
    a.processing_date, \
    a.High_Price, \
    a.Low_Price, \
    a.Open_Price, \
    a.Close_Price, \
    a.Adj_Close_Price \
    from TWSE_Index a \
    order by processing_date desc; " \
                   %(day_range)

    df=pd.read_sql(TWSE_index_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


def OTC_index(check_code,day_range=100):
    OTC_index_SQL="select top %s \
    a.processing_date, \
    a.High_Price, \
    a.Low_Price, \
    a.Open_Price, \
    a.Close_Price \
    from OTC_Index a \
    order by processing_date desc; " \
                  %(day_range)

    df=pd.read_sql(OTC_index_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)



'''
#########################################################################
##                   上市、上櫃各類股指數                    
#########################################################################
各類股指數

day_range  =>天數
    default=100

'''

def TWSE_Category_index(check_code,day_range=100):
    TWSE_Category_index_SQL="select \
    a.Processing_date, \
    a.Index_name, \
    a.Close_price, \
    a.Num_share, \
    a.Cash_share, \
    a.Account_num, \
    a.Range_index, \
    a.Tran_weight \
    from Category_Index a \
    where a.Market_type='上市' \
    and  a.processing_date in  \
            (select distinct top %s processing_date  \
            from Institutional_investors b \
            where b.Market_type='上市'  \
            order by b.processing_date desc ) \
    order by a.Processing_date desc;" \
                            %(day_range)

    df=pd.read_sql(TWSE_Category_index_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


def OTC_Category_index(check_code,day_range=100):
    OTC_Category_index_SQL="select \
    a.Processing_date, \
    a.Index_name, \
    a.Close_price, \
    a.Num_share, \
    a.Cash_share, \
    a.Account_num, \
    a.Range_index, \
    a.Tran_weight \
    from Category_Index a \
    where a.Market_type='上櫃' \
    and  a.processing_date in  \
            (select distinct top %s processing_date  \
            from Institutional_investors b \
            where b.Market_type='上櫃'  \
            order by b.processing_date desc ) \
    order by a.Processing_date desc;" \
                           %(day_range)

    df=pd.read_sql(OTC_Category_index_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   上市、上櫃指數三大法人                    
#########################################################################
各類股指數

day_range  =>天數
    default=100

'''

def TWSE_Institutional_investors(check_code,day_range=100):
    TWSE_Institutional_investors_SQL="select top %s \
                    a.Processing_date, \
                    a.Foreign_investors, \
                    a.Investment_trust, \
                    a.Dealer, \
                    a.Total_buysell \
                    from Institutional_investors_TWSE a \
                    order by Processing_date desc " \
                                     %(day_range)

    df=pd.read_sql(TWSE_Institutional_investors_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

def OTC_Institutional_investors(check_code,day_range=100):
    OTC_Institutional_investors_SQL="select top %s \
                    a.Processing_date, \
                    a.Foreign_investors, \
                    a.Investment_trust, \
                    a.Dealer, \
                    a.Total_buysell \
                    from Institutional_investors_OTC a \
                    order by Processing_date desc " \
                                    %(day_range)

    df=pd.read_sql(OTC_Institutional_investors_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   上市、上櫃股票 代號+名稱+市場別                   
#########################################################################
各類股指數


'''

def Stock_num_name(check_code):
    Stock_Num_Name_SQL="select a.Stock_num+'-'+a.Stock_name+'('+a.Market_type+')' as Stock_nm\
                    from Stock_Category a \
                    order by a.Stock_num asc " \

    df=pd.read_sql(Stock_Num_Name_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                  每日成交價、本益比、淨值比                    
#########################################################################
個股指數

day_range  =>天數
    default=100
stock_num  =>股票代號

'''
def Ind_every_transaction(check_code,stock_num,day_range=365):
    Ind_every_transaction_SQL="select top %s a.Processing_date, \
           a.Stock_num, \
           b.Stock_name, \
           a.Open_price, \
           a.High_price, \
           a.Low_price, \
           a.Close_price, \
           round(a.Trading_volume/1000,0) as Trading_volume, \
           a.Yield_rate, \
           a.PE_rate, \
           a.PB_rate \
        from Every_Transaction a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where a.Stock_num='%s' \
        order by a.Processing_date desc;" \
                              %(day_range,stock_num)
    df=pd.read_sql(Ind_every_transaction_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   當月短期總營收突破長期營收                    
#########################################################################

year   =>年
month  =>月份
market_type =>市場別
    ex.上市、上櫃
'''

def Short_revenue_breakthrough_long(check_code,market_type,year,month):
    year=int(year)
    month=int(month)
    if month==1:
        last_year=year-1
        last_month=12
    else:
        last_year=year
        last_month=month-1


    Currently_month_SQL="select a.Year,a.Month,a.Stock_num,b.Stock_name,a.Growth_short,a.Growth_long \
        from Long_Short_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where a.year=%s \
        and a.month=%s \
        and b.Market_type='%s' \
        and a.growth_short>a.growth_long \
        order by a.stock_num asc;" \
                        %(year,month,market_type)

    df_cur=pd.read_sql(Currently_month_SQL,con=eng)


    Last_month_SQL="select a.Stock_num \
        from Long_Short_Revenue a left join Stock_Category b \
        on a.Stock_num=b.Stock_num \
        where a.year=%s \
        and a.month=%s \
        and b.Market_type='%s' \
        and a.growth_short<a.growth_long \
        order by a.stock_num asc;" \
                   %(last_year,last_month,market_type)

    df_last=pd.read_sql(Last_month_SQL,con=eng)


    df=pd.merge(df_cur,df_last, on='Stock_num')

    #取出最新股價
    Price_SQL="select trim(a.Stock_num) as Stock_num, \
        a.Close_price \
        from Every_Transaction a \
        where a.Processing_date in ( \
        select top 1 Processing_date \
        from Every_Transaction \
        where Market_type='%s' \
        order by Processing_date desc) \
        and a.Market_type='%s';" \
              %(market_type,market_type)
    df_price=pd.read_sql_query(Price_SQL,con=eng)


    #合併表格
    df=pd.merge(df, df_price, on='Stock_num',how='left')
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   當月長期總營收突破短期營收                    
#########################################################################

year   =>年
month  =>月份
market_type =>市場別
    ex.上市、上櫃
'''

def Long_revenue_breakthrough_short(check_code,market_type,year,month):
    year=int(year)
    month=int(month)
    if month==1:
        last_year=year-1
        last_month=12
    else:
        last_year=year
        last_month=month-1


    Currently_month_SQL="select a.Year,a.Month,a.Stock_num,b.Stock_name,a.Growth_short,a.Growth_long \
        from Long_Short_Revenue a left join Stock_Category b\
        on a.Stock_num=b.Stock_num \
        where a.year=%s \
        and a.month=%s \
        and b.Market_type='%s' \
        and a.growth_short<a.growth_long \
        order by a.stock_num asc;" \
                        %(year,month,market_type)

    df_cur=pd.read_sql(Currently_month_SQL,con=eng)


    Last_month_SQL="select a.Stock_num \
        from Long_Short_Revenue a left join Stock_Category b\
        on a.Stock_num=b.Stock_num \
        where a.year=%s \
        and a.month=%s \
        and b.Market_type='%s' \
        and a.growth_short>a.growth_long \
        order by a.stock_num asc;" \
                   %(last_year,last_month,market_type)

    df_last=pd.read_sql(Last_month_SQL,con=eng)


    df=pd.merge(df_cur,df_last, on='Stock_num')
    #取出最新股價
    Price_SQL="select trim(a.Stock_num) as Stock_num, \
        a.Close_price \
        from Every_Transaction a \
        where a.Processing_date in ( \
        select top 1 Processing_date \
        from Every_Transaction \
        where Market_type='%s' \
        order by Processing_date desc) \
        and a.Market_type='%s';" \
              %(market_type,market_type)
    df_price=pd.read_sql_query(Price_SQL,con=eng)


    #合併表格
    df=pd.merge(df, df_price, on='Stock_num',how='left')



    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   各類股當日成交價                    
#########################################################################

Industry_sector   =>類股名稱
Market_type     =>市場

'''

def Industry_sector_every_transaction(check_code,Industry_sector,Market_type):


    Industry_every_transaction_SQL="select a.Processing_date,       a.Stock_num,       b.Stock_name, \
                               a.Open_price,       a.High_price,       a.Low_price, \
                               a.Close_price,       a.Trading_volume,       a.Trading_count, \
                               a.Turnover,       a.Yield_rate,       a.Yield_year, \
                               a.PB_rate,       a.PE_rate \
                        from Every_Transaction a left join Stock_Category b \
                        on  a.Stock_num =b.Stock_num \
                        where b.Market_type='%s' \
                        and b.Industry_sector='%s' \
                        and a.Processing_date = ( \
                            select top 1 c.Processing_date \
                            from Every_Transaction c \
                            where c.Market_type='%s' \
                            order by c.Processing_date desc) \
                        order by a.Stock_num asc;" \
                                   %(Market_type,Industry_sector,Market_type)

    df=pd.read_sql(Industry_every_transaction_SQL,con=eng)


    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   上市、上櫃類股代號                 
#########################################################################
類股代號

'''

def Industry_sector_name(check_code):
    Industry_Sector_Name_SQL="select distinct Industry_sector \
                        from Stock_Category \
                        order by Industry_sector asc"

    df=pd.read_sql(Industry_Sector_Name_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   單季財務比率                    
#########################################################################

stock_num   =>股票代碼
'''

def Financial_ratio_season(check_code,stock_num):

    Financial_ratio_SQL="select * \
    from Financial_Ratio_Season \
    where Stock_num='%s' \
    order by year desc,season desc;" \
                        %(stock_num)
    df=pd.read_sql(Financial_ratio_SQL,con=eng)

    #取出每季平均股價
    Every_transaction_SQL="select Stock_num,DATEPART(yy , Processing_date)-1911 Year, \
        DATEPART(qq , Processing_date) Season, \
         avg(Close_price) Price \
        from Every_Transaction \
        where Stock_num='%s' \
        and Processing_date > DATEADD(qq, -32, GETDATE()) \
        group by DATEPART(yy , Processing_date),DATEPART(qq , Processing_date),Stock_num \
        order by year desc,season desc;" \
                          %(stock_num)
    Every_transaction=pd.read_sql(Every_transaction_SQL,con=eng)

    df=Every_transaction.merge(df,how='right',on=['Year','Season','Stock_num'])

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   累季財務比率                   
#########################################################################

stock_num   =>股票代碼
'''

def Financial_ratio(check_code,stock_num):
    Financial_ratio_SQL="select * \
    from Financial_Ratio \
    where Stock_num='%s' \
    order by year desc,season desc;" \
                        %(stock_num)
    df=pd.read_sql(Financial_ratio_SQL,con=eng)
    #取出每季平均股價
    Every_transaction_SQL="select Stock_num,DATEPART(yy , Processing_date)-1911 Year, \
        DATEPART(qq , Processing_date) Season, \
         avg(Close_price) Price \
        from Every_Transaction \
        where Stock_num='%s' \
        and Processing_date > DATEADD(qq, -32, GETDATE()) \
        group by DATEPART(yy , Processing_date),DATEPART(qq , Processing_date),Stock_num \
        order by year desc,season desc;" \
                          %(stock_num)
    Every_transaction=pd.read_sql(Every_transaction_SQL,con=eng)

    df=Every_transaction.merge(df,how='right',on=['Year','Season','Stock_num'])

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)
'''
#########################################################################
##                   累季現金流量表                    
#########################################################################

year   =>年
season  =>季
market_type =>市場別
    ex.上市、上櫃
'''

def Cash_flow_statement(check_code,market_type,year,season):
    Cash_flow_statement_SQL="select a.Stock_num,b.Stock_name,c.Close_price \
         ,a.CFO,a.CFI,a.CFF,a.ECF,a.CF,a.Pre_CF,a.Aft_CF \
    from Cash_Flow_Statement a left join Stock_Category b \
    on a.stock_num=b.stock_num \
    left join ( \
        select Stock_num,Close_price \
        from Every_Transaction \
        where Processing_date = ( \
            select top 1 Processing_date \
            from TWSE_Index \
            order by Processing_date desc \
            )  ) c \
    on a.Stock_num=c.Stock_num \
    where a.Market_type = '%s' \
    and a.year=%s \
    and a.season=%s \
    order by a.Stock_num asc;" \
                            %(market_type,year,season)

    df=pd.read_sql(Cash_flow_statement_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   單季現金流量表                    
#########################################################################

year   =>年
season  =>季
market_type =>市場別
    ex.上市、上櫃
'''

def Cash_flow_statement_season(check_code,market_type,year,season):
    Cash_flow_statement_season_SQL="select a.Stock_num,b.Stock_name,c.Close_price \
         ,a.CFO,a.CFI,a.CFF,a.ECF,a.CF,a.Pre_CF,a.Aft_CF \
    from Cash_Flow_Statement_season a left join Stock_Category b \
    on a.stock_num=b.stock_num \
    left join ( \
        select Stock_num,Close_price \
        from Every_Transaction \
        where Processing_date = ( \
            select top 1 Processing_date \
            from TWSE_Index \
            order by Processing_date desc \
            )  ) c \
    on a.Stock_num=c.Stock_num \
    where a.Market_type = '%s' \
    and a.year=%s \
    and a.season=%s \
    order by a.Stock_num asc;" \
                                   %(market_type,year,season)

    df=pd.read_sql(Cash_flow_statement_season_SQL,con=eng)
    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   累季綜合損益                
#########################################################################

year   =>年
season  =>季
market_type =>市場別
    ex.上市、上櫃
'''

def Comprehensive_income(check_code,market_type,year,season):

    Common_SQL="select a.Stock_num, \
        b.Stock_name, \
        a.Operating_profit, \
        a.Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Common a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
               %(market_type,year,season)


    Common=pd.read_sql(Common_SQL,con=eng)


    Bank_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Bank a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
             %(market_type,year,season)


    Bank=pd.read_sql(Bank_SQL,con=eng)


    Stock_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Stock a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
              %(market_type,year,season)


    Stock=pd.read_sql(Stock_SQL,con=eng)

    Finance_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Finance a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
                %(market_type,year,season)


    Finance=pd.read_sql(Finance_SQL,con=eng)


    Insurance_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Insurance a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
                  %(market_type,year,season)


    Insurance=pd.read_sql(Insurance_SQL,con=eng)


    Every_transaction_SQL="select Stock_num,Close_price \
        from Every_Transaction \
        where Processing_date in ( \
            select top 1 Processing_date \
            from Every_Transaction \
            order by Processing_date desc \
            ) \
        and Market_type='%s'" \
                          %(market_type)


    Every_transaction=pd.read_sql(Every_transaction_SQL,con=eng)


    df=Common.merge(Bank,how='outer')
    df=df.merge(Insurance,how='outer')
    df=df.merge(Stock,how='outer')
    df=df.merge(Finance,how='outer')
    df=Every_transaction.merge(df,how='right',on='Stock_num')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   單季綜合損益                
#########################################################################

year   =>年
season  =>季
market_type =>市場別
    ex.上市、上櫃
'''

def Comprehensive_income_season(check_code,market_type,year,season):

    Common_SQL="select a.Stock_num, \
        b.Stock_name, \
        a.Operating_profit, \
        a.Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Common_Season a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
               %(market_type,year,season)


    Common=pd.read_sql(Common_SQL,con=eng)


    Bank_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Bank_Season a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
             %(market_type,year,season)


    Bank=pd.read_sql(Bank_SQL,con=eng)


    Stock_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Stock_Season a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
              %(market_type,year,season)


    Stock=pd.read_sql(Stock_SQL,con=eng)

    Finance_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Finance_Season a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
                %(market_type,year,season)


    Finance=pd.read_sql(Finance_SQL,con=eng)


    Insurance_SQL="select \
        a.Stock_num, \
        b.Stock_name, \
        a.Pre_tax_income as Operating_profit, \
        0 as Out_operating_revence, \
        a.CNI, \
        a.Basic_EPS \
        from Comprehensive_Income_Insurance_Season a left join Stock_Category b \
        on a.stock_num=b.stock_num \
        where a.Market_type = '%s' \
          and a.year=%s \
          and a.season=%s \
        order by a.Stock_num asc" \
                  %(market_type,year,season)


    Insurance=pd.read_sql(Insurance_SQL,con=eng)


    Every_transaction_SQL="select Stock_num,Close_price \
        from Every_Transaction \
        where Processing_date in ( \
            select top 1 Processing_date \
            from Every_Transaction \
            order by Processing_date desc \
            ) \
        and Market_type='%s'" \
                          %(market_type)


    Every_transaction=pd.read_sql(Every_transaction_SQL,con=eng)


    df=Common.merge(Bank,how='outer')
    df=df.merge(Insurance,how='outer')
    df=df.merge(Stock,how='outer')
    df=df.merge(Finance,how='outer')
    df=Every_transaction.merge(df,how='right',on='Stock_num')

    result = df.to_json(orient = 'records', force_ascii=False)
    print(result)

'''
#########################################################################
##                   資產負債                
#########################################################################

year   =>年
season  =>季
market_type =>市場別
    ex.上市、上櫃
'''
def Balance_sheet(check_code,market_type,year,season):
    Common_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Common a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
               %(market_type,year,season)


    Common=pd.read_sql(Common_SQL,con=eng)

    Bank_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Bank a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
             %(market_type,year,season)


    Bank=pd.read_sql(Bank_SQL,con=eng)

    Finance_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Finance a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
                %(market_type,year,season)


    Finance=pd.read_sql(Finance_SQL,con=eng)

    Insurance_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Insurance a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
                  %(market_type,year,season)


    Insurance=pd.read_sql(Insurance_SQL,con=eng)

    Stock_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Stock a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
              %(market_type,year,season)


    Stock=pd.read_sql(Stock_SQL,con=eng)

    Other_SQL="select a.Stock_num, \
            b.Stock_name, \
            a.Asset, \
            a.Liability, \
            a.Total_equity, \
            a.Book_value_per_share \
            from Balance_Sheet_Other a left join Stock_Category b \
            on a.stock_num=b.stock_num \
            where a.Market_type = '%s' \
              and a.year=%s \
              and a.season=%s \
            order by a.Stock_num asc" \
              %(market_type,year,season)


    Other=pd.read_sql(Other_SQL,con=eng)

    Every_transaction_SQL="select Stock_num,Close_price \
            from Every_Transaction \
            where Processing_date in ( \
                select top 1 Processing_date \
                from Every_Transaction \
                order by Processing_date desc \
                ) \
            and Market_type='%s'" \
                          %(market_type)


    Every_transaction=pd.read_sql(Every_transaction_SQL,con=eng)

    df=pd.concat([Common, Bank,Finance,Insurance,Stock,Other],axis=0)

    Common.merge(Bank,how='inner',on='Stock_num')
    df=Every_transaction.merge(df,how='right',on='Stock_num')
    result = df.to_json(orient ='records', force_ascii=False)
    print(result)


'''
#########################################################################
##                   個股_基本資料                    
#########################################################################

stock_num   =>股票代碼
'''

def Basic_info(check_code,Stock_num):
    import datetime
    year = datetime.date.today().strftime("%Y")
    #基本資料
    data_SQL="select a.*,b.Main_business \
    from Stock_Category a left join Main_Business b \
    on a.Stock_num=b.Stock_num \
    where a.Stock_num='%s';" \
             %(Stock_num)
    data=pd.read_sql(data_SQL,con=eng)

    #股價
    price_SQL="select top 1 a.Close_price \
    from Every_Transaction a \
    where a.Stock_num='%s' \
    order by a.Processing_date desc" \
              %(Stock_num)
    price=pd.read_sql(price_SQL,con=eng)

    data['Current_equity']=price.Close_price[0]*data.Outstanding_shares[0]
    data['Funding_date']=data['Funding_date'].apply(lambda x:x+'  (成立'+str(+int(year)-int(x.split('-')[0]))+'年)')
    data['Listed_date']=data['Listed_date'].apply(lambda x:x+'  (上市'+str(+int(year)-int(x.split('-')[0]))+'年)')
    data[['Paid_in_capital','Current_equity']]=data[['Paid_in_capital','Current_equity']].applymap(lambda x:int(x)/100000000)
    result=data.to_json(orient='records',force_ascii=False)
    print(result)

'''
#########################################################################
##                   個股_重要子公司                    
#########################################################################

stock_num   =>股票代碼
'''
def Important_subsidiary(check_code,Stock_num):
    data_SQL="select * \
    from Important_Subsidiary a \
    where a.Stock_num='%s';" \
             %(Stock_num)

    data=pd.read_sql(data_SQL,con=eng)

    result=data.to_json(orient='records',force_ascii=False)
    print(result)

'''
#########################################################################
##                   個股_海外子公司                    
#########################################################################

stock_num   =>股票代碼
'''
def Oversea_company(check_code,Stock_num):
    data_SQL="select a.Stock_num \
    ,a.Oversea_company_name \
    ,a.Oversea_company \
    ,a.Region \
    ,a.Hold_equity \
    from Oversea_Company a \
    where a.Stock_num='%s' \
      and year in (select top 1 year \
                   from Oversea_Company \
                   where Stock_num=a.Stock_num \
                   order by year desc) \
      and season in (select top 1 season \
                     from Oversea_Company \
                     where Stock_num=a.Stock_num \
                     order by Season desc) \
    order by a.Hold_equity desc,a.Region desc;" \
             %(Stock_num)

    data=pd.read_sql(data_SQL,con=eng)

    result=data.to_json(orient='records',force_ascii=False)
    print(result)