package com.example.demo.archive_jython;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Properties;

import org.python.util.PythonInterpreter;
public class testpythonapi {
    public static void main(String[] args) {
        Properties props = new Properties();
        Properties preprops = System.getProperties();
        PythonInterpreter.initialize(preprops,props,new String[0]);
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("import sys");
        interpreter.exec("print sys.path");
        interpreter.exec("sys.path.append('F:\\python\\Lib\\site-packages')");

        String[] arguments = new String[] {"python", "F:\\MY_STOCK_WEB\\test.py", "huzhiwei", "25"};
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            int re = process.waitFor();
            System.out.println(re);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
