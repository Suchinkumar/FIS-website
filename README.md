# FIS-website
This project is a foundational demonstration of key principles in information security, focusing on secure user authentication and registration within a web application context. The project leverages modern web technologies and practices to showcase essential security measures

#### Key Features:

1. **Secure Web Application**:
    - Built with Flask, a lightweight Python web framework, to create a robust web application.
    - Implements CORS (Cross-Origin Resource Sharing) to ensure secure interaction between different domains.

2. **Database Integration**:
    - Utilizes MySQL for data storage, demonstrating how to securely interact with a relational database.
    - Incorporates the `mysql.connector` and `flask_mysqldb` modules for database operations.

3. **User Authentication**:
    - Provides secure user login and registration functionalities.
    - Uses parameterized queries to prevent SQL injection attacks.
    - Enforces password policies to enhance security.

4. **IP Banning**:
    - Implements IP banning using the `flask_ipban` module to mitigate brute force attacks.
    - Automatically bans IP addresses after a configurable number of failed login attempts.

#### Project Structure:

- **main.py**:
    - The core of the web application.
    - Configures the Flask app, sets up CORS and MySQL, and defines the routes for login and registration.
    - Implements security measures such as IP banning and password policy enforcement.

- **sql.py**:
    - Contains database connection setup and query execution.
    - Demonstrates how to securely handle user input to prevent SQL injection.

- **tempCodeRunnerFile.py**:
    - Includes additional MySQLdb functionalities.

#### How to Run:

1. **Setup Environment**:
    - Install required Python packages:
      ```sh
      pip install flask flask-mysqldb flask-cors flask-ipban mysql-connector-python
      ```
    - Ensure MySQL server is running and accessible with the credentials specified in `main.py`.

2. **Database Configuration**:
    - Create a MySQL database named `fis`.
    - Create necessary tables (`users`, `password`, `level`) to store user data.

3. **Run the Application**:
    - Start the Flask application:
      ```sh
      python main.py
      ```
    - Access the application via `http://localhost:5000`.

#### Security Considerations:

- **Input Validation**:
    - Ensures user inputs are validated and sanitized to prevent common web vulnerabilities.
- **Password Handling**:
    - Enforces a policy where passwords cannot contain spaces.
    - Utilizes secure hashing methods for storing passwords (recommendation for future improvements).
- **Error Handling**:
    - Implements error handling to manage and log application errors without exposing sensitive information.
