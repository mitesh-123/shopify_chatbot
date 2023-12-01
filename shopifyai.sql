-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 22, 2023 at 01:02 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopifyai`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `body_html` longtext DEFAULT NULL,
  `vendor` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `title`, `body_html`, `vendor`, `status`, `price`, `stock`, `image`, `created_at`, `updated_at`) VALUES
(1, 'Gift Card', 'This is a gift card for the store', 'Snowboard Vendor', 'active', '25.0', 10, NULL, '2023-10-19 09:51:30', '0000-00-00 00:00:00'),
(2, 'Selling Plans Ski Wax', 'This is a gift card for the store', 'Chat AI Dev', 'active', '24.0', 15, NULL, '2023-10-19 09:54:08', '0000-00-00 00:00:00'),
(3, 'The 3p Fulfilled Snowboard', 'This is a gift card for the store', 'Chat AI Dev', 'active', '10.0', 8, NULL, '2023-10-19 09:56:06', '0000-00-00 00:00:00'),
(4, 'The Archived Snowboard', 'This is a gift card for the store', 'Snowboard Vendor', 'archived', '20.0', 20, NULL, '2023-10-19 09:57:47', '0000-00-00 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
