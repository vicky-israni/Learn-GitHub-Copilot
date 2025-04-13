describe('Registration Form', () => {
  beforeEach(() => {
    // Visit the registration page before each test
    cy.visit('/register');
  });

  it('should prevent registration with an already registered email', () => {
    // Register a user with a specific email
    cy.get('input[name="name"]').type('Test User');
    cy.get('input[name="email"]').type('test@example.com');
    cy.get('input[name="phone"]').type('1234567890');
    cy.get('input[name="password"]').type('password123');
    cy.get('input[name="profile_picture"]').selectFile('cypress/fixtures/profile.jpg');
    cy.get('form').submit();

    // Ensure the user is redirected to the home page
    cy.url().should('include', '/');
    cy.contains('Welcome, Test User!');

    // Try to register again with the same email
    cy.visit('/register');
    cy.get('input[name="name"]').type('Another User');
    cy.get('input[name="email"]').type('test@example.com');
    cy.get('input[name="phone"]').type('0987654321');
    cy.get('input[name="password"]').type('password456');
    cy.get('input[name="profile_picture"]').selectFile('cypress/fixtures/profile.jpg');
    cy.get('form').submit();

    // Verify the error message is displayed
    cy.contains('User already exists. Please log in.');
  });
});