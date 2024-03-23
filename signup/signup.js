document.getElementById("signup-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const newUsername = document.getElementById("new-username").value;
    const newPassword = document.getElementById("new-password").value;
  
    // Store username and password in local storage
    localStorage.setItem("username", newUsername);
    localStorage.setItem("password", newPassword);
  
    alert("Account created successfully. You can now login.");
    window.location.href = "login.html"; // Redirect to login page after signup
  });
  