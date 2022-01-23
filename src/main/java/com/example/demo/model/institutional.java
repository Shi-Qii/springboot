package com.example.demo.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Date;


@Entity
@Table(name = "Institutional_investors")
public class institutional {
//(
//    Processing_date   date,
//    Stock_num         nvarchar(10),
//    Foreign_investors int,
//    Investment_trust  int,
//    Dealer            int,
//    Total_buysell     int,
//    Market_type       nvarchar(10)
//)

    @Id

    private Date Processing_date;
    private String Stock_num;
    private Integer Foreign_investors;
    private Integer Investment_trust;
    private Integer Dealer;
    private Integer Total_buysell;
    private String Market_type;

    @Override
    public String toString() {
        return "institutional{" +
                "Processing_date=" + Processing_date +
                ", Stock_num='" + Stock_num + '\'' +
                ", Foreign_investors=" + Foreign_investors +
                ", Investment_trust=" + Investment_trust +
                ", Dealer=" + Dealer +
                ", Total_buysell=" + Total_buysell +
                ", Market_type='" + Market_type + '\'' +
                '}';
    }

    public Date getProcessing_date() {
        return Processing_date;
    }

    public void setProcessing_date(Date processing_date) {
        Processing_date = processing_date;
    }

    public String getStock_num() {
        return Stock_num;
    }

    public void setStock_num(String stock_num) {
        Stock_num = stock_num;
    }

    public Integer getForeign_investors() {
        return Foreign_investors;
    }

    public void setForeign_investors(Integer foreign_investors) {
        Foreign_investors = foreign_investors;
    }

    public Integer getInvestment_trust() {
        return Investment_trust;
    }

    public void setInvestment_trust(Integer investment_trust) {
        Investment_trust = investment_trust;
    }

    public Integer getDealer() {
        return Dealer;
    }

    public void setDealer(Integer dealer) {
        Dealer = dealer;
    }

    public Integer getTotal_buysell() {
        return Total_buysell;
    }

    public void setTotal_buysell(Integer total_buysell) {
        Total_buysell = total_buysell;
    }

    public String getMarket_type() {
        return Market_type;
    }

    public void setMarket_type(String market_type) {
        Market_type = market_type;
    }

}
