// app.js
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

// API route example
app.get('/api/message', (req, res) => {
  res.json({ message: 'Hello from Node.js Backend!' });
});

// Root route - serves index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

if (require.main === module) {
  app.listen(3000, () => console.log('Server running on http://localhost:3000'));
}

module.exports = app; // exported for testing
