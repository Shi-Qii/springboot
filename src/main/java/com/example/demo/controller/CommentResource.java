package com.example.demo.controller;

import java.net.URI;
import java.util.List;
import java.util.Optional;

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
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.example.demo.dao.CommentJPA;
import com.example.demo.model.MovieCommentBean;

@CrossOrigin(origins = { "http://localhost:8080" })
@RestController
//@PreAuthorize("hasRole('ADMIN')")
public class CommentResource {

	@Autowired
	CommentJPA commentJPA;

//	@Autowiredaaaaaasss
//	private CoursesHardcodedService courseManagementService;

	@GetMapping("/instructors/{username}/comment")
	public List<MovieCommentBean> getAllComments(@PathVariable String username) {
		return commentJPA.findAll();
	}

	@DeleteMapping("/instructors/{username}/comment/{id}")
//	@PreAuthorize("hasRole('ADMIN')")
	public List<MovieCommentBean> deleteComment(@PathVariable String username, @PathVariable long id) {
		commentJPA.deleteById(id);
		System.out.println("dele");
		return commentJPA.findAll();
	}

	@GetMapping("/instructors/{username}/comment/{id}")
	public Optional<MovieCommentBean> getComment(@PathVariable String username, @PathVariable long id) {
		return commentJPA.findById(id);
	}

	@PutMapping("/instructors/{username}/comment/{id}")
	public ResponseEntity<MovieCommentBean> updateComment(@PathVariable String username, @PathVariable long id,
			@RequestBody MovieCommentBean movieCommentBean) {
		MovieCommentBean commentUpdated = commentJPA.save(movieCommentBean);
		return new ResponseEntity<MovieCommentBean>(commentUpdated, HttpStatus.OK);
	}

	@PostMapping("/instructors/{username}/comment")
	public ResponseEntity<Void> createComment(@PathVariable String username,
			@RequestBody MovieCommentBean movieCommentBean) {

		MovieCommentBean createdComment = commentJPA.save(movieCommentBean);
		URI uri = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(createdComment.getId())
				.toUri();
		return ResponseEntity.created(uri).build();
	}

}
