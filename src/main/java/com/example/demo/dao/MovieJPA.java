package com.example.demo.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.model.movieTheater;

public interface MovieJPA extends JpaRepository<movieTheater, Long> {

//	 @Query(value = "SELECT *  FROM course WHERE type = 'love' ", nativeQuery=true)
//	spring data	Table 3. Supported keywords inside method names
	List<movieTheater> queryBytype(String type);

}
