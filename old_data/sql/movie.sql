-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2020-11-29 09:01:38
-- 服务器版本： 5.7.31
-- PHP 版本： 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `movie_info`
--

-- --------------------------------------------------------

--
-- 表的结构 `movie`
--

DROP TABLE IF EXISTS `movie`;
CREATE TABLE IF NOT EXISTS `movie` (
  `ID` int(10) NOT NULL,
  `date` varchar(200) NOT NULL,
  `rating` float NOT NULL,
  `rating_count` int(10) NOT NULL,
  `rating_weight` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

ALTER TABLE director_movie ADD UNIQUE KEY (director_ID, movie_ID)

DELETE FROM `actor_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `director_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `writer_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `genre_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `language_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `region_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '');
DELETE FROM `movie` WHERE date = ''

平均分: SELECT genre, COUNT(movie_ID), AVG(rating) FROM `genre_movie` JOIN movie WHERE movie_ID = ID GROUP BY genre
SELECT actor_id, COUNT(movie_ID), AVG(rating) FROM `actor_movie` JOIN movie WHERE movie_ID = ID GROUP BY actor_id

清除空date的movie: SELECT * FROM `actor_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')
清除没有演员的movie: SELECT * FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM actor_movie)
--
-- 转存表中的数据 `movie`
--

INSERT INTO `movie` (`ID`, `date`, `rating`, `rating_count`, `rating_weight`) VALUES
(1, '1', 1, 1, '1'),
(30220799, '2020-11-20(中国大陆),2020-07-29(比利时),2020-12-18(美国网络)', 5.7, 15344, '3.1%,14.6%,49.8%,27.9%,4.6%');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
