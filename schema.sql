DROP TABLE IF EXISTS textbooks;
DROP TABLE IF EXISTS prompts;

CREATE TABLE textbooks (
  TextbookID INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  price FLOAT(6)
);

CREATE TABLE prompts (
  PromptID INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  TextbookID int,
  reflection TEXT NOT NULL,
  msg TEXT NOT NULL,
  FOREIGN KEY (TextbookID) REFERENCES textbooks(TextbookID)
);