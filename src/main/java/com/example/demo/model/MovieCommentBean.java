package com.example.demo.model;

import java.io.Serializable;
import java.sql.Blob;
import java.util.Map;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.persistence.Transient;

import org.springframework.web.multipart.MultipartFile;

@Entity
@Table(name = "MovieComment")
public class MovieCommentBean implements Serializable {
    private static final long serialVersionUID = 8828979055742280923L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
//	private Integer commentId;
    private Long id;
    private String title;
    private String author;

    @Column(columnDefinition = "NVARCHAR(MAX)", nullable = false)
    private String comment;

    @Transient
    private Integer companyId;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "FK_CompanyBean_Id")
    private CompanyBean companyBean;
    private Blob image;
    private String fileName;
    @Transient
    MultipartFile Image;
    private String type;
    private Integer frequency;

    public MovieCommentBean(String title, String author, String comment, CompanyBean companyBean,
                            Integer companyId, String type, Integer frequency) {
//		this.commentId = commentId;
        this.title = title;
        this.author = author;
        this.comment = comment;
        this.companyBean = companyBean;
        this.companyId = companyId;
        this.type = type;
        this.frequency = frequency;
    }

    public MovieCommentBean() {
    }

//	public Integer getCommentId() {
//		return commentId;
//	}
//
//	public void setCommentId(Integer commentId) {
//		this.commentId = commentId;
//	}

    public CompanyBean getCompanyBean() {
        return companyBean;
    }

    public void setCompanyBean(CompanyBean companyBean) {
        this.companyBean = companyBean;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public Integer getCompanyId() {
        return companyId;
    }

    public void setCompanyId(Integer companyId) {
        this.companyId = companyId;
    }

    @Override
    public String toString() {
        return "MovieCommentBean [ " + "title=" + title + ", author=" + author
                + " comment=" + comment + ", companyId=" + companyId + ", companyBean=" + companyBean
                + ", Image=" + Image + "]";
    }

    public Blob getImage() {
        return image;
    }

    public void setImage(Blob image) {
        this.image = image;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public MultipartFile getMovieImage() {
        return Image;
    }

    public void setMovieImage(MultipartFile movieImage) {
        this.Image = movieImage;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Integer getFrequency() {
        return frequency;
    }

    public void setFrequency(Integer frequency) {
        this.frequency = frequency;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

}
