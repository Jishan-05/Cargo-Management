-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2024 at 05:21 PM
-- Server version: 11.5.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cms`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `phone_number` varchar(20) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `user_id`, `phone_number`, `address`) VALUES
(1, 4, '9878789890', '6 vv dd cdfvdf dff');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add admin', 7, 'add_admin'),
(26, 'Can change admin', 7, 'change_admin'),
(27, 'Can delete admin', 7, 'delete_admin'),
(28, 'Can view admin', 7, 'view_admin'),
(29, 'Can add booking', 8, 'add_booking'),
(30, 'Can change booking', 8, 'change_booking'),
(31, 'Can delete booking', 8, 'delete_booking'),
(32, 'Can view booking', 8, 'view_booking'),
(33, 'Can add city', 9, 'add_city'),
(34, 'Can change city', 9, 'change_city'),
(35, 'Can delete city', 9, 'delete_city'),
(36, 'Can view city', 9, 'view_city'),
(37, 'Can add country', 10, 'add_country'),
(38, 'Can change country', 10, 'change_country'),
(39, 'Can delete country', 10, 'delete_country'),
(40, 'Can view country', 10, 'view_country'),
(41, 'Can add customer', 11, 'add_customer'),
(42, 'Can change customer', 11, 'change_customer'),
(43, 'Can delete customer', 11, 'delete_customer'),
(44, 'Can view customer', 11, 'view_customer'),
(45, 'Can add deliveryroute', 12, 'add_deliveryroute'),
(46, 'Can change deliveryroute', 12, 'change_deliveryroute'),
(47, 'Can delete deliveryroute', 12, 'delete_deliveryroute'),
(48, 'Can view deliveryroute', 12, 'view_deliveryroute'),
(49, 'Can add employee', 13, 'add_employee'),
(50, 'Can change employee', 13, 'change_employee'),
(51, 'Can delete employee', 13, 'delete_employee'),
(52, 'Can view employee', 13, 'view_employee'),
(53, 'Can add parcel', 14, 'add_parcel'),
(54, 'Can change parcel', 14, 'change_parcel'),
(55, 'Can delete parcel', 14, 'delete_parcel'),
(56, 'Can view parcel', 14, 'view_parcel'),
(57, 'Can add parcelstatus', 15, 'add_parcelstatus'),
(58, 'Can change parcelstatus', 15, 'change_parcelstatus'),
(59, 'Can delete parcelstatus', 15, 'delete_parcelstatus'),
(60, 'Can view parcelstatus', 15, 'view_parcelstatus'),
(61, 'Can add pricing', 16, 'add_pricing'),
(62, 'Can change pricing', 16, 'change_pricing'),
(63, 'Can delete pricing', 16, 'delete_pricing'),
(64, 'Can view pricing', 16, 'view_pricing'),
(65, 'Can add state', 17, 'add_state'),
(66, 'Can change state', 17, 'change_state'),
(67, 'Can delete state', 17, 'delete_state'),
(68, 'Can view state', 17, 'view_state'),
(69, 'Can add user', 18, 'add_user'),
(70, 'Can change user', 18, 'change_user'),
(71, 'Can delete user', 18, 'delete_user'),
(72, 'Can view user', 18, 'view_user'),
(73, 'Can add auth group', 19, 'add_authgroup'),
(74, 'Can change auth group', 19, 'change_authgroup'),
(75, 'Can delete auth group', 19, 'delete_authgroup'),
(76, 'Can view auth group', 19, 'view_authgroup'),
(77, 'Can add auth group permissions', 20, 'add_authgrouppermissions'),
(78, 'Can change auth group permissions', 20, 'change_authgrouppermissions'),
(79, 'Can delete auth group permissions', 20, 'delete_authgrouppermissions'),
(80, 'Can view auth group permissions', 20, 'view_authgrouppermissions'),
(81, 'Can add auth permission', 21, 'add_authpermission'),
(82, 'Can change auth permission', 21, 'change_authpermission'),
(83, 'Can delete auth permission', 21, 'delete_authpermission'),
(84, 'Can view auth permission', 21, 'view_authpermission'),
(85, 'Can add auth user', 22, 'add_authuser'),
(86, 'Can change auth user', 22, 'change_authuser'),
(87, 'Can delete auth user', 22, 'delete_authuser'),
(88, 'Can view auth user', 22, 'view_authuser'),
(89, 'Can add auth user groups', 23, 'add_authusergroups'),
(90, 'Can change auth user groups', 23, 'change_authusergroups'),
(91, 'Can delete auth user groups', 23, 'delete_authusergroups'),
(92, 'Can view auth user groups', 23, 'view_authusergroups'),
(93, 'Can add auth user user permissions', 24, 'add_authuseruserpermissions'),
(94, 'Can change auth user user permissions', 24, 'change_authuseruserpermissions'),
(95, 'Can delete auth user user permissions', 24, 'delete_authuseruserpermissions'),
(96, 'Can view auth user user permissions', 24, 'view_authuseruserpermissions'),
(97, 'Can add django admin log', 25, 'add_djangoadminlog'),
(98, 'Can change django admin log', 25, 'change_djangoadminlog'),
(99, 'Can delete django admin log', 25, 'delete_djangoadminlog'),
(100, 'Can view django admin log', 25, 'view_djangoadminlog'),
(101, 'Can add django content type', 26, 'add_djangocontenttype'),
(102, 'Can change django content type', 26, 'change_djangocontenttype'),
(103, 'Can delete django content type', 26, 'delete_djangocontenttype'),
(104, 'Can view django content type', 26, 'view_djangocontenttype'),
(105, 'Can add django migrations', 27, 'add_djangomigrations'),
(106, 'Can change django migrations', 27, 'change_djangomigrations'),
(107, 'Can delete django migrations', 27, 'delete_djangomigrations'),
(108, 'Can view django migrations', 27, 'view_djangomigrations'),
(109, 'Can add django session', 28, 'add_djangosession'),
(110, 'Can change django session', 28, 'change_djangosession'),
(111, 'Can delete django session', 28, 'delete_djangosession'),
(112, 'Can view django session', 28, 'view_djangosession'),
(113, 'Can add feedback', 29, 'add_feedback'),
(114, 'Can change feedback', 29, 'change_feedback'),
(115, 'Can delete feedback', 29, 'delete_feedback'),
(116, 'Can view feedback', 29, 'view_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `parcel_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `booking_date` datetime DEFAULT current_timestamp(),
  `amount_paid` decimal(10,2) DEFAULT NULL,
  `payment_status` text NOT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `parcel_id`, `customer_id`, `booking_date`, `amount_paid`, `payment_status`, `created_at`) VALUES
(3, 8, 7, '2024-09-06 13:45:33', 16800.00, '', '2024-09-04 11:49:23'),
(22, 27, 1, NULL, NULL, '', NULL),
(23, 28, 1, '2024-09-06 15:06:34', 77500.00, '', NULL),
(24, 29, 1, '2024-09-06 15:09:02', 55100.00, '', NULL),
(25, 30, 1, '2024-09-06 15:10:37', 77500.00, '', NULL),
(26, 31, 2, '2024-09-06 14:06:48', 77500.00, '', NULL),
(27, 32, 1, '2024-09-06 15:18:39', 77500.00, 'Accepted', NULL),
(28, 33, 1, NULL, NULL, 'Pending', NULL),
(29, 34, 3, '2024-09-06 14:59:22', 77500.00, '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`id`, `name`, `state_id`) VALUES
(1, 'Ahmedabad', 1),
(2, 'Vadodara', 1),
(3, 'Mahesana', 1),
(6, 'junaghadh', 1),
(7, 'Udaypur', 2),
(8, 'ahmedabad', 1),
(10, 'Surat', 1);

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`id`, `name`) VALUES
(1, 'India'),
(5, 'Indonesia'),
(8, 'japan'),
(9, 'Russia');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `user_id`, `phone_number`, `address`) VALUES
(1, 3, '9714353300', 'c 58 al hanifiya park vatva ahmedabad'),
(2, 5, '9767895678', 'b 67 abc park near xyz arcade bapunagar ahmedabad'),
(3, 7, '9876567899', '34 rty apartment biok '),
(4, 8, '9876567894', 'f 78  fgg ghgn  gnn'),
(5, 9, '9876567894', '78 bhg vvvvv vvvvv '),
(6, 10, '8765678987', '67 bgh road near hirawadi  circle ahmedabad'),
(7, 11, '5678998765', 'g bg hnhn bbgb'),
(8, NULL, '8765678765', '');

-- --------------------------------------------------------

--
-- Table structure for table `deliveryroute`
--

CREATE TABLE `deliveryroute` (
  `id` int(11) NOT NULL,
  `from_city_id` int(11) DEFAULT NULL,
  `to_city_id` int(11) DEFAULT NULL,
  `distance_km` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `deliveryroute`
--

INSERT INTO `deliveryroute` (`id`, `from_city_id`, `to_city_id`, `distance_km`) VALUES
(2, 3, 1, 78.00),
(3, 1, 2, 110.00),
(4, 2, 1, 110.00),
(5, 2, 3, 130.00),
(6, 2, 6, 130.00),
(11, 6, 2, 123.00),
(12, 7, 1, 456.00),
(13, 1, 7, 456.00);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'system', 'admin'),
(19, 'system', 'authgroup'),
(20, 'system', 'authgrouppermissions'),
(21, 'system', 'authpermission'),
(22, 'system', 'authuser'),
(23, 'system', 'authusergroups'),
(24, 'system', 'authuseruserpermissions'),
(8, 'system', 'booking'),
(9, 'system', 'city'),
(10, 'system', 'country'),
(11, 'system', 'customer'),
(12, 'system', 'deliveryroute'),
(25, 'system', 'djangoadminlog'),
(26, 'system', 'djangocontenttype'),
(27, 'system', 'djangomigrations'),
(28, 'system', 'djangosession'),
(13, 'system', 'employee'),
(29, 'system', 'feedback'),
(14, 'system', 'parcel'),
(15, 'system', 'parcelstatus'),
(16, 'system', 'pricing'),
(17, 'system', 'state'),
(18, 'system', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-30 16:36:19.130053'),
(2, 'auth', '0001_initial', '2024-08-30 16:36:20.195296'),
(3, 'admin', '0001_initial', '2024-08-30 16:36:20.380409'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-30 16:36:20.393380'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-30 16:36:20.435801'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-30 16:36:20.566391'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-30 16:36:20.642950'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-30 16:36:20.691382'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-30 16:36:20.704369'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-30 16:36:20.850971'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-30 16:36:20.855867'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-30 16:36:20.874229'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-30 16:36:20.928039'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-30 16:36:20.986391'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-30 16:36:21.042850'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-30 16:36:21.054252'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-30 16:36:21.103713'),
(18, 'sessions', '0001_initial', '2024-08-30 16:36:21.184602'),
(19, 'system', '0001_initial', '2024-08-30 16:36:21.200267'),
(20, 'system', '0002_authgroup_authgrouppermissions_authpermission_and_more', '2024-08-30 17:21:21.124488'),
(21, 'system', '0003_feedback', '2024-09-05 07:14:05.035747');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ka0qb5nuutwr7vbs2j5805mm7knh4nh1', 'eyJ1c2VyX2lkIjo3fQ:1sma3p:Y4n5ivmu7x2wohg_kciK7m1ezXPWh4l7TWva0jZ3-gU', '2024-09-20 14:35:41.263427'),
('nvv6rv9f0z3nf8cx7axjv86df6krsyui', 'eyJ1c2VyX2lkIjo3fQ:1sljFU:C55sq-Nbar0NgpP8Gs9B8elSb4vhBBbP9jlH4Zl_UYc', '2024-09-18 06:12:12.946779'),
('vnoumxe5obpa8pacz1o7jcv8dhf4d5zv', 'eyJ1c2VyX2lkIjo0fQ:1skVqX:hhyOq3Fk0sRrtllFqIuIzJAw8rBp5_IkaKJwC402WLU', '2024-09-14 21:41:25.463552');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `employee_id` varchar(50) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `user_id`, `employee_id`, `phone_number`, `position`, `address`) VALUES
(1, 12, '1', '67976546789', 'manager', 'a 67 nr ty hall '),
(2, 10, '2', NULL, 'driver', ''),
(6, 13, '3', '6789876709', 'manager', ''),
(7, 14, '', '8987656090', 'driver', '');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `createdby` int(11) DEFAULT NULL,
  `feedback_text` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `createdby`, `feedback_text`, `created_at`) VALUES
(1, 1, 'good service\r\n', '2024-09-05 07:28:51'),
(9, 2, 'impressive work', '2024-09-05 11:20:10');

-- --------------------------------------------------------

--
-- Table structure for table `parcel`
--

CREATE TABLE `parcel` (
  `id` int(11) NOT NULL,
  `tracking_id` varchar(255) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `parcel_type` varchar(100) NOT NULL,
  `from_city_id` int(11) DEFAULT NULL,
  `to_city_id` int(11) DEFAULT NULL,
  `weight` decimal(10,2) DEFAULT NULL,
  `height` decimal(10,2) DEFAULT NULL,
  `length` decimal(10,2) DEFAULT NULL,
  `width` decimal(10,2) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `status` enum('Booked','In Transit','Delivered','Canceled') NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parcel`
--

INSERT INTO `parcel` (`id`, `tracking_id`, `customer_id`, `parcel_type`, `from_city_id`, `to_city_id`, `weight`, `height`, `length`, `width`, `price`, `status`, `created_at`, `updated_at`) VALUES
(1, '6e43a899-7bdb-41af-84fb-0a4ec8ed62c5', 1, 'small', 3, 2, 0.14, NULL, NULL, NULL, 8003.00, 'Booked', NULL, '2024-09-02 11:59:32'),
(2, '904fsdjnsdddnsd', 2, 'small', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Canceled', NULL, '2024-09-02 11:59:37'),
(8, '20bee4b7-83f4-4c92-8a36-f8db3eee84cd', 7, 'large', 2, 3, 89.00, 0.00, 0.00, 0.00, 16800.00, 'Booked', NULL, '2024-09-06 13:45:33'),
(27, '06999bbd-5239-4df5-8ca3-b8240e443db1', 1, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, '', '2024-09-04 09:51:04', '2024-09-04 09:51:04'),
(28, 'eac5fbef-3c9c-4b50-ae26-e2a8fbd9206c', 1, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, 'Booked', '2024-09-06 11:36:19', '2024-09-06 15:06:34'),
(29, 'bc0d70eb-40f4-41a6-877a-c7efc3be6df8', 1, 'small', 3, 1, NULL, NULL, NULL, NULL, 55100.00, 'Booked', '2024-09-06 11:36:50', '2024-09-06 15:09:02'),
(30, '9723f676-29bc-4656-a92f-87b68014f365', 1, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, 'Booked', '2024-09-06 13:58:17', '2024-09-06 15:10:37'),
(31, 'dc642536-cec7-43fc-9d3c-253ea78ed589', 2, 'large', 2, 1, NULL, NULL, NULL, NULL, 77500.00, 'Booked', '2024-09-06 14:06:34', '2024-09-06 14:06:48'),
(32, '7f158d75-e6fd-48d3-85c6-813ffa24c93d', 1, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, 'Booked', '2024-09-06 14:35:57', '2024-09-06 15:18:39'),
(33, 'cd966c22-87ba-4be6-9025-fff8e0723947', 1, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, '', '2024-09-06 14:43:14', '2024-09-06 14:43:14'),
(34, 'd351c550-789c-45cf-b950-a1cb24b90bd8', 3, 'small', 1, 2, NULL, NULL, NULL, NULL, 77500.00, 'Booked', '2024-09-06 14:58:10', '2024-09-06 14:59:22');

-- --------------------------------------------------------

--
-- Table structure for table `parcelstatus`
--

CREATE TABLE `parcelstatus` (
  `id` int(11) NOT NULL,
  `parcel_id` int(11) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `updated_by_user_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parcelstatus`
--

INSERT INTO `parcelstatus` (`id`, `parcel_id`, `status`, `updated_by_user_id`, `updated_at`) VALUES
(2, 1, 'Not Delivered', 1, '2024-09-20 06:56:00'),
(5, 8, 'Payment accepted', 8, '2024-09-06 13:45:33'),
(6, 8, 'Parcel arrived', 8, '2024-09-06 13:45:33'),
(7, 31, 'Payment accepted', 7, '2024-09-06 14:06:48'),
(8, 31, 'Parcel arrived', 7, '2024-09-06 14:06:48'),
(9, 34, 'Payment accepted', 7, '2024-09-06 14:59:22'),
(10, 34, 'Parcel arrived', 7, '2024-09-06 14:59:22'),
(11, 28, 'Payment accepted', 7, '2024-09-06 15:05:08'),
(12, 28, 'Parcel arrived', 7, '2024-09-06 15:05:08'),
(13, 28, 'Payment accepted', 7, '2024-09-06 15:06:34'),
(14, 28, 'Parcel arrived', 7, '2024-09-06 15:06:34'),
(15, 29, 'Payment accepted', 7, '2024-09-06 15:09:02'),
(16, 29, 'Parcel arrived', 7, '2024-09-06 15:09:02'),
(17, 30, 'Payment accepted', 7, '2024-09-06 15:10:37'),
(18, 30, 'Parcel arrived', 7, '2024-09-06 15:10:37'),
(19, 32, 'Payment accepted', 7, '2024-09-06 15:18:39'),
(20, 32, 'Parcel arrived', 7, '2024-09-06 15:18:39');

-- --------------------------------------------------------

--
-- Table structure for table `pricing`
--

CREATE TABLE `pricing` (
  `id` int(11) NOT NULL,
  `base_price` decimal(10,2) DEFAULT NULL,
  `price_per_km` decimal(10,2) DEFAULT NULL,
  `price_per_kg` decimal(10,2) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pricing`
--

INSERT INTO `pricing` (`id`, `base_price`, `price_per_km`, `price_per_kg`, `created_at`, `updated_at`) VALUES
(1, 100.00, 100.00, 100.00, '2024-08-31 08:06:27', '2024-09-05 19:48:28'),
(3, 500.00, 700.00, 678.00, '2024-09-01 14:29:56', '2024-09-01 14:29:56');

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `country_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`id`, `name`, `country_id`) VALUES
(1, 'Gujarat', 1),
(2, 'Rajesthan', 1),
(3, 'Maharashtra', 1),
(4, 'Punjab', 1),
(9, 'Himachal Pradesh', 1),
(10, 'Uttarakhand', 1),
(11, 'Tamilnadu', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `role` enum('Admin','Employee','Customer') NOT NULL,
  `date_joined` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `email`, `first_name`, `last_name`, `role`, `date_joined`) VALUES
(2, 'Rohit', '@rohit345', 'rohitmehra12@gmail.com', 'Rohit', 'randeria', 'Employee', '2024-08-04 16:06:35'),
(3, 'jishan', 'mj7890', 'jisha0786@gmail.com', 'Mansuri', 'Jishan', 'Customer', '2024-08-03 00:36:00'),
(4, 'Monit Dube', '@monit123', 'monit123@gmail.com', 'Monit', 'Dube', 'Admin', '2024-09-01 16:06:46'),
(5, 'faizan', 'fz4567', 'faizan23@gmail.com', 'Mansuri', 'Faizan', 'Customer', '2024-09-09 16:06:54'),
(6, 'akshay', 'ak4747', 'ak78@gmail.com', 'Akshay ', 'panchal', 'Employee', '2024-09-01 16:06:59'),
(7, 'Tejas Parmar', 'pbkdf2_sha256$870000$EHhNDQ2yxdQLoAJVXfZUMm$Vp+3J2n5eXn2XcSof7dzAWiRm0t22yaIYhlKohrp4S8=', 'tej67@gmail.com', 'Tejas', 'Parmar', 'Customer', '2024-09-01 16:07:03'),
(8, 'Danish', 'pbkdf2_sha256$870000$HaS8UWzhCZ6KXbZCgqMLRU$w0cd627RHw1oe/kf9qOKnicIxONwBO1NVHwbw/A4ui4=', 'danis34@gmail.com', 'Danish', 'Shaikh', 'Customer', '2024-08-14 21:35:00'),
(9, 'harry', 'pbkdf2_sha256$870000$3M7RubYjqlPpMTKFrl5Ax5$bW7Sahvu0HnoLCu7O6lZd3CsUZZXwuIYYe81Qg3RzbE=', 'harry67@gmail.com', 'harry', 'patel', 'Customer', '2024-08-31 20:28:36'),
(10, 'punit', 'punpun789', 'punpk90@gmail.om', 'punit', 'pathak', 'Customer', '2024-08-31 20:36:07'),
(11, 'manan', 'pbkdf2_sha256$870000$wNyEqMSx0XqJqAECkwpabD$va2WwggOXzsOaQNydbQSaj9z3ByO3OZAuakApXBXZmk=', 'manak6@gmail.com', 'manan', 'kolate', 'Customer', '2024-08-31 20:49:14'),
(12, 'jignes', 'jigjig00', 'jig78@gmail.com', 'jignes', 'patel', 'Employee', '2024-08-31 21:34:08'),
(13, 'rohan', 'rohan7890', 'rk092@gmail.com', 'rohan', 'kumar', 'Employee', '2024-09-01 17:38:13'),
(14, 'amaan', 'amn789amn789', 'amaan78@gmail.com', 'amaan', 'ansari', 'Employee', '2024-09-02 05:52:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_ibfk_1` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_ibfk_1` (`parcel_id`),
  ADD KEY `booking_ibfk_2` (`customer_id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `city_ibfk_1` (`state_id`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_ibfk_1` (`user_id`);

--
-- Indexes for table `deliveryroute`
--
ALTER TABLE `deliveryroute`
  ADD PRIMARY KEY (`id`),
  ADD KEY `deliveryroute_ibfk_1` (`from_city_id`),
  ADD KEY `deliveryroute_ibfk_2` (`to_city_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD KEY `employee_ibfk_1` (`user_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `feedback_ibfk_1` (`createdby`);

--
-- Indexes for table `parcel`
--
ALTER TABLE `parcel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tracking_id` (`tracking_id`),
  ADD KEY `parcel_ibfk_1` (`customer_id`),
  ADD KEY `parcel_ibfk_2` (`from_city_id`),
  ADD KEY `parcel_ibfk_3` (`to_city_id`);

--
-- Indexes for table `parcelstatus`
--
ALTER TABLE `parcelstatus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `parcelstatus_ibfk_1` (`parcel_id`),
  ADD KEY `parcelstatus_ibfk_2` (`updated_by_user_id`);

--
-- Indexes for table `pricing`
--
ALTER TABLE `pricing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`id`),
  ADD KEY `state_ibfk_1` (`country_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `deliveryroute`
--
ALTER TABLE `deliveryroute`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `parcel`
--
ALTER TABLE `parcel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `parcelstatus`
--
ALTER TABLE `parcelstatus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `pricing`
--
ALTER TABLE `pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`parcel_id`) REFERENCES `parcel` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `deliveryroute`
--
ALTER TABLE `deliveryroute`
  ADD CONSTRAINT `deliveryroute_ibfk_1` FOREIGN KEY (`from_city_id`) REFERENCES `city` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `deliveryroute_ibfk_2` FOREIGN KEY (`to_city_id`) REFERENCES `city` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`createdby`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `parcel`
--
ALTER TABLE `parcel`
  ADD CONSTRAINT `parcel_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `parcel_ibfk_2` FOREIGN KEY (`from_city_id`) REFERENCES `city` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `parcel_ibfk_3` FOREIGN KEY (`to_city_id`) REFERENCES `city` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `parcelstatus`
--
ALTER TABLE `parcelstatus`
  ADD CONSTRAINT `parcelstatus_ibfk_1` FOREIGN KEY (`parcel_id`) REFERENCES `parcel` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `parcelstatus_ibfk_2` FOREIGN KEY (`updated_by_user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `state`
--
ALTER TABLE `state`
  ADD CONSTRAINT `state_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
