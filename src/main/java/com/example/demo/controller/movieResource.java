package com.example.demo.controller;

import java.io.IOException;
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

import javax.servlet.ServletContext;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.example.demo.dao.MovieJPA;
import com.example.demo.model.movieTheater;

@CrossOrigin(origins = {"http://localhost:8080"})
@RestController
//@RequestMapping("/api/autha")
//@PreAuthorize("hasRole('ADMIN')")
public class movieResource {

    @Autowired
    MovieJPA jpa;
    @Autowired
    movieTheater MovieTheater;
//	@Autowired
//	ServletContext context;


//	@Autowired
//	private CoursesHardcodedService courseManagementService;

    @GetMapping("/instructors/{username}/courses")
    public List<movieTheater> getAllCourses(@PathVariable String username) {
        System.out.println("getAllCourses");
        return jpa.findAll();
    }

    //	selectType
    @GetMapping("/instructors/{username}/{selectType}")
    public List<movieTheater> getlovetype(@PathVariable String username, @PathVariable String selectType) {
        return jpa.queryBytype(selectType);
    }

    @GetMapping("/instructors/{username}/readcomment")
    public List<movieTheater> getAllComment(@PathVariable String username) {
        System.out.println("getAllComment");
        return jpa.findAll(); //

    }

    @GetMapping("/instructors/{username}/readcomment/{id}")
//	readComment
    public Optional<movieTheater> readComment(@PathVariable String username, @PathVariable long id) {
        System.out.println("test");
        return jpa.findById(id);
    }

    @DeleteMapping("/instructors/{username}/movie/{id}")
//	@PreAuthorize("hasRole('ADMIN')")
    public List<movieTheater> deleteCourse(@PathVariable String username, @PathVariable long id) {
        jpa.deleteById(id);

        System.out.println("dele");
        return jpa.findAll();// TODO: 2021/4/6
    }

    public static void main(String[] args) {

    }

    @PutMapping("/instructors/{username}/courses/{id}")
    public ResponseEntity<movieTheater> updateCourse(@PathVariable String username, @PathVariable long id,
                                                     @RequestBody movieTheater movieTheater) {
        movieTheater courseUpdated = jpa.save(movieTheater);
        System.out.println("====>updateCourse");
        return new ResponseEntity<movieTheater>(courseUpdated, HttpStatus.OK);
    }

    @PostMapping("/instructors/{username}/courses")
    public ResponseEntity<movieTheater> createCourse(@PathVariable String username, @RequestBody movieTheater movieTheater) {

        movieTheater createdCourse = jpa.save(movieTheater);
        URI uri = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(createdCourse.getId())
                .toUri();

        System.out.println("create");
        return ResponseEntity.created(uri).build();

    }

    //上傳圖片
//C:\Users\User\Desktop\Spring_Vue\src\main\resources\static
    private static final String UPLOAD_PATH = "C:\\Users\\User\\Desktop\\Spring_Vue\\src\\main\\resources\\static\\";

    @PostMapping("/upload")
    public String singleFileUpload(@RequestParam("file") MultipartFile file, HttpServletRequest request) {
        try {
            byte[] bytes = file.getBytes();
            String imageFileName = file.getOriginalFilename();
            Path path = Paths.get(UPLOAD_PATH + imageFileName);
            Files.write(path, bytes);
            return imageFileName;
        } catch (IOException e) {
            e.printStackTrace();
        }

        return "";
    }

    //讀取圖片1
    @GetMapping("/getImage/{name}")

    public void getImage(HttpServletResponse response, @PathVariable("name") String name) throws IOException {

        response.setContentType("image/jpeg;charset=utf-8");
        response.setHeader("Content-Disposition", "inline; filename=girls.png");
        ServletOutputStream outputStream = response.getOutputStream();
        System.out.println("static" + name);
        outputStream.write(Files.readAllBytes(Paths.get(UPLOAD_PATH).resolve(name)));
        outputStream.flush();
        outputStream.close();
    }
}
