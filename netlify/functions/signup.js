// netlify/functions/signup.js

exports.handler = async (event, context) => {
    const { name, email, password } = JSON.parse(event.body);
  
    // Placeholder for actual sign-up logic
    // You can integrate with a database or an authentication service here
    if (email && password && name) {
      return {
        statusCode: 200,
        body: JSON.stringify({ message: "Sign up successful!" }),
      };
    } else {
      return {
        statusCode: 400,
        body: JSON.stringify({ message: "Invalid data submitted." }),
      };
    }
  };
  