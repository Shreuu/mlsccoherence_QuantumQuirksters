document.getElementById("login-form").addEventListener("submit", function(event) {
  event.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Retrieve username and password from local storage
  const savedUsername = localStorage.getItem("username");
  const savedPassword = localStorage.getItem("password");

  // Check if entered credentials match saved credentials
  if (username === savedUsername && password === savedPassword) {
      // Redirect to dashboard page upon successful login
      window.location.href = "dashboard.html";
  } else {
      // Display an alert for invalid credentials
      alert("Invalid username or password. Please try again.");
  }
});
