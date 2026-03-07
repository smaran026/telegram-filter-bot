const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

// 🔴 PUT YOUR MAKE WEBHOOK URL HERE
const MAKE_WEBHOOK = "https://hook.make.com/YOUR_WEBHOOK_ID";

app.post("/webhook", async (req, res) => {

  const message = req.body.message;

  // Ignore non-messages
  if (!message || !message.text) {
    return res.sendStatus(200);
  }

  const text = message.text;

  // Only allow commands starting with /
  if (!text.startsWith("/")) {
    return res.sendStatus(200);
  }

  // Respond to Telegram immediately
  res.sendStatus(200);

  try {
    await axios.post(MAKE_WEBHOOK, req.body);
    console.log("Command forwarded to Make:", text);
  } catch (err) {
    console.log("Error sending to Make:", err.message);
  }

});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("Bot filter running on port", PORT);
});
