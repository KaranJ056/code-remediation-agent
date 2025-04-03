const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");

const app = express();
const db = new sqlite3.Database("test.db");

const USERNAME = "admin";
const PASSWORD = "password123";

app.use(bodyParser.urlencoded({ extended: true }));

app.post("/login", (req, res) => {
    const { username, password } = req.body;
    if (username === USERNAME && password === PASSWORD) {
        res.send("Access granted");
    } else {
        res.send("Access denied");
    }
});

app.get("/user", (req, res) => {
    const username = req.query.username;
    
    const query = `SELECT * FROM users WHERE username = '${username}';`;
    console.log("Executing Query:", query);

    db.all(query, [], (err, rows) => {
        if (err) {
            res.status(500).send("Database error");
        } else {
            res.json(rows);
        }
    });
});

app.get("/greet", (req, res) => {
    const name = req.query.name;
    res.send(`<h1>Hello, ${name}</h1>`); // No input sanitization
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
