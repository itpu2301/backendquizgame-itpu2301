DROP DATABASE IF EXISTS quizgame;
CREATE DATABASE quizgame;

Use quizgame;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `answers` (
  `id` int(11) NOT NULL,
  `question_id` int(11) DEFAULT NULL,
  `answer` text NOT NULL,
  `is_correct` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `answers` (`id`, `question_id`, `answer`, `is_correct`) VALUES
(1, 1, 'startet und gibt Gas', 0),
(2, 1, 'biegt ab und verfährt sich', 0),
(3, 1, 'hält an und fragt Passanten', 0),
(4, 1, 'dreht und wendet', 1),
(5, 2, 'Focks Tärrier', 0),
(6, 2, 'Dallma Tiener', 0),
(7, 2, 'Re Pinnscher', 0),
(8, 2, 'Bernard Diener', 1),
(9, 3, 'ein Ungleich-Gewicht', 0),
(10, 3, 'ein Über-Maß', 0),
(11, 3, 'eine Schief-Lage', 0),
(12, 3, 'ein Miss-Verhältnis', 1),
(13, 4, 'Nünftig vernünftig', 0),
(14, 4, 'Sichtig umsichtig', 0),
(15, 4, 'Sam achtsam', 0),
(16, 4, 'Sonnen besonnen', 1),
(17, 5, 'September', 0),
(18, 5, 'November', 0),
(19, 5, 'Dezember', 0),
(20, 5, 'Oktober', 1),
(21, 6, 'Madrid', 0),
(22, 6, 'Valencia', 0),
(23, 6, 'Barcelona', 0),
(24, 6, 'Lissabon', 1),
(25, 7, 'LG Electronics', 0),
(26, 7, 'Hyundai Motor Company', 0),
(27, 7, 'Huawei', 0),
(28, 7, 'Samsung Electronics', 1),
(29, 8, '25 Jahre', 0),
(30, 8, '15 Jahre', 0),
(31, 8, '45 Jahre', 0),
(32, 8, '30 Jahre', 1),
(33, 9, 'Venus', 0),
(34, 9, 'Merkur', 0),
(35, 9, 'Jupiter', 0),
(36, 9, 'Mars', 1),
(37, 10, 'Venus', 0),
(38, 10, 'Uranus', 0),
(39, 10, 'Pluto', 0),
(40, 10, 'Merkur', 1),
(41, 11, 'China', 0),
(42, 11, 'Russland', 0),
(43, 11, 'USA', 0),
(44, 11, 'Kanada', 1),
(45, 12, '7', 0),
(46, 12, '9', 0),
(47, 12, '10', 0),
(48, 12, '8', 1),
(49, 13, 'Herr Schuler', 0),
(50, 13, 'Herr Peterson', 0),
(51, 13, 'Herr Mayer', 0),
(52, 13, 'Herr Nielson', 1),
(53, 14, '24', 0),
(54, 14, '32400', 0),
(55, 14, '6400', 0),
(56, 14, '86400', 1),
(57, 15, 'Fohlen', 0),
(58, 15, 'Ferkel', 0),
(59, 15, 'Kitz', 0),
(60, 15, 'Welpe', 1),
(61, 16, 'Bundeskanzler', 0),
(62, 16, 'Bundesrat', 0),
(63, 16, 'Bundestag', 0),
(64, 16, 'Bundesversammlung', 1),
(65, 17, 'Kreditgesellschaft auf Aktien', 0),
(66, 17, 'Kompetenzgesellschaft auf Aktien', 0),
(67, 17, 'Kardinalgesellschaft auf Aktien', 0),
(68, 17, 'Kommanditgesellschaft auf Aktien', 1),
(69, 18, 'Thomas Oppermann', 0),
(70, 18, 'Wolfgang Kubicki', 0),
(71, 18, 'Petra Pau', 0),
(72, 18, 'Wolfgang Schäuble', 1),
(73, 19, 'Demokratische Partei', 0),
(74, 19, 'Grüne Partei', 0),
(75, 19, 'Parteilos', 0),
(76, 19, 'Republikanische Partei', 1),
(77, 20, 'Richard Nixon', 0),
(78, 20, 'Dwight D. Eisenhower', 0),
(79, 20, 'George H. W. Bush', 0),
(80, 20, 'Donald Trump', 1),
(81, 21, 'Soziologie', 0),
(82, 21, 'Englisch', 0),
(83, 21, 'Mathematik', 0),
(84, 21, 'Informatik', 1),
(85, 22, 'Helium', 0),
(86, 22, 'Wasserstoff', 0),
(87, 22, 'Sauerstoff', 0),
(88, 22, 'Wasser', 1),
(89, 23, 'Kenia', 0),
(90, 23, 'Russland', 0),
(91, 23, 'USA', 0),
(92, 23, 'China', 1),
(93, 24, 'Asien', 0),
(94, 24, 'Europa', 0),
(95, 24, 'Amerika', 0),
(96, 24, 'Afrika', 1),
(97, 25, 'Alpen', 0),
(98, 25, 'Zugspitze', 0),
(99, 25, 'Annapurna', 0),
(100, 25, 'Mount Everest', 1),
(101, 26, '... eines Baumes', 0),
(102, 26, '... eines Landes', 0),
(103, 26, '... einer Stadt', 0),
(104, 26, '... eines Ozeans', 1),
(105, 27, 'Großbritannien', 0),
(106, 27, 'Kanada', 0),
(107, 27, 'Frankreich', 1),
(108, 27, 'Kanada', 0),
(109, 28, '1914', 0),
(110, 28, '1944', 0),
(111, 28, '1948', 0),
(112, 28, '1918', 1),
(113, 29, 'Koch mein Lieblingsgericht', 0),
(114, 29, 'Verführ meine Frau', 0),
(115, 29, 'Bewohn mein Haus', 0),
(116, 29, 'Sing meinen Song', 1),
(117, 30, 'Caipirinja', 0),
(118, 30, 'Cajpirinha', 0),
(119, 30, 'Caijpiriña', 0),
(120, 30, 'Caipirinha', 1),
(121, 31, 'Haarspray', 0),
(122, 31, 'Deospray', 0),
(123, 31, 'Pfefferspray', 0),
(124, 31, 'Nasenspray', 1),
(125, 32, 'Dr. Hannibal Lecter', 0),
(126, 32, 'Forrest Gump', 0),
(127, 32, 'Truman Capote', 0),
(128, 32, 'Joker', 1),
(129, 33, 'Basketball', 0),
(130, 33, 'Volleyball', 0),
(131, 33, 'Tennis', 0),
(132, 33, 'Handball', 1),
(133, 34, '25°', 0),
(134, 34, '19.25°', 0),
(135, 34, '21.5°', 0),
(136, 34, '23.5°', 1),
(137, 35, 'zwei', 0),
(138, 35, 'fünf', 0),
(139, 35, 'vier', 0),
(140, 35, 'drei', 1),
(141, 36, 'Mikrowelle', 0),
(142, 36, 'Tauchsieder', 0),
(143, 36, 'Brotbackautomat', 0),
(144, 36, 'Kühlschrank', 1),
(145, 37, 'Etwa 45 Millionen', 0),
(146, 37, 'Etwa 20 Millionen', 0),
(147, 37, 'Etwa 55 Millionen', 0),
(148, 37, 'Etwa 30 Millionen', 1),
(149, 38, '512', 0),
(150, 38, '128', 0),
(151, 38, '256', 0),
(152, 38, '336', 1),
(153, 39, 'John F. Kennedy', 0),
(154, 39, 'Harry S. Truman', 0),
(155, 39, 'Bill Clinton', 0),
(156, 39, 'Franklin D. Roosevelt', 1),
(157, 40, '54', 0),
(158, 40, '46', 0),
(159, 40, '36', 0),
(160, 40, '56', 1),
(161, 41, '22', 0),
(162, 41, '28', 0),
(163, 41, '27', 0),
(164, 41, '23', 1),
(165, 42, 'Helium', 0),
(166, 42, 'Francium', 0),
(167, 42, 'Wasserstoff', 0),
(168, 42, 'Kohlenstoff', 1);



CREATE TABLE `highscores` (
  `user` varchar(32) NOT NULL,
  `score` int(32) NOT NULL,
  `date_added` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



INSERT INTO `highscores` (`user`, `score`, `date_added`) VALUES
('dave', 500, '2024-04-17 14:47:43'),
('NewUser', 100, '2024-04-17 14:47:43'),
('micha', 500, '2024-04-17 14:47:43'),
('steve', 500, '2024-04-17 14:48:24'),
('steve', 500, '2024-04-17 14:48:35');



CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `difficulty` int(11) NOT NULL,
  `question` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `questions` (`id`, `difficulty`, `question`) VALUES
(1, 1, 'Vervollständigen Sie den Satz: “Von allen Seiten betrachtet – oder auch: Wie man es ...?”'),
(2, 1, 'Beschäftigt der fünfmalige Tour-de-France-Sieger Hinault entsprechende Hausangestellte, dann arbeiten bei ... ?'),
(3, 1, 'Lässt man sich eine Beziehung mit einer Schönheitskönigin ein, hat man sozusagen …?'),
(4, 1, 'Gesundheitsbewusste Strandurlauber sind auch beim …?'),
(5, 1, 'Wer einen Kellner sucht, findet ihn buchstäblich im …?'),
(6, 1, 'Was ist die Hauptstadt von Portugal?'),
(7, 1, 'Wie heißt das größte Technologieunternehmen in Südkorea?'),
(8, 1, 'Wie lange dauerte der 30-jährige Krieg?'),
(9, 1, 'Welcher ist der „rote Planet“ unseres Sonnensystems?'),
(10, 1, 'Welcher Planet unseres Sonnensystems ist der Sonne am nächsten?'),
(11, 1, 'Welches Land ist flächenmäßig das zweitgrößte der Erde?'),
(12, 1, 'Wie viele Planeten hat unser Sonnensystem?'),
(13, 1, 'Wie heißt Pippi Langstrumpfs Affe?'),
(14, 1, 'Wie viele Sekunden hat ein Tag?'),
(15, 1, 'Wie nennt man einen jungen Hund?'),
(16, 1, 'Wer wählt den Bundespräsidenten?'),
(17, 1, 'Wofür steht die Abkürzung KGaA?'),
(18, 1, 'Wer ist der derzeitige Bundestagspräsident? (2021)'),
(19, 1, 'Welcher Partei gehörte der 16. US-Präsident Abraham Lincoln an?'),
(20, 1, 'Gegen welchen US-Präsident wurden erstmals mehr als ein Impeachment-Verfahren gestartet?'),
(21, 1, 'Was ist das beste Fach der Welt?'),
(22, 1, 'Was ist H2O?'),
(23, 1, 'In welchem Land wohnen die meisten Menschen?'),
(24, 1, 'Auf welchem Kontinent liegt die Wüste Sahara?'),
(25, 1, 'Wie heißt der höchste Berg der Welt?'),
(26, 1, 'Wenn du die Buchstaben im Wort \"Tatalink\" anders anordnest, erhältst du den Namen...'),
(27, 2, 'Die Freiheitsstatue in New York war ein Geschenk von:'),
(28, 2, 'Wann ging der Erste Weltkrieg zu Ende?'),
(29, 2, 'In welcher Sendung kamen unter anderem Jeanette Biedermann, Mark Forster und Lena Meyer-Landrut ins Tauschgeschäft?'),
(30, 2, 'Was mancher selbst im nüchternen Zustand nicht hinbekommt: Korrekt schreibt sich der beliebte Cocktail …?'),
(31, 2, 'Wobei wird vor einem sogenannten Rebound-Effekt gewarnt, der nicht selten zu einer Abhängigkeit führt?'),
(32, 2, 'Die Darstellung welcher Figur wurde schon zweimal mit einem Schauspiel-Oscar prämiert?'),
(33, 2, 'Alfred Gislason ist seit Februar 2020 bereits der zweite Isländer im Amt des deutschen Männer-Nationaltrainers im …?'),
(34, 2, 'Wie stark ist die Erdachse zur Umlaufbahn (Ekliptik) geneigt?'),
(35, 2, 'Wie viele Herzen besitzt ein Oktopus?'),
(36, 2, '1930 erhielten Albert Einstein und ein Kollege das US-Patent 1781541. Wofür war es?'),
(37, 2, 'Wie viele Weihnachtsbäume werden in Deutschland pro Jahr verkauft?'),
(38, 2, 'Wie viele Einkerbungen hat ein Golfball?'),
(39, 2, 'Wer war während des 2. Weltkriegs US-Präsident?'),
(40, 2, 'Aus wie vielen Kräutern ist Jägermeister gemacht?'),
(41, 2, 'Wie viele Bandscheiben hat ein Mensch?'),
(42, 2, 'Woraus besteht ein Diamant?');


ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`);


ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=169;


ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;


ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`);
COMMIT;

