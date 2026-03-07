const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

const MAKE_WEBHOOK = "node-app-production-7fa7.up.railway.app";

app.post("/", async (req, res) => {
  const message = req.body.message;

  if (!message || !message.text) {
    return res.sendStatus(200);
  }

  const text = message.text;

  // Only forward commands starting with /
  if (!text.startsWith("/")) {
    return res.sendStatus(200);
  }

  try {
    await axios.post(MAKE_WEBHOOK, req.body);
  } catch (err) {
    console.log(err.message);
  }

  res.sendStatus(200);
});

app.listen(process.env.PORT || 3000, () => {
  console.log("Bot filter running");
});
