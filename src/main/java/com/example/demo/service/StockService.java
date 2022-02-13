package com.example.demo.service;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

@Service
public class StockService {

    public String getData(@RequestBody Map<String, Object> requestMap) throws IOException {
        System.out.println("查看map:" + requestMap);
        String pythonKey1 = (String) requestMap.get("key1");
        String pythonKey2 = (String) requestMap.get("key2");
        String pythonKey3 = (String) requestMap.get("key3");
        String pythonKey4 = (String) requestMap.get("key4");
        String pythonKey5 = (String) requestMap.get("key5");
        HashMap<String, Map<String, Object>> objectObjectHashMap = new HashMap<>();
        HashMap<String, ArrayList<Object>> objectObjectHashMap2 = new HashMap<>();
        String path = getPath();
        String table = "";
        HashMap<String, String> objectHashMap = new HashMap<>();
        objectHashMap.put("parameter1", pythonKey1);
        objectHashMap.put("parameter2", pythonKey2);
        objectHashMap.put("parameter3", pythonKey3);
        objectHashMap.put("parameter4", pythonKey4);
        objectHashMap.put("parameter5", pythonKey5);

        String[] arguments = new String[]{
                "python",
                path,
                objectHashMap.get("parameter1"),
                objectHashMap.get("parameter2"),
                objectHashMap.get("parameter3"),
                objectHashMap.get("parameter4"),
                objectHashMap.get("parameter5"),
        };
        //C:\Users\JeterPc\Desktop\sideproject\springboot\src\main\resources\python_api\institutional_investors.py
        //C:\Users\JeterPc\Desktop\sideproject\springboot\src\main\resources\python_api\institutional_investors.py
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            InputStreamReader inputStreamReader = new InputStreamReader(process.getInputStream(), Charset.forName("utf-8"));
            BufferedReader in = new BufferedReader(inputStreamReader);
            String line = null;
            while ((line = in.readLine()) != null) {
                table += line;
            }
            in.close();
//            JSONObject jsonData = new JSONObject(table);
//            System.out.println("================以下是處理資料========================");
//            Iterator<String> keys = jsonData.keys();
//            for (Iterator<String> it = keys; it.hasNext(); ) {
//                String key = it.next();
//                JSONObject jsonDataJSONArray = jsonData.getJSONObject(key);
//                Map<String, Object> stringObjectMap = jsonDataJSONArray.toMap();
//                objectObjectHashMap.put(key, stringObjectMap);
//            }
//            Institutional institutional = new Institutional();
//            objectObjectHashMap.forEach(
//                    (k, map) -> {
//                        ArrayList<Object> stringArrayList = new ArrayList<>();
//                        map.forEach((a, value) -> {
//                            stringArrayList.add(value);
//                            objectObjectHashMap2.put(k, stringArrayList);
//                        });
//                    }
//            );
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("最後送出"+table);
//        return objectObjectHashMap2;
        return table;
    }
    public String getInitData() throws IOException {
        System.out.println("--------------開始初始化-----------");
        String path = getInitPath();
        String table = "";

        String[] arguments = new String[]{
                "python",
                path,
                "Stock_Num_name"
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
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.print("最後送出:"+table);
        System.out.println("--------------end-----------");
        return table;
    }
    public String getPath() throws IOException {
        String id = "institutional_investors" + ".py"; //到時候從前端傳進來對應的名子
        String pyClasspathTemplate = "src/main/resources/python_api/%s";
        String pyFolderClasspathPath = String.format(pyClasspathTemplate, id);
        String filePath = new File(pyFolderClasspathPath).getAbsolutePath();
        return filePath;
    }
    public String getInitPath() throws IOException {
        String id = "inital_data" + ".py"; //到時候從前端傳進來對應的名子
        String pyClasspathTemplate = "src/main/resources/python_api/%s";
        String pyFolderClasspathPath = String.format(pyClasspathTemplate, id);
        String filePath = new File(pyFolderClasspathPath).getAbsolutePath();
        return filePath;
    }
}
