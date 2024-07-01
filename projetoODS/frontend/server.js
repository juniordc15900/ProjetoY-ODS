const express = require("express");
const app = express();
const stripe = require("stripe")("YOUR_SECRET_STRIPE_KEY");
const bodyParser = require("body-parser");

app.use(bodyParser.json());

app.post("/create-payment-intent", async (req, res) => {
  const { amount } = req.body;

  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency: "usd",
    });

    res.status(200).send({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (e) {
    res.status(400).send({
      error: {
        message: e.message,
      },
    });
  }
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
