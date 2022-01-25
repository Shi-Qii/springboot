package com.example.demo.controller;

import com.example.demo.dao.institutionalJPA;
import com.example.demo.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.*;
import java.util.ArrayList;
import java.util.Map;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
public class stockDataController {

    @Autowired
    institutionalJPA jpa;

    @Autowired
    StockService stockService;
//        先保留原本用jpa 撈資料 ，現在改用 python 返回字串
//    @GetMapping("/api/getStockData")
//    public List<institutional> getStockData() {
//        List<institutional> jpaAll = jpa.query();
//        System.out.println("getAllCourses" + jpaAll);
//        return jpaAll;
//    }



    @PostMapping("/api/getStockData")
    public String getStockData(@RequestBody Map<String,Object> map) throws IOException {
        String data = stockService.getData(map);
        return data;
    }


}
