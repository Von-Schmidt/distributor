import sqlite3 from 'sqlite3';
const db = new sqlite3.Database('./users.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the users database.');
});

db.serialize(() => {
  db.run(`CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            company TEXT NOT NULL,
            date_added TEXT NOT NULL
        )`, (err) => {
    if (err) {
      console.log('Error when creating table', err);
    } else {
      console.log('Table created successfully');
    }
  });
});

db.close();
