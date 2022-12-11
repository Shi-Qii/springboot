package com.example.demo.controller;

import com.example.demo.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.Map;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
public class stockDataController {

    @Autowired
    StockService stockService;

    @PostMapping("/api/getStockData")
    public String getStockData(@RequestBody Map<String, Object> map) throws IOException {

        String data = stockService.getData((Map<String, Object>) map.get("key"));
        return data;
    }
    @GetMapping("/api/getAppVueInitData")
    public String getStockData() throws IOException {
        String data = stockService.getInitData();
        return data;
    }
    @GetMapping("/api/getIndustrySectNameAppVueInitData")
    public String getIndustrySectNameInitData() throws IOException {
        String data = stockService.getIndustrySectNameInitData();
        return data;
    }

}
