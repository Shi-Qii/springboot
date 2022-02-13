package com.example.demo.controller;

import com.example.demo.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Map;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
public class AppVueInitDataController {



    @Autowired
    StockService stockService;

    @GetMapping("/api/getAppVueInitData")
    public String getStockData() throws IOException {
        String data = stockService.getInitData();
        return data;
    }


}
