
const request = require("request-promise");


async function testRequestPromise() {
    try {
        const response = await request.get("https://cognito-idp.us-east-1.amazonaws.com/us-east-1_c9G2exjHf/.well-known/jwks.json");
        console.log("Response received!", response);
    } catch (error) {
        console.error("Error: ", error);
    }
}


testRequestPromise();