package com.example.demo.dao;

import com.example.demo.model.Institutional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface institutionalJPA extends JpaRepository<Institutional,Long> {
    //	spring data	Table 3. Supported keywords inside method names
    	 @Query(value = "SELECT top 10 *  FROM Institutional_investors ", nativeQuery=true)
         List<Institutional> query();
}
