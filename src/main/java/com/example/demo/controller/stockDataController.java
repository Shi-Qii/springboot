package com.example.demo.controller;

import com.example.demo.dao.institutionalJPA;
import com.example.demo.model.institutional;
import com.example.demo.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.*;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
public class stockDataController {

    @Autowired
    institutionalJPA jpa;

    @Autowired
    StockService stockService;

    //    @GetMapping("/api/getStockData")
//    public  List<institutional> getStockData() {
//        List<institutional> jpaAll = jpa.query();
//        System.out.println("getAllCourses"+jpaAll);
//        return jpaAll;
//    }
//
//
    @GetMapping("/api/getStockData")
    public Map<String, Object> getStockData() throws IOException {
        HashMap<String, Object> hashMap = new HashMap<>();
//        先保留原本用jpa 撈資料 ，現在改用 python 返回字串
//        List<institutional> jpaAll = jpa.query();
//        hashMap.put("table",jpaAll);
        String data = stockService.getData();
        hashMap.put("table1", data);
        return hashMap;
    }


}
