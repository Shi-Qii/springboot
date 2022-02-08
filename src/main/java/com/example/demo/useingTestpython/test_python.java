package com.example.demo.useingTestpython;

import java.io.*;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.charset.Charset;

public class test_python {



    public static void main(String[] args) throws IOException {
        System.out.println("建立develop");
        String par1="OTC_Institutional_Investors_Day";
        String par2="2";
        String par3="2330";
        String par4="Foreign_investors";
        String par5= "20";

        String id = "twse_otc_index"+".py"; //到時候從前端傳進來對應的名子

        String pyClasspathTemplate = "src/main/resources/python_api/%s";
        String pyFolderClasspathPath = String.format(pyClasspathTemplate, id);
        String filePath = new File(pyFolderClasspathPath).getAbsolutePath();

        String[] arguments = new String[] {"python", filePath, par1,par2,par3,par4,par5};
        String table = "";
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            InputStreamReader inputStreamReader = new InputStreamReader(process.getInputStream(), Charset.forName("utf-8"));
            String readerEncoding = inputStreamReader.getEncoding();
            BufferedReader in = new BufferedReader(inputStreamReader);
            String line = null;
            while ((line = in.readLine()) != null) {

                table += line;
             //   System.out.println(table);
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
