// tests/app.test.js
const request = require('supertest');
const app = require('../app');

describe('Node UI App Tests', () => {
  test('GET /api/message returns correct JSON', async () => {
    const res = await request(app).get('/api/message');
    expect(res.statusCode).toBe(200);
    expect(res.body).toEqual({ message: 'Hello from Node.js Backend!' });
  });

  test('GET / serves the HTML file', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('<h1>Node.js App with UI</h1>');
  });
});
