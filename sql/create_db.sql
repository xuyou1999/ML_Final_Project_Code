DROP DATABASE IF EXISTS `movie_info`;
CREATE DATABASE IF NOT EXISTS `movie_info` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `movie_info`;

DROP TABLE IF EXISTS `movie`;
CREATE TABLE IF NOT EXISTS `movie` (
  `ID` int(10) NOT NULL,
  `date` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` float NOT NULL,
  `rating_count` int(10) NOT NULL,
  `rating_weight` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `actor_movie`;
CREATE TABLE IF NOT EXISTS `actor_movie` (
  `actor_ID` int(10) DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `actor_ID` (`actor_ID`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `genre_movie`;
CREATE TABLE IF NOT EXISTS `genre_movie` (
  `genre` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `genre` (`genre`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `language_movie`;
CREATE TABLE IF NOT EXISTS `language_movie` (
  `language` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `language` (`language`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `director_movie`;
CREATE TABLE IF NOT EXISTS `director_movie` (
  `director_ID` int(10) DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `director_ID` (`director_ID`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `writer_movie`;
CREATE TABLE IF NOT EXISTS `writer_movie` (
  `writer_ID` int(10) DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `writer_ID` (`writer_ID`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `region_movie`;
CREATE TABLE IF NOT EXISTS `region_movie` (
  `region` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `movie_ID` int(10) NOT NULL,
  UNIQUE KEY `region` (`region`,`movie_ID`),
  KEY `movie_ID` (`movie_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;