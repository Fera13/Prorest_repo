DROP DATABASE IF EXISTS Prorest;
CREATE DATABASE Prorest;
USE Prorest;

CREATE TABLE songs (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    song_name VARCHAR(80),
    artist VARCHAR(160),
    yt_link VARCHAR(200),
    channel_name VARCHAR(160),
    credit VARCHAR(300)
);

CREATE TABLE def_quotes (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quote VARCHAR(400)
);

CREATE TABLE per_quotes (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quote VARCHAR(400)
);

CREATE TABLE refs (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sources VARCHAR(200),
    link VARCHAR(200)
);

CREATE TABLE snacks (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    snack_name VARCHAR(160),
    benefits VARCHAR(400),
    source_id INT NOT NULL,
    FOREIGN KEY (source_id) REFERENCES refs(id)
    
);

CREATE TABLE important_dates (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    the_date DATE,
    the_time VARCHAR(5),
    title VARCHAR(100),
    msg VARCHAR(200)
);

CREATE TABLE wake_time(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    my_time text
);

INSERT INTO refs(sources, link) VALUES
("INTEGRIS Health. (2021, October 23). Foods That Give You Energy. Retrieved April 28, 2022, from https://integrisok.com/resources/on-your-health/2021/september/healthy-foods-that-give-you-energy", "https://integrisok.com/resources/on-your-health/2021/september/healthy-foods-that-give-you-energy"),
("Cirillo, F., 2006. The pomodoro technique (the pomodoro). Agile Processes in Software Engineering and, 54(2), p.35.", "http://3.249.194.220/download/pomodoro-technique.pdf"),
("Harvard Health. (2021, March 6). Foods linked to better brainpower. Retrieved April 28, 2022, from https://www.health.harvard.edu/healthbeat/foods-linked-to-better-brainpower","https://www.health.harvard.edu/healthbeat/foods-linked-to-better-brainpower"),
("Scott AJ, Webb TL, Rowse G. Does improving sleep lead to better mental health?. BMJ Open. 2017;7(9):e016873. doi:10.1136/bmjopen-2017-016873", "https://bmjopen.bmj.com/content/7/9/e016873%22"),
("Treatment to fight depression (2021, Feb). Harvard Health publishing. Retrieved January 2022 from https://www.health.harvard.edu/mind-and-mood/exercise-is-an-all-natural-treatment-to-fight-depression", "https://www.health.harvard.edu/mind-and-mood/exercise-is-an-all-natural-treatment-to-fight-depression%22");

INSERT INTO snacks(snack_name, benefits, source_id) VALUES
("Bananas", "They???re full of complex carbohydrates, vitamin B6, potassium and even a little protein.", 1),
("Dates", "Dates contain vitamins and minerals like iron, manganese, copper, potassium and magnesium, in addition to fiber and antioxidants.", 1),
("Avocados", "They???re a superfood! Avocados are rich in ???good??? fats, fiber and B vitamins. Around 85% of the fat in avocados is from monounsaturated and polyunsaturated fatty acids, which promote healthy blood-fat levels and boost the absorption of nutrients.", 1),
("Cashews", "low in sugar and rich in fiber, heart-healthy fats, and plant protein. They're a solid source of copper, magnesium and manganese which are key ingredients for energy production, healthy bones brain health and immunity.", 1),
("Leafy vegetables", "such as kale, spinach, collards, and broccoli are rich in brain-healthy nutrients like vitamin K, lutein, folate, and beta carotene. Research suggests these plant-based foods may help slow cognitive decline.", 2),
("Berries", "improves memory and delays memory decline", 2),
("Walnuts", "Walnuts are high in a type of omega-3 fatty acid called alpha-linolenic acid (ALA). Diets rich in ALA and other omega-3 fatty acids have been linked to lower blood pressure and cleaner arteries.", 2);

INSERT INTO songs(song_name, artist, yt_link, channel_name, credit) VALUES
(	"Purpose", "Jonny Easton", "https://www.youtube.com/watch?v=eZEczfSAjVQ", "BreakingCopyright ??? Royalty Free Music", 
    "Jonny Easton - Purpose is under a Creative Commons (CC BY-NC-SA 3.0) license Music promoted by BreakingCopyright: https://bit.ly/b-purpose"),
(	"Undertow", "Scott Buckley", "https://www.youtube.com/watch?v=3TKghKSDnEM", "BreakingCopyright ??? Royalty Free Music", 
    "Scott Buckley - Undertow is under a Creative Commons (CC-BY 3.0) license https://www.youtube.com/user/musicbyscottb Music promoted by BreakingCopyright: https://bit.ly/bkc-undertow "),
(	"Leaving", "AER??HEAD", "https://www.youtube.com/watch?v=cTMOQiY0axo", "BreakingCopyright ??? Royalty Free Music",
	"AER??HEAD - Leaving is under a Creative Commons (CC BY-SA 3.0) license. https://www.youtube.com/c/AER%C3%98HEAD Music promoted by BreakingCopyright: https://bit.ly/bkc-leaving"),
(	"Day In Paris", "Pyrosion", "https://www.youtube.com/watch?v=twpQogWOgAs", "BreakingCopyright ??? Royalty Free Music",
	"Pyrosion - Day In Paris is under a Creative Commons (CC BY-SA 3.0) license. https://www.youtube.com/channel/UCHX5... Music promoted by BreakingCopyright: https://bit.ly/bc-day-in-paris"),
(	"Infinity", "LEMMiNO Music", "https://www.youtube.com/watch?v=uweorwa3q34", "BreakingCopyright ??? Royalty Free Music",
	"LEMMiNO - Infinity [Chill] is released under a Creative Commons license (BY-SA) 4.0 https://www.youtube.com/user/LEMMiNOM... Music provided by BreakingCopyright: https://bit.ly/lemmino-infinity "),
(	"Timeless", "Neutrin05", "https://www.youtube.com/watch?v=gBmgk8WakJE", "BreakingCopyright ??? Royalty Free Music",
	"Neutrin05 - Timeless is under a Creative Commons (CC-BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-timeless"),
(	"Ethereal", "Punch Deck", "https://www.youtube.com/watch?v=H4BAEf5V-Yc", "BreakingCopyright ??? Royalty Free Music",
	"Punch Deck - Ethereal is under a Creative Commons (CC BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-ethereal2"),
(	"If Only You Knew", "Vorsa", "https://www.youtube.com/watch?v=YR3IcPewNlk", "BreakingCopyright ??? Royalty Free Music",
	"Song: Vorsa - If Only You Knew Music provided by BreakingCopyright: https://bit.ly/vorsa-if-only-you-knew"),
(	"Jul", "Scott Buckley ", "https://www.youtube.com/watch?v=pHJfHK4jb6E", "BreakingCopyright ??? Royalty Free Music",
	"Scott Buckley - Jul is under a Creative Commons (CC BY 3.0) license. https://youtube.com/user/musicbyscottb Music promoted by BreakingCopyright: https://bit.ly/bc-jul-song"),
(	"Your Little Wings", "Tokyo Music Walker", "https://www.youtube.com/watch?v=znarNyPELcU", "BreakingCopyright ??? Royalty Free Music",
	"Tokyo Music Walker - Your Little Wings is under a Creative Commons (CC-BY 3.0) license Music promoted by BreakingCopyright: https://bit.ly/bkc-little"),
(	"Path Of The Fireflies", "AER??HEAD", "https://www.youtube.com/watch?v=sJyO-By_9wc", "BreakingCopyright ??? Royalty Free Music",
	"AER??HEAD - Path Of The Fireflies is under a Creative Commons (CC BY-SA 3.0) license Music promoted by BreakingCopyright: https://bit.ly/b-path-fireflies"),
(	"Miss You", "Middle Child", "https://www.youtube.com/watch?v=eJ-LvX9HLrU", "BreakingCopyright ??? Royalty Free Music",
	"Middle Child - Miss You is under a Creative Commons (CC BY-SA 3.0) license. https://youtu.be/AlTKzeQB7tE Music promoted by BreakingCopyright: https://bit.ly/bkc-miss-you"),
(	"Dystopia", "Neutrin05", "https://www.youtube.com/watch?v=_1ThytX4ZiA", "BreakingCopyright ??? Royalty Free Music",
	"'Dystopia' by Neutrin05 is under a Creative Commons license (CC BY 3.0) Music promoted by BreakingCopyright: http://bit.ly/Neutrin05-Dystopia"),
(	"Sardana", "Kevin MacLeod", "https://www.youtube.com/watch?v=SzqPoVNrvMc", "BreakingCopyright ??? Royalty Free Music",
	"Music: Kevin MacLeod - Sardana Promoted by Incompetech: https://youtu.be/Xohu_aq8oqk");
    
INSERT INTO def_quotes(id, quote) VALUES
(1, "Nothing is impossible!"),
(2, "When you have a dream, you???ve got to grab it and never let go."),
(3, "A positive mindset brings positive things!"),
(4, "You will always pass failure on your way to success."),
(5, "It always seems impossible until it is done."),
(6, "Once you replace negative thoughts with positive ones, you???ll start having positive results."),
(7, "The only time you fail is when you fall down and stay down."),
(8, "If opportunity doesn???t knock, build a door."),
(9, "Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same."),
(10, "It???s not whether you get knocked down, it???s whether you get up.");

