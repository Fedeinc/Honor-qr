exports.handler = async function(event, context) {
    const { email, password } = JSON.parse(event.body);

    // Placeholder authentication logic
    if (email === "user@example.com" && password === "securepassword") {
        return {
            statusCode: 200,
            body: JSON.stringify({ message: "Login successful!" }),
        };
    } else {
        return {
            statusCode: 401,
            body: JSON.stringify({ message: "Invalid credentials!" }),
        };
    }
};
