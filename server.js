const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

const MAKE_WEBHOOK = "https://hook.eu1.make.com/c6csfcesv8t8efckjke6wkyw3fayzri9";

app.post("/webhook", (req, res) => {

  // respond immediately to Telegram
  res.sendStatus(200);

  const message = req.body.message;

  if (!message || !message.text) {
    return;
  }

  if (!message.text.startsWith("/")) {
    return;
  }

  console.log("Command received:", message.text);

  axios.post(MAKE_WEBHOOK, req.body)
    .then(() => console.log("Sent to Make"))
    .catch(err => console.log("Make error:", err.message));

});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("Bot filter running");
});
