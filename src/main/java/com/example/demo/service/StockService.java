package com.example.demo.service;

import com.example.demo.model.Institutional;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

@Service
public class StockService {

//    @Autowired
//    Institutional institutional;


    public Map<String, ArrayList<Object>> getData(@RequestBody Map<String, Object> requestMap) throws IOException {
        System.out.println("查看map:" + requestMap);
        String pythonKey = (String) requestMap.get("key");
        HashMap<String, Map<String, Object>> objectObjectHashMap = new HashMap<>();
        HashMap<String, ArrayList<Object>> objectObjectHashMap2 = new HashMap<>();
        String path = getPath();
        String table = "";
        HashMap<String, String> objectHashMap = new HashMap<>();
        objectHashMap.put("parameter1", pythonKey);
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
            JSONObject jsonData = new JSONObject(table);
            System.out.println("================以下是處理資料========================");
            Iterator<String> keys = jsonData.keys();
            for (Iterator<String> it = keys; it.hasNext(); ) {
                String key = it.next();
                JSONObject jsonDataJSONArray = jsonData.getJSONObject(key);
                Map<String, Object> stringObjectMap = jsonDataJSONArray.toMap();
                objectObjectHashMap.put(key, stringObjectMap);
            }
            Institutional institutional = new Institutional();
            objectObjectHashMap.forEach(
                    (k, map) -> {
                        ArrayList<Object> stringArrayList = new ArrayList<>();
                        map.forEach((a, value) -> {
                            stringArrayList.add(value);
                            objectObjectHashMap2.put(k, stringArrayList);
                        });
                    }
            );
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(objectObjectHashMap2);
        return objectObjectHashMap2;
    }

    public String getPath() throws IOException {
        String id = "institutional_investors" + ".py"; //到時候從前端傳進來對應的名子
        String pyClasspathTemplate = "src/main/resources/python_api/%s";
        String pyFolderClasspathPath = String.format(pyClasspathTemplate, id);
        String filePath = new File(pyFolderClasspathPath).getAbsolutePath();
        return filePath;
    }
}
