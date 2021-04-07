//package com.example.demo;
//
//import java.net.URI;
//import java.util.List;
//import java.util.Optional;
//
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.http.HttpStatus;
//import org.springframework.http.ResponseEntity;
//import org.springframework.web.bind.annotation.CrossOrigin;
//import org.springframework.web.bind.annotation.DeleteMapping;
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.PathVariable;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.PutMapping;
//import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RestController;
//import org.springframework.web.servlet.support.ServletUriComponentsBuilder;
//
//@CrossOrigin(origins = { "http://localhost:8080" })
////http://localhost:8081 要對照vue serve的port位 http://localhost:8081
//@RestController
//public class CourseResource {
//
//	@Autowired
//	CourseRepositorty courserepository;
//
//	// 查詢全部
//	@GetMapping("/instructors/{username}/courses")
//	public List<Course> getAllCourses() {
//		return courserepository.findAll();
//	}
//
//	// 依據id查詢
//	@GetMapping("/instructors/{username}/courses/{id}")
//	public Optional<Course> getCourse(@PathVariable long id) {
//		return courserepository.findById(id);
//	}
//
//	// 刪除單筆
//	@DeleteMapping("/instructors/{username}/courses/{id}")
//	public List<Course> del(@PathVariable("id") long id) throws Exception {
//		courserepository.deleteById(id);
//		return courserepository.findAll();
//	}
//	//修改
//	@PutMapping("/instructors/{username}/courses/{id}")
//	public ResponseEntity<Course> updateCourse(@PathVariable long id,
//			@RequestBody Course course) {
//		Course courseUpdated = courserepository.save(course);
//		return new ResponseEntity<Course>(courseUpdated, HttpStatus.OK);
//	}
//	//新增依照ID新增
//	@PostMapping("/instructors/{username}/courses")
//	public ResponseEntity<Void> createCourse(@RequestBody Course course) {
//		Course createdCourse = courserepository.save(course);
//		URI uri = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(createdCourse.getId())
//				.toUri();
//		return ResponseEntity.created(uri).build();
//	}
//
//}