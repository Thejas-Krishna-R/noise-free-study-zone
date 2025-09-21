const express = require('express');
const app = express();
const PORT = 5000;

// Middleware to parse JSON
app.use(express.json());

// Test route
app.get('/', (req, res) => {
  res.send('Noise-Free Study Zone Backend is running!');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
app.post('/noise', (req, res) => {
  console.log("Received noise data:", req.body);
  res.status(200).send("Noise data received");
});
