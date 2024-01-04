-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 07:18 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `opac_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_registration`
--

CREATE TABLE `user_registration` (
  `First_Name` char(10) NOT NULL,
  `Last_Name` char(10) NOT NULL,
  `Title` char(5) NOT NULL,
  `Gender` char(7) NOT NULL,
  `Date` int(2) NOT NULL,
  `Month` int(2) NOT NULL,
  `Year` int(4) NOT NULL,
  `Address` text NOT NULL,
  `First_Contact` varchar(11) NOT NULL,
  `Second_Contact` varchar(11) NOT NULL,
  `First_Email` text NOT NULL,
  `Second_Email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_registration`
--

INSERT INTO `user_registration` (`First_Name`, `Last_Name`, `Title`, `Gender`, `Date`, `Month`, `Year`, `Address`, `First_Contact`, `Second_Contact`, `First_Email`, `Second_Email`) VALUES
('Rabiatul', 'Sanusi', 'Ms.', 'Female', 30, 11, 2004, 'Lot 2395 Kampong Mengkuang Masjid', '0136169837', '01124141226', 'adawiyahsan@gmail.com', 'rabiatulsan@gmail.com'),
('Adawiyah', 'Sanusi', 'Ms.', 'Female', 30, 11, 2004, 'Lot 2395 Kampong Mengkuang Masjid', '0196719345', '01124141226', 'adawiyahsan@gmail.com', 'rabiatulsan@gmail.com'),
('Adawiyah', 'Sanusi', 'Ms.', 'Female', 30, 11, 2004, 'Lot 2395 Kampong Mengkuang Masjid', '0196719345', '01124141226', 'adawiyahsan@gmail.com', 'rabiatulsan@gmail.com'),
('Fatimah', 'Ahmad', 'Mrs.', 'Female', 11, 8, 1967, 'No 38 Taman Seri Kemuning, Jitra', '0194474550', '0134585540', 'fatimah@gmail.com', 'fatimah67@gmail.com'),
('Fatimah', 'Ahmad', 'Mrs.', 'Female', 11, 8, 1967, 'No 38 Taman Seri Kemuning, Jitra', '0194474550', '0134585540', 'fatimah@gmail.com', 'fatimah67@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
