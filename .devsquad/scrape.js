const https = require("https");
const targets = [
  "aws-documentation-mcp-server",
  "aws-iac-mcp-server",
  "lambda-tool-mcp-server",
  "aws-serverless-mcp-server",
  "aws-pricing-mcp-server",
  "cloudwatch-mcp-server",
  "cloudwatch-applicationsignals-mcp-server",
  "well-architected-security-mcp-server",
  "dynamodb-mcp-server",
  "aws-dataprocessing-mcp-server",
  "stepfunctions-tool-mcp-server",
  "aws-network-mcp-server",
  "cfn-mcp-server",
];

async function fetchPage(url) {
  return new Promise((resolve) => {
    https.get(url, (resp) => {
      let data = "";
      resp.on("data", (chunk) => (data += chunk));
      resp.on("end", () => resolve(data));
    });
  });
}

(async () => {
  for (const t of targets) {
    const html = await fetchPage("https://awslabs.github.io/mcp/servers/" + t);

    let found = false;

    const textBlocks = html.split("<pre");
    for (let i = 1; i < textBlocks.length; i++) {
      let block = textBlocks[i];
      if (!block.includes("uvx")) continue;
      let innerText = block.split("</pre>")[0].replace(/<[^>]+>/g, "");
      // unescape HTML entities
      innerText = innerText
        .replace(/&quot;/g, '"')
        .replace(/&amp;/g, "&")
        .replace(/&lt;/g, "<")
        .replace(/&gt;/g, ">")
        .replace(/&#x27;/g, "'");
      if (innerText.includes('"command"') && innerText.includes("uvx")) {
        console.log("--- " + t + " ---");
        console.log(innerText.trim());
        found = true;
        break;
      }
    }
    if (!found) {
      console.log("--- " + t + " --- (NOT FOUND)");
    }
  }
})();
