package com.example.demo.jython;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
public class runtime {
    public static void main(String[] args) {
        System.out.println("run------------");
        Process process = null;
        try {
            process = Runtime.getRuntime().exec("python F:\\MY_STOCK_WEB\\test2.py");
            process.waitFor();
            int i = process.exitValue();
            // 0成功
            System.out.println(i);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
