package com.example.demo.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.springframework.stereotype.Component;

@Component
@Entity
@Table(name = "movieTheater")
public class movieTheater {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
//	private String username;
//	private String description;

    @Column(columnDefinition = "NVARCHAR(MAX)", nullable = false)
    private String movieComment;

    private String title;
    //	private Blob image;
    private String fileName;
    private String type;
    private String acs;

    public String getMovieComment() {
        return movieComment;
    }

    public void setMovieComment(String movieComment) {
        this.movieComment = movieComment;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }


    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;

        result = prime * result + ((id == null) ? 0 : id.hashCode());

        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        movieTheater other = (movieTheater) obj;

        if (id == null) {
            if (other.id != null)
                return false;
        } else if (!id.equals(other.id))
            return false;

        return true;
    }

    public movieTheater(Long id) {
        super();
        this.id = id;

    }

    public movieTheater(String acs) {

        this.acs = acs;
    }

    public String getAcs() {
        return acs;
    }

    public void setAcs(String acs) {
        this.acs = acs;
    }
}
