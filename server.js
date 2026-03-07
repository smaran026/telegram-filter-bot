const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

const MAKE_WEBHOOK = "https://hook.eu1.make.com/c6csfcesv8t8efckjke6wkyw3fayzri9";

app.post("/webhook", async (req, res) => {
  try {

    const message = req.body.message;

    if (!message || !message.text) {
      return res.sendStatus(200);
    }

    const text = message.text;

    // Only allow commands
    if (!text.startsWith("/")) {
      return res.sendStatus(200);
    }

    console.log("Command:", text);

    try {
      await axios.post(MAKE_WEBHOOK, req.body);
    } catch (err) {
      console.log("Make webhook error:", err.message);
    }

    res.sendStatus(200);

  } catch (err) {
    console.log("Server error:", err.message);
    res.sendStatus(200);
  }
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("Bot filter running");
});
