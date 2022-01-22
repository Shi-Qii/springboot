package com.example.demo.jython;

import org.python.util.PythonInterpreter;

import java.util.Properties;
public class testpython {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("python.home", "F:\\python");
        props.put("python.console.encoding", "UTF-8");
        props.put("python.security.respectJavaAccessibility", "false");
        props.put("python.import.site", "false");
        Properties preprops = System.getProperties();
        PythonInterpreter.initialize(preprops,props,new String[0]);
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("import sys");
        interpreter.exec("sys.path.append('F:\\python\\Lib\\site-packages')");
        interpreter.exec("sys.path.append('F:\\python\\Lib\\site-packages\\urllib3')");
        interpreter.exec("sys.path.append('F:\\python\\Lib\\site-packages\\requests')");
        interpreter.exec("sys.path.append('F:/MY_STOCK_WEB/')");
       // interpreter.exec("sys.path.append('F:\\python\\Lib\\urllib')");
        interpreter.exec("print sys.path");
        //interpreter.exec("pip install requests");
        //interpreter.exec("import requests");

        interpreter.execfile("F:\\MY_STOCK_WEB\\test.py");
//        interpreter.exec("sys.path.append('C:/Users/JeterPc/.m2/repository/org/python/jython-standalone/2.7.0/Lib')");
//         interpreter.exec("sys.path.append('C:\\Users\\JeterPc\\Desktop\\Medium-master\\code\\path to the Lib folder\\Lib\\site-packages\\requests')");
//        interpreter.exec("sys.path.append('C:/Users/JeterPc/Desktop/Medium-master/code/src/helloPython/demo3.py')");
//        interpreter.exec("print sys.path");
//        interpreter.exec("import time");
//        interpreter.exec("import requests");
//        interpreter.exec("import urllib3");
//        interpreter.exec("import logging");
//        interpreter.exec("days=('mod','Tue','Wed','Thu','Fri','Sat','Sun'); ");
//        interpreter.exec("print days[1];");
//        interpreter.exec("print 'created by tengxing on 2017.3!'");











    }
}
