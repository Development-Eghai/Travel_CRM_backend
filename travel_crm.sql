-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 22, 2025 at 07:51 AM
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `activities`
--

INSERT INTO `activities` (`id`, `name`, `slug`, `description`, `image`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'River Rafting', 'river-rafting', 'Thrilling white-water adventure', 'https://cdn.example.com/rafting.jpg', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `activity_types`
--

DROP TABLE IF EXISTS `activity_types`;
CREATE TABLE IF NOT EXISTS `activity_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `icon_url` text,
  `tenant_id` int NOT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `activity_types`
--

INSERT INTO `activity_types` (`id`, `name`, `description`, `icon_url`, `tenant_id`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Adventure', 'High-energy activities like trekking, rafting, and ziplining', 'https://cdn.wanderpro.com/icons/adventure.png', 1, 1, '2025-08-22 12:41:42', '2025-08-22 12:41:42');

-- --------------------------------------------------------

--
-- Table structure for table `blog_categories`
--

DROP TABLE IF EXISTS `blog_categories`;
CREATE TABLE IF NOT EXISTS `blog_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `description` text,
  `image_url` text,
  `parent_id` int DEFAULT NULL,
  `tenant_id` int NOT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `sort_order` int DEFAULT '0',
  `level` int DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `blog_categories`
--

INSERT INTO `blog_categories` (`id`, `name`, `slug`, `description`, `image_url`, `parent_id`, `tenant_id`, `is_active`, `sort_order`, `level`, `created_at`, `updated_at`) VALUES
(1, 'Adventure', 'adventure', 'Outdoor and thrill-seeking travel blogs', 'https://cdn.wanderpro.com/images/adventure.jpg', 1, 1, 1, 1, 0, '2025-08-22 13:07:00', '2025-08-22 13:07:00');

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
  `is_published` tinyint(1) DEFAULT '0',
  `description` text,
  `meta_title` varchar(255) DEFAULT NULL,
  `meta_tag` text,
  `meta_description` text,
  `slug` varchar(255) DEFAULT NULL,
  `tenant_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `blog_posts`
--

INSERT INTO `blog_posts` (`id`, `heading`, `category_id`, `featured_image`, `alt_tag`, `date`, `author_name`, `tag_ids`, `is_featured`, `is_published`, `description`, `meta_title`, `meta_tag`, `meta_description`, `slug`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'Top 10 Beaches in South India', 3, 'https://cdn.wanderpro.com/blogs/beaches.jpg', 'Sunset at Kovalam Beach', '2025-08-22', 'Anand', '[1, 5, 9]', 1, 1, 'Explore the most serene and scenic beaches across Tamil Nadu and Kerala.', 'Best Beaches in South India', 'beach, travel, south india', 'A curated list of top beach destinations for your next coastal getaway.', 'best-beaches-south-india', 1, '2025-08-22 12:47:55', '2025-08-22 12:47:55');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `customer_name`, `trip_id`, `booking_type`, `booking_status`, `payment_status`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'Ananya Rao', 4, 'Fixed Departure', 'Confirmed', 'Paid', 1, '2025-08-22 11:55:45', '2025-08-22 11:55:45');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `slug`, `description`, `image`, `tenant_id`, `created_at`, `updated_at`) VALUES
(3, 'Adventuredcc', 'adventure', 'Trips focused on thrill and outdoor activities', 'https://cdn.example.com/adventure.jpg', 1, '2025-08-22 11:55:45', '2025-08-22 11:55:45');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `destinations`
--

INSERT INTO `destinations` (`id`, `name`, `slug`, `hero_image`, `description`, `parent_id`, `destination_type`, `popular_trip_ids`, `blog_category_ids`, `featured_blog_ids`, `about`, `how_to_reach`, `activity_ids`, `travel_guide_tips`, `tenant_id`, `created_at`, `updated_at`) VALUES
(2, 'Goa', 'goaaaa', 'https://example.com/goa.jpg', 'Beach paradise', NULL, 'Domestic', '[101, 102]', '[5, 6]', '[201]', 'Known for beaches and nightlife', 'Fly to Goa International Airport', '[301, 302]', 'Pack sunscreen and swimwear', 1, '2025-08-19 17:55:08', '2025-08-19 17:55:08');

-- --------------------------------------------------------

--
-- Table structure for table `fixed_departures`
--

DROP TABLE IF EXISTS `fixed_departures`;
CREATE TABLE IF NOT EXISTS `fixed_departures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `description` text,
  `tenant_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_trip_id` (`trip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `fixed_departures`
--

INSERT INTO `fixed_departures` (`id`, `trip_id`, `title`, `start_date`, `end_date`, `description`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 4, 'WanderOn Himalayan Escape', '2025-09-15 10:00:00', '2025-09-20 18:00:00', 'A 6-day fixed departure to the Himalayas', 1, '2025-08-22 12:13:42', '2025-08-22 12:13:42');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `leads`
--

INSERT INTO `leads` (`id`, `name`, `email`, `mobile`, `trip_type_id`, `destination_id`, `pickup_location`, `drop_location`, `travel_date_from`, `travel_date_to`, `adults`, `children`, `assigned_to`, `follow_up_date`, `follow_up_time`, `notes`, `status`, `tenant_id`, `created_at`, `updated_at`) VALUES
(2, 'Aarav Mehta', 'aarav@example.com', '9876543210', 1, 1, 'Mumbai', 'Leh', '2025-09-10', '2025-09-15', 2, 1, 3, '2025-08-25', '14:30:00', 'Interested in Ladakh adventure', 'new', 1, '2025-08-20 13:21:51', '2025-08-20 13:21:51');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lead_assignments`
--

INSERT INTO `lead_assignments` (`id`, `lead_id`, `assigned_to`, `due_date`, `priority`, `follow_up_date`, `comments`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 2, 4, '2025-08-26', 'High', '2025-08-25', 'Call after 10 AM. Interested in Ladakh trip.', 1, '2025-08-22 12:20:19', '2025-08-22 12:20:19');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lead_comments`
--

INSERT INTO `lead_comments` (`id`, `lead_id`, `comment`, `commented_by`, `created_at`) VALUES
(2, 2, 'Customer requested Ladakh itinerary with hotel upgrade.', 4, '2025-08-20 13:44:03');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quotations`
--

INSERT INTO `quotations` (`id`, `lead_id`, `template_name`, `trip_details`, `itenary`, `hotels`, `transport`, `cost_breakdown`, `terms`, `payment_policy`, `cancellation_policy`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 2, 'Ladakh Adventure', '7-day itinerary with hotel upgrades', '{\"day1\": \"Arrival\", \"day2\": \"Leh sightseeing\"}', '{\"Leh\": \"Hotel Grand Dragon\", \"Nubra\": \"Desert Camp\"}', '{\"type\": \"SUV\", \"provider\": \"Local Tours\"}', '{\"tax\": 5400, \"base\": 45000, \"total\": 50400}', 'Prices subject to change', '50% advance', 'Full refund before 7 days', 1, NULL, NULL),
(2, 2, 'Ladakh Adventure', '7-day itinerary with hotel upgrades', '{\"day1\": \"Arrival\", \"day2\": \"Leh sightseeing\"}', '{\"Leh\": \"Hotel Grand Dragon\", \"Nubra\": \"Desert Camp\"}', '{\"type\": \"SUV\", \"provider\": \"Local Tours\"}', '{\"tax\": 5400, \"base\": 45000, \"total\": 50400}', 'Prices subject to change', '50% advance', 'Full refund before 7 days', 1, NULL, NULL),
(3, 2, 'Ladakh Adventure', '7-day itinerary with hotel upgrades', '{\"day1\": \"Arrival\", \"day2\": \"Leh sightseeing\"}', '{\"Leh\": \"Hotel Grand Dragon\", \"Nubra\": \"Desert Camp\"}', '{\"type\": \"SUV\", \"provider\": \"Local Tours\"}', '{\"tax\": 5400, \"base\": 45000, \"total\": 50400}', 'Prices subject to change', '50% advance', 'Full refund before 7 days', 1, '2025-08-20 14:05:28', '2025-08-20 14:05:28');

-- --------------------------------------------------------

--
-- Table structure for table `quotation_items`
--

DROP TABLE IF EXISTS `quotation_items`;
CREATE TABLE IF NOT EXISTS `quotation_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quotation_id` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text,
  `quantity` int DEFAULT '1',
  `unit_price` decimal(12,2) DEFAULT NULL,
  `total_price` decimal(12,2) DEFAULT NULL,
  `sort_order` int DEFAULT '0',
  `tenant_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `quotation_id` (`quotation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quotation_items`
--

INSERT INTO `quotation_items` (`id`, `quotation_id`, `title`, `description`, `quantity`, `unit_price`, `total_price`, `sort_order`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 1, '5N Stay at Manali Resort', 'Includes breakfast and mountain view room', 1, 18500.00, 18500.00, 1, 1, '2025-08-22 13:16:40', '2025-08-22 13:16:40');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `modules`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'Sales Agent', '{\"leads\": true, \"bookings\": true, \"comments\": true, \"quotations\": false}', 1, '2025-08-22 12:30:32', '2025-08-22 12:30:32');

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
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `site_settings`
--

INSERT INTO `site_settings` (`id`, `site_title`, `company_name`, `site_description`, `logo_url`, `favicon_url`, `contact_email`, `phone_numbers`, `business_address`, `tenant_id`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'WanderPro CRM', 'WanderPro Pvt Ltd', 'Your travel CRM for leads, bookings, and blogs', 'https://cdn.wanderpro.com/logo.png', 'https://cdn.wanderpro.com/favicon.ico', 'support@wanderpro.com', '{\"sales\": \"+91-9123456780\", \"support\": \"+91-9876543210\"}', '123, MG Road, Bengaluru', 1, 1, '2025-08-22 12:37:26', '2025-08-22 12:37:26');

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
CREATE TABLE IF NOT EXISTS `tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `description` text,
  `tenant_id` int NOT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `name`, `slug`, `description`, `tenant_id`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Beach', 'beach', 'All beach-related content and destinations', 1, 1, '2025-08-22 12:51:28', '2025-08-22 12:51:28'),
(2, 'Beach1', 'Beach1', 'All beach-related content and destinations', 1, 1, '2025-08-22 12:51:28', '2025-08-22 12:51:28'),
(3, 'Beach2', 'Beach2', 'All beach-related content and destinations', 1, 1, '2025-08-22 12:51:28', '2025-08-22 12:51:28');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `title`, `priority`, `description`, `assigned_to`, `due_date`, `status`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'Call client for itinerary confirmation', 'High', 'Confirm travel dates and send updated quotation', 4, '2025-08-24', 'Pending', 1, '2025-08-22 12:26:18', '2025-08-22 12:26:18');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `trips`
--

INSERT INTO `trips` (`id`, `title`, `overview`, `destination_id`, `trip_model`, `trip_type_id`, `category_ids`, `hotel_category`, `price`, `original_price`, `pickup_location`, `drop_location`, `fixed_slots`, `tenant_id`, `created_at`, `updated_at`) VALUES
(4, 'Himalayan Adventure', 'Explore the majestic Himalayashgggggggg', 2, 'Fixed', 1, '[3, 5]', '3-Star', 12999.00, 14999.00, 'Delhi Airport', 'Delhi Airport', '[{\"end_date\": \"2025-10-07\", \"start_date\": \"2025-10-01\"}, {\"end_date\": \"2025-11-21\", \"start_date\": \"2025-11-15\"}]', 1, '2025-08-19 12:01:38', '2025-08-19 12:06:11');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `trip_days`
--

INSERT INTO `trip_days` (`id`, `trip_id`, `day_title`, `image_url`, `description`, `activity_ids`, `accommodation`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 4, 'Day 2 - Adventure Trek', 'https://cdn.example.com/day2.jpg', 'Morning trek followed by river rafting.', '[1]', 'Mountain Lodge', 1, '2025-08-22 12:06:20', '2025-08-22 12:06:20'),
(2, 4, 'Day 2 - Adventure Trek', 'https://cdn.example.com/day2.jpg', 'Morning trek followed by river rafting.', '[1]', 'Mountain Lodge', 1, '2025-08-22 12:09:25', '2025-08-22 12:09:25');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `trip_types`
--

INSERT INTO `trip_types` (`id`, `name`, `slug`, `description`, `image`, `tenant_id`, `created_at`, `updated_at`) VALUES
(1, 'Adventure', 'adventure', 'Trips focused on outdoor and thrill activities', 'https://cdn.example.com/adventure.jpg', 1, '2025-08-20 12:44:28', '2025-08-20 12:44:28');

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

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fixed_departures`
--
ALTER TABLE `fixed_departures`
  ADD CONSTRAINT `fixed_departures_ibfk_1` FOREIGN KEY (`trip_id`) REFERENCES `trips` (`id`);

--
-- Constraints for table `quotation_items`
--
ALTER TABLE `quotation_items`
  ADD CONSTRAINT `quotation_items_ibfk_1` FOREIGN KEY (`quotation_id`) REFERENCES `quotations` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
