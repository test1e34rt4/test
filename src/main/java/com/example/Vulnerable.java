package com.example;

import javax.servlet.http.HttpServletRequest;
import java.io.*;
import java.sql.*;

public class Vulnerable {

    // 🔥 SQL Injection
    public void getUser(HttpServletRequest request) throws SQLException {
        String userId = request.getParameter("id");
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password");
        Statement stmt = con.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = '" + userId + "'"); // ⚠️ SQL Injection
    }

    // 🔥 Path Traversal
    public void readFile(HttpServletRequest request) throws IOException {
        String filename = request.getParameter("file");
        BufferedReader reader = new BufferedReader(new FileReader("/data/" + filename)); // ⚠️ Path Traversal
    }

    // 🔥 Hardcoded secret
    private static final String SECRET = "ghp_fake_123456789";

    // 🔥 Command injection
    public void runCommand(HttpServletRequest request) throws IOException {
        String input = request.getParameter("cmd");
        Runtime.getRuntime().exec("sh -c " + input); // ⚠️ Command Injection
    }
}
