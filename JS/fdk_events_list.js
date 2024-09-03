const fs = require("fs");
const json2csv = require("json2csv").parse;

// Read data from file
const rawData = fs.readFileSync(
  "/Users/kmuruganandham/Documents/GitHub/freshapps_sdk/addon/events/eventsNew.json"
);
const data = JSON.parse(rawData);

const result = {};

for (const key in data) {
  if (data.hasOwnProperty(key)) {
    result[key] = data[key]
      .filter((obj) => obj.event_type === "product_event")
      .map((obj) => obj.name);
  }
}

console.log(result);

// Convert result to CSV format
const csvData = [];
for (const key in result) {
  if (result.hasOwnProperty(key)) {
    const events = result[key];
    events.forEach((event) => {
      csvData.push({ key, external_event_name: event });
    });
  }
}

// Convert JSON to CSV
const csv = json2csv(csvData, { fields: ["key", "external_event_name"] });

// Write CSV to file
fs.writeFileSync("output.csv", csv);

console.log("CSV file generated successfully.");
