package com.example.service;

import com.example.model.User;
import java.util.HashMap;
import java.util.Map;

public class UserService {
    private Map<String, User> userStore = new HashMap<>();

    public void saveUser(User user) {
        userStore.put(user.getUsername(), user);
    }

    public boolean validateUser(String username, String password) {
        User user = userStore.get(username);
        return user != null && user.getPassword().equals(password);
    }
}