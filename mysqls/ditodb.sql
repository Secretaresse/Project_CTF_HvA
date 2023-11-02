-- DROP DATABASE ditodb;
-- CREATE DATABASE ditodb;
-- CREATE USER 'jelle'@'%' IDENTIFIED BY 'ditodb';
GRANT SELECT, INSERT, DELETE, UPDATE ON ditodb.* TO 'jelle'@'%';

USE ditodb;

-- -- CREATE TABLES
-- TABLE user
CREATE TABLE ditodb.user (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX `username_UNIQUE` (username ASC) VISIBLE
  );

-- TABLE user
CREATE TABLE ditodb.challenge (
  id INT NOT NULL AUTO_INCREMENT,
  ctf VARCHAR(255) NOT NULL,
  points INT NOT NULL,
  PRIMARY KEY (id)
  );

-- TABLE flag
CREATE TABLE ditodb.flag (
  id INT NOT NULL AUTO_INCREMENT,
  flag VARCHAR(255) NOT NULL,
  challenge_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_table1_challenge1_idx (challenge_id ASC) VISIBLE,
  CONSTRAINT fk_table1_challenge1
    FOREIGN KEY (challenge_id)
    REFERENCES ditodb.challenge (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );

-- TABLE challenge complete, linking table
CREATE TABLE ditodb.challenge_complete (
  user_id INT NOT NULL,
  challenge_id INT NOT NULL,
  PRIMARY KEY (user_id, challenge_id),
  INDEX fk_user_has_challenge_challenge1_idx (challenge_id ASC) VISIBLE,
  INDEX fk_user_has_challenge_user_idx (user_id ASC) VISIBLE,
  CONSTRAINT fk_user_has_challenge_user
    FOREIGN KEY (user_id)
    REFERENCES ditodb.user (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_user_has_challenge_challenge1
    FOREIGN KEY (challenge_id)
    REFERENCES ditodb.challenge (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );


--  -- INSERT VALUES INTO TABLES
-- values for user
INSERT INTO ditodb.user VALUES(NULL,'jelle','wachtwoord');
INSERT INTO ditodb.user VALUES(NULL,'andres','wachtwoord');
INSERT INTO ditodb.user VALUES(NULL,'justin','wachtwoord');
INSERT INTO ditodb.user VALUES(NULL,'dikra','wachtwoord');

-- values for challenge
INSERT INTO ditodb.challenge VALUES(1,'pandactf',1);
INSERT INTO ditodb.challenge VALUES(2,'cookiectf',3);
INSERT INTO ditodb.challenge VALUES(3,'adminctf',5);

-- values for flag
INSERT INTO ditodb.flag VALUES(NULL,'DitoCTF(Adnvoxeqc_panda)',1);
INSERT INTO ditodb.flag VALUES(NULL,'DitoCTF(DbeHcYdr_admin)',2);
INSERT INTO ditodb.flag VALUES(NULL,'DitoCTF(MfbVhOCj_mp3)',3);

show tables;