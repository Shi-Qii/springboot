package com.example.demo;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

@Aspect
@Component
public class aop {

//	@Pointcut("execution (public * com.example.demo.controller.*.deleteCourse(..)) ")
//	public void gologin() {
//
//	}

//	@After(value = "gologin()")
//	@After("execution (public * com.example.demo.controller.*.deleteCourse(..)) ")
//	public void test() {
//		System.out.println("After");
//	}
//	@Before("execution (public * com.example.demo.security.jwt.*.commence(..)) ")
//	public void gologin(JoinPoint joinPoint) {
//		String methodName = joinPoint.getSignature().getName();
//		System.out.println("Before"+methodName);
//	}


}
