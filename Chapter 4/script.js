function validatePhoneNumber(input) {
    input.value = input.value.replace(/\D/g, '').slice(0, 10);
}

function validateForm(event) {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;

    if (!name || !email || !phone || !password) {
        alert('Please fill out all required fields.');
        event.preventDefault();
    }
}

function checkPasswordStrength(password) {
    const strengthIndicator = document.getElementById('password-strength');
    let strength = 'Weak';
    const strongPassword = new RegExp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\\$%\\^&\\*])(?=.{8,})');
    const mediumPassword = new RegExp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})');

    if (strongPassword.test(password)) {
        strength = 'Strong';
    } else if (mediumPassword.test(password)) {
        strength = 'Medium';
    }

    strengthIndicator.textContent = `Password Strength: ${strength}`;
}

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[action="/submit-registration"]');
    form.addEventListener('submit', validateForm);

    const passwordInput = document.getElementById('password');
    passwordInput.addEventListener('input', function() {
        checkPasswordStrength(passwordInput.value);
    });

    const themeToggleButton = document.createElement('button');
    themeToggleButton.textContent = 'Toggle Theme';
    themeToggleButton.className = 'theme-toggle-button';
    themeToggleButton.addEventListener('click', toggleTheme);
    document.body.appendChild(themeToggleButton);
});