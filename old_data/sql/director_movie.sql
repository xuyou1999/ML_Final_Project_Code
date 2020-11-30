-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2020-11-29 09:17:54
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
-- 表的结构 `director_movie`
--

DROP TABLE IF EXISTS `director_movie`;
CREATE TABLE IF NOT EXISTS `director_movie` (
  `director_ID` int(11) NOT NULL,
  `movie_ID` int(11) NOT NULL,
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `director_movie`
--

INSERT INTO `director_movie` (`director_ID`, `movie_ID`) VALUES
(1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
