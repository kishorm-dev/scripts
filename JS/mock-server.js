const express = require("express");
const app = express();

// Endpoint that intentionally delays its response
app.get("/delayed", (req, res) => {
  // Get the timeout value from query parameters, defaulting to 5000 milliseconds if not provided
  const timeout = req.query.timeout ? parseInt(req.query.timeout) : 25000;
  console.log(timeout);
  setTimeout(() => {
    res.send("Response after delay");
  }, timeout);
});

const server = app.listen(3000, () => {
  console.log("Mock server running on port 3000");
});
