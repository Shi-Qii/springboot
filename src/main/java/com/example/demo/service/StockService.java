package com.example.demo.service;

import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.HashMap;

@Service
public class StockService {


    public String getData() throws IOException {
        String path = getPath();
        String table = "";
        HashMap<String, String> objectHashMap = new HashMap<>();
        objectHashMap.put("parameter1", "Ind_Institutional_Investors_Day");
        objectHashMap.put("parameter2", "1110");
        objectHashMap.put("parameter3", "10");
        objectHashMap.put("parameter4", "Foreign_investors");
        objectHashMap.put("parameter5", "20");

        String[] arguments = new String[]{
                "python",
                path,
                objectHashMap.get("parameter1"),
                objectHashMap.get("parameter2"),
                objectHashMap.get("parameter3"),
                objectHashMap.get("parameter4"),
                objectHashMap.get("parameter5"),
        };

        try {
            Process process = Runtime.getRuntime().exec(arguments);
            InputStreamReader inputStreamReader = new InputStreamReader(process.getInputStream(), Charset.forName("utf-8"));
            BufferedReader in = new BufferedReader(inputStreamReader);
            String line = null;
            while ((line = in.readLine()) != null) {
                table += line;
            }
            in.close();
            System.out.println(table);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return table;
    }

    public String getPath() throws IOException {
        String id = "institutional_investors" + ".py"; //到時候從前端傳進來對應的名子
        String pyClasspathTemplate = "src/main/resources/python_api/%s";
        String pyFolderClasspathPath = String.format(pyClasspathTemplate, id);
        String filePath = new File(pyFolderClasspathPath).getAbsolutePath();
        return filePath;
    }
}
