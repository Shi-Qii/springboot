package com.example.demo.model;

import java.io.Serializable;
import java.util.LinkedHashSet;
import java.util.Set;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
// 本類別封裝單筆出版社資料
@Entity
@Table(name="MoiveCompany")
public class CompanyBean implements Serializable {
	private static final long serialVersionUID = 1L;
	private Integer id ;
	private String  name;
	private String  address;
	private String  type;
	private Set<MovieCommentBean> books = new LinkedHashSet<>();
	

	
	public CompanyBean(Integer id, String name, String address, String url, String type) {
		this.id = id;
		this.name = name;
		this.address = address;
		this.type = type;
	}
	public CompanyBean() {
	}
	
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}
	@OneToMany(mappedBy="companyBean")
	public Set<MovieCommentBean> getBooks() {
		return books;
	}
	public void setBooks(Set<MovieCommentBean> books) {
		this.books = books;
	}
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}	
	
}