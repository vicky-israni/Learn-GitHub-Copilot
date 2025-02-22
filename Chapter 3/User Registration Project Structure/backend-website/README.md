# Backend Website

This project is a simple backend application that handles user registrations and logins without using a database. It is built using Java and follows a layered architecture.

## Project Structure

```
backend-website
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── example
│   │   │           ├── controller
│   │   │           │   └── UserController.java
│   │   │           ├── model
│   │   │           │   └── User.java
│   │   │           ├── service
│   │   │           │   └── UserService.java
│   │   │           └── util
│   │   │               └── PasswordUtil.java
│   │   └── resources
│   │       └── application.properties
│   └── test
│       └── java
│           └── com
│               └── example
│                   └── UserControllerTest.java
├── pom.xml
└── README.md
```

## Features

- User registration
- User login
- Password hashing and validation

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd backend-website
   ```

3. Build the project using Maven:
   ```
   mvn clean install
   ```

4. Run the application:
   ```
   mvn spring-boot:run
   ```

## Usage

- To register a user, send a POST request to `/register` with a JSON body containing `username`, `password`, and `email`.
- To log in a user, send a POST request to `/login` with a JSON body containing `username` and `password`.

## Testing

Unit tests for the UserController can be found in `src/test/java/com/example/UserControllerTest.java`. You can run the tests using:
```
mvn test
```

## Dependencies

This project uses the following dependencies:
- Spring Boot
- Lombok (for reducing boilerplate code)

## License

This project is licensed under the MIT License.