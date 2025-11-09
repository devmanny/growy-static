#!/usr/bin/env node
const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files
app.use(express.static(__dirname));

// Handle clean URLs - add .html extension if file doesn't exist
app.use((req, res, next) => {
  if (!req.path.includes('.') && req.path !== '/') {
    const htmlPath = path.join(__dirname, `${req.path}.html`);
    res.sendFile(htmlPath, (err) => {
      if (err) {
        next();
      }
    });
  } else {
    next();
  }
});

// Fallback to index.html for SPA-like behavior
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`✓ Server running at http://localhost:${PORT}`);
  console.log(`✓ Clean URLs enabled - /programs works!`);
});
