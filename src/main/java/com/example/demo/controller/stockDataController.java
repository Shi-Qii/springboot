package com.example.demo.controller;

import com.example.demo.dao.institutionalJPA;
import com.example.demo.model.institutional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
public class stockDataController {

    @Autowired
    institutionalJPA jpa;



    @GetMapping("/api/getStockData")
    public  List<institutional> getStockData() {
        List<institutional> jpaAll = jpa.query();
        System.out.println("getAllCourses"+jpaAll);
        return jpaAll;
    }

}
