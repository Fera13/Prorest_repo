CREATE DATABASE IF NOT EXISTS Prorest;
USE Prorest;

CREATE TABLE songs (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    song_name VARCHAR(80),
    artist VARCHAR(160),
    yt_link VARCHAR(200),
    channel_name VARCHAR(160),
    credit VARCHAR(300)
);

CREATE TABLE def_qoutes (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    qoute VARCHAR(400)
);

CREATE TABLE per_qoutes (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    qoute VARCHAR(160)
);

INSERT INTO songs(song_name, artist, yt_link, channel_name, credit) VALUES
(	"Purpose", "Jonny Easton", "https://www.youtube.com/watch?v=eZEczfSAjVQ", "BreakingCopyright — Royalty Free Music", 
    "Jonny Easton - Purpose is under a Creative Commons (CC BY-NC-SA 3.0) license Music promoted by BreakingCopyright: https://bit.ly/b-purpose"),
(	"Undertow", "Scott Buckley", "https://www.youtube.com/watch?v=3TKghKSDnEM", "BreakingCopyright — Royalty Free Music", 
    "Scott Buckley - Undertow is under a Creative Commons (CC-BY 3.0) license https://www.youtube.com/user/musicbyscottb Music promoted by BreakingCopyright: https://bit.ly/bkc-undertow "),
(	"Leaving", "AERØHEAD", "https://www.youtube.com/watch?v=cTMOQiY0axo", "BreakingCopyright — Royalty Free Music",
	"AERØHEAD - Leaving is under a Creative Commons (CC BY-SA 3.0) license. https://www.youtube.com/c/AER%C3%98HEAD Music promoted by BreakingCopyright: https://bit.ly/bkc-leaving"),
(	"Undertow", "Scott Buckley", "https://www.youtube.com/watch?v=3TKghKSDnEM", "BreakingCopyright — Royalty Free Music",
	"Scott Buckley - Undertow is under a Creative Commons (CC-BY 3.0) license https://www.youtube.com/user/musicbys... Music promoted by BreakingCopyright: https://bit.ly/bkc-undertow "),
(	"Day In Paris", "Pyrosion", "https://www.youtube.com/watch?v=twpQogWOgAs", "BreakingCopyright — Royalty Free Music",
	"Pyrosion - Day In Paris is under a Creative Commons (CC BY-SA 3.0) license. https://www.youtube.com/channel/UCHX5... Music promoted by BreakingCopyright: https://bit.ly/bc-day-in-paris"),
(	"Infinity", "LEMMiNO Music", "https://www.youtube.com/watch?v=uweorwa3q34", "BreakingCopyright — Royalty Free Music",
	"LEMMiNO - Infinity [Chill] is released under a Creative Commons license (BY-SA) 4.0 https://www.youtube.com/user/LEMMiNOM... Music provided by BreakingCopyright: https://bit.ly/lemmino-infinity "),
(	"Asleep", "HaTom", "https://www.youtube.com/watch?v=fn9fqTUHl7Q", "BreakingCopyright — Royalty Free Music",
	"HaTom - Asleep (Instrumental) is under a Creative Commons (CC-BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-instrumental"),
(	"Timeless", "Neutrin05", "https://www.youtube.com/watch?v=gBmgk8WakJE", "BreakingCopyright — Royalty Free Music",
	"Neutrin05 - Timeless is under a Creative Commons (CC-BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-timeless"),
(	"Ethereal", "Punch Deck", "https://www.youtube.com/watch?v=H4BAEf5V-Yc", "BreakingCopyright — Royalty Free Music",
	"Punch Deck - Ethereal is under a Creative Commons (CC BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-ethereal2"),
(	"If Only You Knew", "Vorsa", "https://www.youtube.com/watch?v=YR3IcPewNlk", "BreakingCopyright — Royalty Free Music",
	"Song: Vorsa - If Only You Knew Music provided by BreakingCopyright: https://bit.ly/vorsa-if-only-you-knew"),
(	"Jul", "Scott Buckley ", "https://www.youtube.com/watch?v=pHJfHK4jb6E", "BreakingCopyright — Royalty Free Music",
	"Scott Buckley - Jul is under a Creative Commons (CC BY 3.0) license. https://youtube.com/user/musicbyscottb Music promoted by BreakingCopyright: https://bit.ly/bc-jul-song"),
(	"Your Little Wings", "Tokyo Music Walker", "https://www.youtube.com/watch?v=znarNyPELcU", "BreakingCopyright — Royalty Free Music",
	"Tokyo Music Walker - Your Little Wings is under a Creative Commons (CC-BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-little"),
(	"Path Of The Fireflies", "AERØHEAD", "https://www.youtube.com/watch?v=sJyO-By_9wc", "BreakingCopyright — Royalty Free Music",
	"AERØHEAD - Path Of The Fireflies is under a Creative Commons (CC BY-SA 3.0) license Music promoted by BreakingCopyright: https://bit.ly/b-path-fireflies"),
(	"Giving Way", "AERØHEAD", "https://www.youtube.com/watch?v=MGx8-0E7rlY", "BreakingCopyright — Royalty Free Music",
	"AERØHEAD - Giving Way is under a Creative Commons (CC BY-SA 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-giving"),
(	"Miss You", "Middle Child", "https://www.youtube.com/watch?v=eJ-LvX9HLrU", "BreakingCopyright — Royalty Free Music",
	"Middle Child - Miss You is under a Creative Commons (CC BY-SA 3.0) license. https://youtu.be/AlTKzeQB7tE Music promoted by BreakingCopyright: https://bit.ly/bkc-miss-you"),
(	"Dystopia", "Neutrin05", "https://www.youtube.com/watch?v=_1ThytX4ZiA", "BreakingCopyright — Royalty Free Music",
	"'Dystopia' by Neutrin05 is under a Creative Commons license (CC BY 3.0) Music promoted by BreakingCopyright: http://bit.ly/Neutrin05-Dystopia"),
(	"Sardana", "Kevin MacLeod", "https://www.youtube.com/watch?v=SzqPoVNrvMc", "BreakingCopyright — Royalty Free Music",
	"Music: Kevin MacLeod - Sardana Promoted by Incompetech: https://youtu.be/Xohu_aq8oqk");
