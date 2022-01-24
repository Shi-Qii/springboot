/**
################################
##   三大法人買賣超，彙總
################################
**/

select top 30
	b.Processing_date,
        a.Industry_sector,
       a.Stock_num,
       a.Stock_name,
       c.Open_price,
       c.Close_price,
       round(b.Close_price-c.Close_price,2) as Up_down,
       round((b.Close_price-c.Close_price)/c.Close_price,2) as Up_down_pct,
       a.Foreign_investors,
       a.Investment_trust,
       a.Dealer,
       a.Total_buysell
from (
         --匯集完成後
         select
             a1.Stock_num,
             a1.Stock_name,
             a1.Industry_sector,
             sum(a1.Foreign_investors) Foreign_investors,
             sum(a1.Investment_trust) Investment_trust,
             sum(a1.Dealer) Dealer,
             sum(a1.Total_buysell) Total_buysell
         from (
                  select
                      a2.Stock_num,
                      b2.Stock_name,
                      b2.Industry_sector,
                      round((a2.Foreign_investors/1000),1) as Foreign_investors,
                      round((a2.Investment_trust/1000),1) as Investment_trust,
                      round((a2.Dealer/1000),1) as Dealer,
                      round((a2.Total_buysell/1000),1) as Total_buysell
                  from Institutional_investors a2 left join Stock_Category b2
                                                            on a2.Stock_num=b2.Stock_num
                  where  b2.Market_type='上市'
                    and  a2.processing_date in
                      --抓連續幾天加總使用top x
                         (select distinct top 3 a3.processing_date
                          from Institutional_investors a3
                          where a3.Market_type='上市'
                          order by a3.processing_date desc
                         )
              ) a1
         group by a1.Stock_num,a1.Stock_name,a1.Industry_sector
     ) a,Every_Transaction b,Every_Transaction c
where a.Stock_num=b.Stock_num
  and a.Stock_num=c.Stock_num
  and  b.processing_date =
       (select top 1 aa.processing_date
        from Institutional_investors aa
        where aa.Market_type='上市'
        order by aa.processing_date desc
       )
  and c.processing_date=dateadd(DD,-1,b.processing_date)
order by a.Foreign_investors desc;

/**
################################
##   三大法人個股
################################
**/

select top 5
    a.Processing_date,
    trim(a.Stock_num) as Stock_num,
    b.Stock_name,
    round((a.Foreign_investors/1000),1) as Foreign_investors,
    round((a.Investment_trust/1000),1) as Investment_trust,
    round((a.Dealer/1000),1) as Dealer,
    round((a.Total_buysell/1000),1) as Total_buysell
from Institutional_investors a,Stock_Category b
where  a.Stock_num=b.Stock_num
  and a.Stock_num='1110'
order by a.Processing_date desc;