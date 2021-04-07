package com.example.demo.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.model.MovieCommentBean;


public interface CommentJPA extends JpaRepository<MovieCommentBean, Long>{

}
