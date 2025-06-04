-- Create a table for users with name, email, and hashed password
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
);


-- Create a table to store login sessions linked to users
CREATE TABLE user_sessions (
    session_id UUID PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    logout_time TIMESTAMP,
    ip_address VARCHAR(45)
);

-- Create a table for user roles
CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    role VARCHAR(50) NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add a role reference to the users table
ALTER TABLE users
ADD COLUMN role_id INTEGER REFERENCES user_roles(id);


