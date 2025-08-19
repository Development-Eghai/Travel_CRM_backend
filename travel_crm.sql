-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 19, 2025 at 07:10 AM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `travel_crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
CREATE TABLE IF NOT EXISTS `activities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `image` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blog_categories`
--

DROP TABLE IF EXISTS `blog_categories`;
CREATE TABLE IF NOT EXISTS `blog_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `image` text,
  `parent_id` int DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blog_posts`
--

DROP TABLE IF EXISTS `blog_posts`;
CREATE TABLE IF NOT EXISTS `blog_posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `heading` varchar(255) DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  `featured_image` text,
  `alt_tag` text,
  `date` date DEFAULT NULL,
  `author_name` varchar(255) DEFAULT NULL,
  `tag_ids` json DEFAULT NULL,
  `is_featured` tinyint(1) DEFAULT NULL,
  `description` text,
  `meta_title` varchar(255) DEFAULT NULL,
  `meta_tag` text,
  `meta_description` text,
  `slug` varchar(255) DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blog_tags`
--

DROP TABLE IF EXISTS `blog_tags`;
CREATE TABLE IF NOT EXISTS `blog_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
CREATE TABLE IF NOT EXISTS `bookings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) DEFAULT NULL,
  `trip_id` int DEFAULT NULL,
  `booking_type` enum('Fixed Departure','Customized') DEFAULT NULL,
  `booking_status` enum('Pending','Confirmed','Cancelled') DEFAULT NULL,
  `payment_status` enum('Pending','Paid','Refunded') DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `image` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `destinations`
--

DROP TABLE IF EXISTS `destinations`;
CREATE TABLE IF NOT EXISTS `destinations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `hero_image` text,
  `description` text,
  `parent_id` int DEFAULT NULL,
  `destination_type` enum('Domestic','International') DEFAULT NULL,
  `popular_trip_ids` json DEFAULT NULL,
  `blog_category_ids` json DEFAULT NULL,
  `featured_blog_ids` json DEFAULT NULL,
  `about` text,
  `how_to_reach` text,
  `activity_ids` json DEFAULT NULL,
  `travel_guide_tips` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `leads`
--

DROP TABLE IF EXISTS `leads`;
CREATE TABLE IF NOT EXISTS `leads` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `trip_type_id` int DEFAULT NULL,
  `destination_id` int DEFAULT NULL,
  `pickup_location` varchar(255) DEFAULT NULL,
  `drop_location` varchar(255) DEFAULT NULL,
  `travel_date_from` date DEFAULT NULL,
  `travel_date_to` date DEFAULT NULL,
  `adults` int DEFAULT NULL,
  `children` int DEFAULT NULL,
  `assigned_to` int DEFAULT NULL,
  `follow_up_date` date DEFAULT NULL,
  `follow_up_time` time DEFAULT NULL,
  `notes` text,
  `status` enum('new','contacted','quoted','booked') DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lead_assignments`
--

DROP TABLE IF EXISTS `lead_assignments`;
CREATE TABLE IF NOT EXISTS `lead_assignments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lead_id` int DEFAULT NULL,
  `assigned_to` int DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `priority` enum('Low','Medium','High') DEFAULT NULL,
  `follow_up_date` date DEFAULT NULL,
  `comments` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lead_comments`
--

DROP TABLE IF EXISTS `lead_comments`;
CREATE TABLE IF NOT EXISTS `lead_comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lead_id` int DEFAULT NULL,
  `comment` text,
  `commented_by` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
CREATE TABLE IF NOT EXISTS `menus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(255) DEFAULT NULL,
  `items` json DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quotations`
--

DROP TABLE IF EXISTS `quotations`;
CREATE TABLE IF NOT EXISTS `quotations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lead_id` int DEFAULT NULL,
  `template_name` varchar(255) DEFAULT NULL,
  `trip_details` text,
  `itenary` json DEFAULT NULL,
  `hotels` json DEFAULT NULL,
  `transport` json DEFAULT NULL,
  `cost_breakdown` json DEFAULT NULL,
  `terms` text,
  `payment_policy` text,
  `cancellation_policy` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `modules` json DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `site_settings`
--

DROP TABLE IF EXISTS `site_settings`;
CREATE TABLE IF NOT EXISTS `site_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `site_title` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `site_description` text,
  `logo_url` text,
  `favicon_url` text,
  `contact_email` varchar(255) DEFAULT NULL,
  `phone_numbers` json DEFAULT NULL,
  `business_address` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE IF NOT EXISTS `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `priority` enum('Low','Medium','High') DEFAULT NULL,
  `description` text,
  `assigned_to` int DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `status` enum('Pending','Completed') DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
CREATE TABLE IF NOT EXISTS `trips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `overview` text,
  `destination_id` int DEFAULT NULL,
  `trip_model` enum('Fixed','Custom') DEFAULT NULL,
  `trip_type_id` int DEFAULT NULL,
  `category_ids` json DEFAULT NULL,
  `hotel_category` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `original_price` decimal(10,2) DEFAULT NULL,
  `pickup_location` varchar(255) DEFAULT NULL,
  `drop_location` varchar(255) DEFAULT NULL,
  `fixed_slots` json DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trip_days`
--

DROP TABLE IF EXISTS `trip_days`;
CREATE TABLE IF NOT EXISTS `trip_days` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip_id` int DEFAULT NULL,
  `day_title` varchar(255) DEFAULT NULL,
  `image_url` text,
  `description` text,
  `activity_ids` json DEFAULT NULL,
  `accommodation` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trip_details`
--

DROP TABLE IF EXISTS `trip_details`;
CREATE TABLE IF NOT EXISTS `trip_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip_id` int DEFAULT NULL,
  `highlights` text,
  `inclusions` text,
  `exclusions` text,
  `faqs` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trip_policies`
--

DROP TABLE IF EXISTS `trip_policies`;
CREATE TABLE IF NOT EXISTS `trip_policies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip_id` int DEFAULT NULL,
  `terms` text,
  `privacy` text,
  `payment_terms` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trip_types`
--

DROP TABLE IF EXISTS `trip_types`;
CREATE TABLE IF NOT EXISTS `trip_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `image` text,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `mobile_number` varchar(20) DEFAULT NULL,
  `password_hash` text,
  `role` enum('Admin','Editor','Agent') DEFAULT NULL,
  `send_user_email` tinyint(1) DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `status` enum('Active','Inactive','Suspended') NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `first_name`, `last_name`, `mobile_number`, `password_hash`, `role`, `send_user_email`, `tenant_id`, `status`, `created_at`, `updated_at`) VALUES
(4, 'anand_dev', 'anand@example.com', 'Anand', 'Dev', '9876543210', '$2b$12$s5sx5s1uyk6hP2n.JPPQI.Yybc2Qx2o04t5YNNPy191bHiiqQR53K', 'Admin', 0, 1, 'Active', '2025-08-19 07:07:57', '2025-08-19 07:07:57');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
