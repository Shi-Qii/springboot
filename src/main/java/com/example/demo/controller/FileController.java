package com.example.demo.controller;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.util.ResourceUtils;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
//@CrossOrigin(origins = { "http://localhost:8080" })
//@RestController
//@RequestMapping("file")
//public class FileController {
//
//	 @PostMapping("upload")
//	    public String upload(@RequestParam("file")MultipartFile mf) throws IOException {
//
//	        /**
//	         * 獲取專案絕對路徑
//	         * 最終檔案上傳是需要絕對路徑的
//	         * 相當於給要上傳的位置定個座標
//	         * classpath:就可以去獲得resources的目錄
//	         * 具體classpath:獲得resources的原因就得自己去探索了，本文主要是講檔案上傳
//	         * 這裡不去除first的話這個路徑開頭會有一個/，雖然沒有什麼影響
//	         */
//	        String absPath = ResourceUtils.getURL("classpath:").getPath().replaceFirst("/","") + "static/files";
//	        /**
//	         * 建立檔案目錄
//	         * 根據自己的需求
//	         * 在這我就以當前時間建立
//	         */
//	        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd-HH-mm");
//	        //檔案的目錄應該為絕對路徑+目錄名
//	        String dirPath = absPath+"/"+sdf.format(new Date());
//	        //通過這個路徑建立目錄
//	        File dir = new File(dirPath);
//	        //如果不存在就建立該目錄
//	        if(!dir.exists()){
//	            dir.mkdirs();
//	        }
//	        /**
//	         * 建立檔案
//	         * 檔名字就根據自己的需求而定
//	         * 我這裡為了方便，就叫cutezha吧
//	         */
//	        //先獲取檔案本身的名字
//	        String oldName = mf.getOriginalFilename();
//	        //使用FileNameUtils獲取副檔名，這裡獲取的沒有.所以手動加上
//	        String extension = "."+FilenameUtils.getExtension(oldName);
//	        String fileName = "cutezha"+extension;
//	        //上傳檔案
//	        mf.transferTo(new File(dir,fileName));
//	        /**
//	         * 將資料返回給前端，我這裡就直接將路徑返回了
//	         * 注意這裡用dirPath才是斜槓，如果使用dir則是反斜槓
//	         */
//	        return dirPath+"/"+fileName;
//	    }
//
//}
