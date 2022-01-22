package com.example.demo.jython;

import jnr.posix.WString;
import org.python.core.PyFunction;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.charset.Charset;

public class test_python {
    public static void main(String[] args) {
        String par1="Listed_Foreign_Buy_Day";
        String par2="上市";
        String par3="Buy";
        String par4="Foreign_investors";
        String par5= "20";
        String[] arguments = new String[] {"python", "F:\\MY_STOCK_WEB\\springboot\\src\\main\\resources\\python_api\\institutional_investors.py", par1,par2,par3,par4,par5};
        String table = "";
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(),"utf-8"));
            String line = null;
            while ((line = in.readLine()) != null) {
                table += line;
                System.out.println(table);
            }
            in.close();
            //int re = process.waitFor();
            OutputStream re = process.getOutputStream();
            //System.out.println(re);
            System.out.println("----------");
            System.out.println(table);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
