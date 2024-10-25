<?php
// Start the session
session_start();

// Database connection details
$servername = "localhost";
$username = "your_db_username"; // Change to your database username
$password = "your_db_password";  // Change to your database password
$dbname = "your_database_name";   // Change to your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data and sanitize it
    $email = htmlspecialchars(trim($_POST['email']));
    $password = htmlspecialchars(trim($_POST['password']));

    // Fetch the user from the database
    $sql = "SELECT * FROM users WHERE email = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();

    if ($user && password_verify($password, $user['password'])) {
        // Login successful
        $_SESSION['user_id'] = $user['id']; // Store user ID in session
        $_SESSION['username'] = $user['username']; // Store username in session
        header("Location: /home"); // Redirect to home page
        exit();
    } else {
        // Login failed
        echo "Invalid email or password."; // Consider logging this for debugging
    }

    $stmt->close();
}

$conn->close();
?>
