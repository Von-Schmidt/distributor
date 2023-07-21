import { v4 as uuidv4 } from 'uuid';
import sqlite3 from 'sqlite3';

export async function post(req) {
  let db = new sqlite3.Database('./my-database.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
      console.error(err.message);
    }
  });

  let { name, username, email, company } = req.body;
  let date_added = new Date().toISOString();

  db.run(`INSERT INTO users(name, username, email, company, date_added) VALUES(?, ?, ?, ?, ?)`, [name, username, email, company, date_added], function(err) {
    if (err) {
      return console.log(err.message);
    }
    console.log(`A row has been inserted with rowid ${this.lastID}`);
  });

  db.close();
  return { body: { status: 'success' } };
}

export async function get(req) {
  let db = new sqlite3.Database('./my-database.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
      console.error(err.message);
    }
  });

  return new Promise((resolve, reject) => {
    db.all(`SELECT * FROM users`, [], (err, rows) => {
      if (err) {
        reject({ status: 500, body: { error: 'Database error' } });
      } else {
        resolve({ status: 200, body: { users: rows } });
      }
    });

    db.close();
  });
}

