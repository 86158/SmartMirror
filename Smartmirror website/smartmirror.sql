-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 18 jun 2021 om 10:13
-- Serverversie: 10.4.17-MariaDB
-- PHP-versie: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartmirror`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `randomzin`
--

CREATE TABLE `randomzin` (
  `zinId` int(11) NOT NULL,
  `zinTekst` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `randomzin`
--

INSERT INTO `randomzin` (`zinId`, `zinTekst`) VALUES
(1, 'The Best Way To Get Started Is To Quit Talking And Begin Doing.'),
(2, 'The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.'),
(3, 'Don’t Let Yesterday Take Up Too Much Of Today.'),
(4, 'You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.'),
(5, 'It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.'),
(6, 'If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.'),
(7, 'People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.'),
(8, 'Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.'),
(9, 'Did you sleep well?'),
(10, 'Je mag er zijn. Ik geloof in jou.'),
(11, 'Dank je wel voor wie jij bent.'),
(12, 'Jij bent zo prachtig. (van binnen en van buiten)'),
(13, 'Ik hoop dat je inziet hoe bijzonder je bent.'),
(14, 'Jij bent hartverwarmend.'),
(15, 'Je bent mooi zoals je bent.'),
(16, 'Je bent geweldig, prachtig, uniek!'),
(17, 'Jouw lach is betoverend.'),
(18, 'Wat heb je een mooie trui aan.'),
(19, 'Zonder jouw was ik niks <3'),
(20, 'Dank je wel dat jij er voor me bent.'),
(21, 'Jij brengt de zonnestralen in mijn dag.'),
(22, 'Je mag trots zijn op jezelf.'),
(23, 'Jouw benadering is verfrissend.'),
(24, 'De manier waarop jij dit varkentje hebt gewassen is inspirerend voor iedereen.');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `randomzin`
--
ALTER TABLE `randomzin`
  ADD PRIMARY KEY (`zinId`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `randomzin`
--
ALTER TABLE `randomzin`
  MODIFY `zinId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
