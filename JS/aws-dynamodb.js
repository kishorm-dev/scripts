const AWS = require("aws-sdk");

// Set the region
AWS.config.update({
  accessKeyId: "TestData",
  secretAccessKey: "TestData",
  region: "localhost",
  endpoint: "http://localhost:4567"
});

// Create DynamoDB service object
const dynamodb = new AWS.DynamoDB();
const param = {
  TableName: "freshdesk-dev",
  KeySchema: [
    { AttributeName: "fa_partition_key", KeyType: "HASH" },
    { AttributeName: "fa_sort_key", KeyType: "RANGE" }
  ],
  AttributeDefinitions: [
    { AttributeName: "fa_partition_key", AttributeType: "S" },
    { AttributeName: "fa_sort_key", AttributeType: "S" }
  ],
  ProvisionedThroughput: {
    ReadCapacityUnits: 10,
    WriteCapacityUnits: 10
  }
};

// dynamodb.createTable(param, function (error) {
//   if (error) {
//     return console.error(error);
//   }
// });

// Define the parameters for the getItem operation
const params = {
  TableName: "freshdesk-dev",
  Key: {
    fa_partition_key: { S: "1:1:1" },
    fa_sort_key: { S: "testAppend" }
  },
  ReturnConsumedCapacity: 'TOTAL'
};

// Retrieve the item from DynamoDB
dynamodb.getItem(params, function (err, data) {
  if (err) {
    console.error(
      "Unable to read item. Error JSON:",
      JSON.stringify(err, null, 2)
    );
  } else {
    console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
    // Calculate the size of the item
    const serializedItem = JSON.stringify(data.Item);
    const itemSizeInBytes = Buffer.byteLength(serializedItem, 'utf8');
    console.log(`Item size: ${itemSizeInBytes} bytes`);
  }
});
