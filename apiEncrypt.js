const crypto = require("crypto");

const jwtSecret = crypto.randomBytes(20).toString("hex");

console.log("JWT Secret :", jwtSecret);
