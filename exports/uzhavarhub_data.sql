-- =====================================================================
-- UzhavarHub Complete Database Export
-- Generated: 2026-10-27 21:03:24
-- Database: SQLite / PostgreSQL ANSI Compatible
-- =====================================================================

-- -----------------------------------------------------------------
-- Table structure for `backend_user`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_user`;
CREATE TABLE `backend_user` (
    `id` INTEGER PRIMARY KEY,
    `username` VARCHAR(150) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `role` VARCHAR(10) NOT NULL,
    `is_active` BOOLEAN NOT NULL,
    `date_joined` DATETIME NOT NULL
);

-- Dumping data for `backend_user` (15 records)
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (3, 'test_farmer', 'farmer@test.com', 'farmer', True, '2026-09-13T10:49:52.274405+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (4, 'test_customer', 'customer@test.com', 'customer', True, '2026-09-13T10:49:52.941170+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (51, 'farmer_ariyaluruzhavar_sandhai_280', 'farmer_ariyaluruzhavar_sandhai_280@example.com', 'farmer', True, '2026-10-27T14:29:53.573456+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (52, 'farmer_ariyaluruzhavar_sandhai_559', 'farmer_ariyaluruzhavar_sandhai_559@example.com', 'farmer', True, '2026-10-27T14:29:54.313310+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (53, 'farmer_ariyaluruzhavar_sandhai_253', 'farmer_ariyaluruzhavar_sandhai_253@example.com', 'farmer', True, '2026-10-27T14:29:55.042130+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (54, 'farmer_jameenrayapettaiuzhavar_sandhai__780', 'farmer_jameenrayapettaiuzhavar_sandhai__780@example.com', 'farmer', True, '2026-10-27T14:29:55.739889+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (55, 'farmer_chengalpetuzhavar_sandhai__628', 'farmer_chengalpetuzhavar_sandhai__628@example.com', 'farmer', True, '2026-10-27T14:29:56.451431+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (56, 'farmer_hosuruzhavar_sandhai__897', 'farmer_hosuruzhavar_sandhai__897@example.com', 'farmer', True, '2026-10-27T14:29:57.147559+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (57, 'farmer_ariyaluruzhavar_sandhai_750', 'farmer_ariyaluruzhavar_sandhai_750@example.com', 'farmer', True, '2026-10-27T14:29:57.852507+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (58, 'farmer_guduvancheriuzhavar_sandhai__493', 'farmer_guduvancheriuzhavar_sandhai__493@example.com', 'farmer', True, '2026-10-27T14:29:58.552781+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (59, 'farmer_uthukottai_apmc_273', 'farmer_uthukottai_apmc_273@example.com', 'farmer', True, '2026-10-27T14:29:59.262390+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (60, 'farmer_jeyankondam_uzhavar_sandhai__616', 'farmer_jeyankondam_uzhavar_sandhai__616@example.com', 'farmer', True, '2026-10-27T14:29:59.963748+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (61, 'farmer_jeyankondam_uzhavar_sandhai__619', 'farmer_jeyankondam_uzhavar_sandhai__619@example.com', 'farmer', True, '2026-10-27T14:30:00.669523+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (62, 'farmer_athuruzhavar_sandhai__330', 'farmer_athuruzhavar_sandhai__330@example.com', 'farmer', True, '2026-10-27T14:30:01.374859+00:00');
INSERT INTO `backend_user` (`id`, `username`, `email`, `role`, `is_active`, `date_joined`) VALUES (63, 'farmer_kumbakonam_uzhavar_sandhai__630', 'farmer_kumbakonam_uzhavar_sandhai__630@example.com', 'farmer', True, '2026-10-27T14:30:02.077686+00:00');

-- -----------------------------------------------------------------
-- Table structure for `backend_farmerprofile`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_farmerprofile`;
CREATE TABLE `backend_farmerprofile` (
    `id` INTEGER PRIMARY KEY,
    `user_id` INTEGER REFERENCES backend_user(id),
    `phone` VARCHAR(15),
    `state` VARCHAR(100),
    `district` VARCHAR(100),
    `location` VARCHAR(255),
    `farming_information` TEXT
);

-- Dumping data for `backend_farmerprofile` (14 records)
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (1, 3, '9876543210', 'Tamil Nadu', 'Coimbatore', 'Green Acres', '');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (48, 51, '9810646077', 'Tamil Nadu', 'Ariyalur', 'Ariyalur(Uzhavar Sandhai)', 'Specializes in growing high-quality crops in the Ariyalur(Uzhavar Sandhai) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (49, 52, '9845603608', 'Tamil Nadu', 'Ariyalur', 'Ariyalur(Uzhavar Sandhai)', 'Specializes in growing high-quality crops in the Ariyalur(Uzhavar Sandhai) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (50, 53, '9881410762', 'Tamil Nadu', 'Ariyalur', 'Ariyalur(Uzhavar Sandhai)', 'Specializes in growing high-quality crops in the Ariyalur(Uzhavar Sandhai) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (51, 54, '9837666441', 'Tamil Nadu', 'Chengalpattu', 'Jameenrayapettai(Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Jameenrayapettai(Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (52, 55, '9842208079', 'Tamil Nadu', 'Chengalpattu', 'Chengalpet(Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Chengalpet(Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (53, 56, '9876198602', 'Tamil Nadu', 'Krishnagiri', 'Hosur(Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Hosur(Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (54, 57, '9884997450', 'Tamil Nadu', 'Ariyalur', 'Ariyalur(Uzhavar Sandhai)', 'Specializes in growing high-quality crops in the Ariyalur(Uzhavar Sandhai) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (55, 58, '9899180609', 'Tamil Nadu', 'Chengalpattu', 'Guduvancheri(Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Guduvancheri(Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (56, 59, '9848196658', 'Tamil Nadu', 'Kancheepuram', 'Uthukottai APMC', 'Specializes in growing high-quality crops in the Uthukottai APMC region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (57, 60, '9850919059', 'Tamil Nadu', 'Ariyalur', 'Jeyankondam (Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Jeyankondam (Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (58, 61, '9848974887', 'Tamil Nadu', 'Ariyalur', 'Jeyankondam (Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Jeyankondam (Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (59, 62, '9894328203', 'Tamil Nadu', 'Salem', 'Athur(Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Athur(Uzhavar Sandhai ) region.');
INSERT INTO `backend_farmerprofile` (`id`, `user_id`, `phone`, `state`, `district`, `location`, `farming_information`) VALUES (60, 63, '9827434883', 'Tamil Nadu', 'Thanjavur', 'Kumbakonam (Uzhavar Sandhai )', 'Specializes in growing high-quality crops in the Kumbakonam (Uzhavar Sandhai ) region.');

-- -----------------------------------------------------------------
-- Table structure for `backend_customerprofile`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_customerprofile`;
CREATE TABLE `backend_customerprofile` (
    `id` INTEGER PRIMARY KEY,
    `user_id` INTEGER REFERENCES backend_user(id),
    `phone` VARCHAR(15),
    `delivery_information` TEXT
);

-- Dumping data for `backend_customerprofile` (1 records)
INSERT INTO `backend_customerprofile` (`id`, `user_id`, `phone`, `delivery_information`) VALUES (2, 4, '8765432109', '123 Main St, Chennai');

-- -----------------------------------------------------------------
-- Table structure for `backend_product`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_product`;
CREATE TABLE `backend_product` (
    `id` INTEGER PRIMARY KEY,
    `farmer_id` INTEGER REFERENCES backend_farmerprofile(id),
    `commodity` VARCHAR(100) NOT NULL,
    `variety` VARCHAR(100),
    `grade` VARCHAR(50),
    `description` TEXT,
    `location` VARCHAR(255) NOT NULL,
    `harvest_date` DATE,
    `created_at` DATETIME NOT NULL
);

-- Dumping data for `backend_product` (13 records)
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (60, 48, 'Tomato', 'Deshi', 'Local', 'Fresh Tomato straight from Ariyalur(Uzhavar Sandhai), Tamil Nadu.', 'Ariyalur(Uzhavar Sandhai)', '2026-10-27', '2026-10-27T14:29:54.267630+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (61, 49, 'Banana', 'Besrai', 'Local', 'Fresh Banana straight from Ariyalur(Uzhavar Sandhai), Tamil Nadu.', 'Ariyalur(Uzhavar Sandhai)', '2026-10-27', '2026-10-27T14:29:55.013775+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (62, 50, 'Brinjal', 'Round', 'Local', 'Fresh Brinjal straight from Ariyalur(Uzhavar Sandhai), Tamil Nadu.', 'Ariyalur(Uzhavar Sandhai)', '2026-10-27', '2026-10-27T14:29:55.712381+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (63, 51, 'Drumstick', 'Drumstick', 'Local', 'Fresh Drumstick straight from Jameenrayapettai(Uzhavar Sandhai ), Tamil Nadu.', 'Jameenrayapettai(Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:29:56.421743+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (64, 52, 'Garlic', 'Average', 'Local', 'Fresh Garlic straight from Chengalpet(Uzhavar Sandhai ), Tamil Nadu.', 'Chengalpet(Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:29:57.118541+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (65, 53, 'Jasmine', 'Jasmine', 'Local', 'Fresh Jasmine straight from Hosur(Uzhavar Sandhai ), Tamil Nadu.', 'Hosur(Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:29:57.824789+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (66, 54, 'Onion', 'Bellary', 'Local', 'Fresh Onion straight from Ariyalur(Uzhavar Sandhai), Tamil Nadu.', 'Ariyalur(Uzhavar Sandhai)', '2026-10-27', '2026-10-27T14:29:58.522579+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (67, 55, 'Orange', 'Darjeeling', 'Local', 'Fresh Orange straight from Guduvancheri(Uzhavar Sandhai ), Tamil Nadu.', 'Guduvancheri(Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:29:59.234584+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (68, 56, 'Paddy(Common)', 'Other', 'Local', 'Fresh Paddy(Common) straight from Uthukottai APMC, Tamil Nadu.', 'Uthukottai APMC', '2026-10-27', '2026-10-27T14:29:59.935359+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (69, 57, 'Pumpkin', 'Pumpkin', 'Local', 'Fresh Pumpkin straight from Jeyankondam (Uzhavar Sandhai ), Tamil Nadu.', 'Jeyankondam (Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:30:00.641123+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (70, 58, 'Mango(Raw-Ripe)', 'Mango - Raw-Ripe', 'Local', 'Fresh Mango(Raw-Ripe) straight from Jeyankondam (Uzhavar Sandhai ), Tamil Nadu.', 'Jeyankondam (Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:30:01.346974+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (71, 59, 'Jack Fruit(Ripe)', 'Jack Fruit', 'Local', 'Fresh Jack Fruit(Ripe) straight from Athur(Uzhavar Sandhai ), Tamil Nadu.', 'Athur(Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:30:02.050621+00:00');
INSERT INTO `backend_product` (`id`, `farmer_id`, `commodity`, `variety`, `grade`, `description`, `location`, `harvest_date`, `created_at`) VALUES (72, 60, 'Mango', 'Safeda', 'Local', 'Fresh Mango straight from Kumbakonam (Uzhavar Sandhai ), Tamil Nadu.', 'Kumbakonam (Uzhavar Sandhai )', '2026-10-27', '2026-10-27T14:30:02.747793+00:00');

-- -----------------------------------------------------------------
-- Table structure for `backend_listing`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_listing`;
CREATE TABLE `backend_listing` (
    `id` INTEGER PRIMARY KEY,
    `product_id` INTEGER UNIQUE REFERENCES backend_product(id),
    `selling_price_per_kg` DECIMAL(10,2) NOT NULL,
    `ai_predicted_price` DECIMAL(10,2),
    `reference_market_price` DECIMAL(10,2),
    `is_active` BOOLEAN NOT NULL,
    `created_at` DATETIME NOT NULL
);

-- Dumping data for `backend_listing` (13 records)
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (60, 60, 57.00, NULL, NULL, True, '2026-10-27T14:29:54.285059+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (61, 61, 57.00, NULL, NULL, True, '2026-10-27T14:29:55.023371+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (62, 62, 46.00, NULL, NULL, True, '2026-10-27T14:29:55.721354+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (63, 63, 275.00, NULL, NULL, True, '2026-10-27T14:29:56.432729+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (64, 64, 105.00, NULL, NULL, True, '2026-10-27T14:29:57.128052+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (65, 65, 1300.00, NULL, NULL, True, '2026-10-27T14:29:57.834222+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (66, 66, 27.50, NULL, NULL, True, '2026-10-27T14:29:58.531739+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (67, 67, 95.00, NULL, NULL, True, '2026-10-27T14:29:59.243946+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (68, 68, 19.00, NULL, NULL, True, '2026-10-27T14:29:59.944707+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (69, 69, 18.00, NULL, NULL, True, '2026-10-27T14:30:00.650557+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (70, 70, 78.00, NULL, NULL, True, '2026-10-27T14:30:01.356212+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (71, 71, 20.00, NULL, NULL, True, '2026-10-27T14:30:02.059717+00:00');
INSERT INTO `backend_listing` (`id`, `product_id`, `selling_price_per_kg`, `ai_predicted_price`, `reference_market_price`, `is_active`, `created_at`) VALUES (72, 72, 120.00, NULL, NULL, True, '2026-10-27T14:30:02.756807+00:00');

-- -----------------------------------------------------------------
-- Table structure for `backend_inventory`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_inventory`;
CREATE TABLE `backend_inventory` (
    `id` INTEGER PRIMARY KEY,
    `product_id` INTEGER UNIQUE REFERENCES backend_product(id),
    `total_quantity` DECIMAL(10,2) NOT NULL,
    `reserved_quantity` DECIMAL(10,2) NOT NULL,
    `available_quantity` DECIMAL(10,2) NOT NULL
);

-- Dumping data for `backend_inventory` (13 records)
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (58, 60, 326.00, 0.00, 326.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (59, 61, 484.00, 0.00, 484.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (60, 62, 218.00, 0.00, 218.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (61, 63, 346.00, 0.00, 346.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (62, 64, 370.00, 0.00, 370.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (63, 65, 350.00, 0.00, 350.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (64, 66, 300.00, 0.00, 300.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (65, 67, 174.00, 0.00, 174.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (66, 68, 395.00, 0.00, 395.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (67, 69, 162.00, 0.00, 162.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (68, 70, 255.00, 0.00, 255.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (69, 71, 176.00, 0.00, 176.00);
INSERT INTO `backend_inventory` (`id`, `product_id`, `total_quantity`, `reserved_quantity`, `available_quantity`) VALUES (70, 72, 295.00, 0.00, 295.00);

-- -----------------------------------------------------------------
-- Table structure for `backend_order`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_order`;
CREATE TABLE `backend_order` (
    `id` INTEGER PRIMARY KEY,
    `customer_id` INTEGER REFERENCES backend_customerprofile(id),
    `total_amount` DECIMAL(12,2) NOT NULL,
    `status` VARCHAR(20) NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL
);

-- Dumping data for `backend_order` (18 records)
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (1, 2, 114.00, 'CONFIRMED', '2026-09-13T15:25:57.830361+00:00', '2026-09-13T15:25:57.836968+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (2, 2, 755.00, 'CONFIRMED', '2026-09-15T08:10:01.152738+00:00', '2026-09-15T08:10:01.162053+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (3, 2, 1197.00, 'DELIVERED', '2026-08-21T18:04:49.614734+00:00', '2026-09-19T18:04:49.619811+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (4, 2, 2394.00, 'DELIVERED', '2026-09-15T18:04:49.629996+00:00', '2026-09-19T18:04:49.635081+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (5, 2, 1539.00, 'DELIVERED', '2026-08-24T18:04:49.643683+00:00', '2026-09-19T18:04:49.649025+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (6, 2, 2508.00, 'DELIVERED', '2026-08-30T18:04:49.672255+00:00', '2026-09-19T18:04:49.677371+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (7, 2, 912.00, 'DELIVERED', '2026-09-11T18:04:49.685485+00:00', '2026-09-19T18:04:49.690382+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (8, 2, 798.00, 'DELIVERED', '2026-08-27T18:04:49.698300+00:00', '2026-09-19T18:04:49.705740+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (9, 2, 506.00, 'DELIVERED', '2026-08-29T18:04:49.728059+00:00', '2026-09-19T18:04:49.732407+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (10, 2, 1610.00, 'DELIVERED', '2026-08-26T18:04:49.741400+00:00', '2026-09-19T18:04:49.745956+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (11, 2, 1472.00, 'DELIVERED', '2026-08-21T18:04:49.754282+00:00', '2026-09-19T18:04:49.758739+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (12, 2, 1656.00, 'DELIVERED', '2026-09-03T18:04:49.767042+00:00', '2026-09-19T18:04:49.771800+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (13, 2, 1978.00, 'DELIVERED', '2026-09-10T18:04:49.780062+00:00', '2026-09-19T18:04:49.784817+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (14, 2, 3300.00, 'DELIVERED', '2026-09-02T18:04:49.807413+00:00', '2026-09-19T18:04:49.811923+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (15, 2, 7150.00, 'DELIVERED', '2026-08-22T18:04:49.820945+00:00', '2026-09-19T18:04:49.825123+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (16, 2, 4410.00, 'DELIVERED', '2026-09-18T18:04:49.846217+00:00', '2026-09-19T18:04:49.850432+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (17, 2, 1260.00, 'DELIVERED', '2026-09-05T18:04:49.859269+00:00', '2026-09-19T18:04:49.864285+00:00');
INSERT INTO `backend_order` (`id`, `customer_id`, `total_amount`, `status`, `created_at`, `updated_at`) VALUES (18, 2, 4725.00, 'DELIVERED', '2026-09-05T18:04:49.872553+00:00', '2026-09-19T18:04:49.877337+00:00');

-- -----------------------------------------------------------------
-- Table structure for `backend_orderitem`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_orderitem`;
CREATE TABLE `backend_orderitem` (
    `id` INTEGER PRIMARY KEY,
    `order_id` INTEGER REFERENCES backend_order(id),
    `listing_id` INTEGER REFERENCES backend_listing(id),
    `quantity` DECIMAL(10,2) NOT NULL,
    `price_at_sale` DECIMAL(10,2) NOT NULL
);

-- Dumping data for `backend_orderitem` (21 records)
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (1, 1, NULL, 2.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (2, 2, NULL, 4.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (3, 2, NULL, 2.00, 105.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (4, 2, NULL, 6.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (5, 2, NULL, 1.00, 19.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (6, 3, NULL, 21.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (7, 4, NULL, 42.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (8, 5, NULL, 27.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (9, 6, NULL, 44.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (10, 7, NULL, 16.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (11, 8, NULL, 14.00, 57.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (12, 9, NULL, 11.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (13, 10, NULL, 35.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (14, 11, NULL, 32.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (15, 12, NULL, 36.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (16, 13, NULL, 43.00, 46.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (17, 14, NULL, 12.00, 275.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (18, 15, NULL, 26.00, 275.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (19, 16, NULL, 42.00, 105.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (20, 17, NULL, 12.00, 105.00);
INSERT INTO `backend_orderitem` (`id`, `order_id`, `listing_id`, `quantity`, `price_at_sale`) VALUES (21, 18, NULL, 45.00, 105.00);

-- -----------------------------------------------------------------
-- Table structure for `backend_payment`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_payment`;
CREATE TABLE `backend_payment` (
    `id` INTEGER PRIMARY KEY,
    `order_id` INTEGER UNIQUE REFERENCES backend_order(id),
    `transaction_id` VARCHAR(100),
    `amount` DECIMAL(12,2) NOT NULL,
    `status` VARCHAR(20) NOT NULL,
    `provider` VARCHAR(50) NOT NULL,
    `payment_timestamp` DATETIME,
    `verification_status` BOOLEAN NOT NULL
);

-- Dumping data for `backend_payment` (2 records)
INSERT INTO `backend_payment` (`id`, `order_id`, `transaction_id`, `amount`, `status`, `provider`, `payment_timestamp`, `verification_status`) VALUES (1, 1, NULL, 114.00, 'SUCCESS', 'TEST_MODE', '2026-09-13T15:25:57.835213+00:00', True);
INSERT INTO `backend_payment` (`id`, `order_id`, `transaction_id`, `amount`, `status`, `provider`, `payment_timestamp`, `verification_status`) VALUES (2, 2, NULL, 755.00, 'SUCCESS', 'TEST_MODE', '2026-09-15T08:10:01.160001+00:00', True);

-- -----------------------------------------------------------------
-- Table structure for `backend_researchevent`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_researchevent`;
CREATE TABLE `backend_researchevent` (
    `id` INTEGER PRIMARY KEY,
    `user_id` INTEGER REFERENCES backend_user(id),
    `event_type` VARCHAR(50) NOT NULL,
    `metadata` TEXT,
    `timestamp` DATETIME NOT NULL
);

-- Dumping data for `backend_researchevent` (235 records)
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (1, NULL, 'PRODUCT_LISTED', '{"product_id": 44, "price": "55.00"}', '2026-09-16T09:14:31.337101+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (2, NULL, 'PRODUCT_LISTED', '{"product_id": 45, "price": "55.00"}', '2026-09-16T09:15:10.262917+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (3, NULL, 'PRODUCT_LISTED', '{"product_id": 46, "price": "55.00"}', '2026-09-16T09:15:59.253811+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (4, NULL, 'PRODUCT_LISTED', '{"product_id": 50, "price": "45.00"}', '2026-09-16T09:36:27.172870+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (5, NULL, 'PRODUCT_LISTED', '{"product_id": 51, "price": "45.00"}', '2026-09-16T09:38:07.948031+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (6, NULL, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 28.35619219226585}', '2026-09-16T09:53:19.875028+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (7, NULL, 'PRODUCT_LISTED', '{"product_id": 52, "price": "45.00"}', '2026-09-16T09:53:19.930363+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (8, NULL, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 28.35619219226586}', '2026-09-16T10:01:05.350877+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (9, NULL, 'PRODUCT_LISTED', '{"product_id": 53, "price": "45.00", "ai_predicted_price": "28.36", "reference_market_price": "32.50"}', '2026-09-16T10:01:05.397903+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (10, NULL, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 28.356192192265848}', '2026-09-16T10:52:07.104641+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (11, NULL, 'PRODUCT_LISTED', '{"product_id": 54, "price": "45.00", "ai_predicted_price": "28.36", "reference_market_price": "32.50"}', '2026-09-16T10:52:07.145232+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (12, 3, 'LOGIN', '{}', '2026-09-19T17:30:32.633053+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (13, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-19T17:30:37.663644+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (14, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-19T17:30:39.692583+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (15, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:30:56.539305+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (16, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 162.0807592128308}', '2026-09-19T17:36:51.154487+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (17, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 57.400094617497615}', '2026-09-19T17:36:54.078141+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (18, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 57.40009461749761}', '2026-09-19T17:36:56.796313+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (19, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-19T17:37:56.157174+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (20, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-19T17:37:58.685719+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (21, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:38:44.136758+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (22, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 32.286523636703876}', '2026-09-19T17:38:54.244096+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (23, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 32.28652363670386}', '2026-09-19T17:38:57.235853+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (24, 4, 'LOGIN', '{}', '2026-09-19T17:39:37.476756+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (25, 4, 'PRODUCT_ADDED_TO_CART', '{"listing_id": 31, "quantity": "1"}', '2026-09-19T17:40:03.441666+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (26, 4, 'PRODUCT_ADDED_TO_CART', '{"listing_id": 33, "quantity": "1"}', '2026-09-19T17:40:04.531028+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (27, 4, 'PRODUCT_ADDED_TO_CART', '{"listing_id": 33, "quantity": "1"}', '2026-09-19T17:40:04.804015+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (28, 4, 'PRODUCT_ADDED_TO_CART', '{"listing_id": 37, "quantity": "1"}', '2026-09-19T17:40:06.394223+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (29, 4, 'PRODUCT_ADDED_TO_CART', '{"listing_id": 37, "quantity": "1"}', '2026-09-19T17:40:06.530416+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (30, 3, 'LOGIN', '{}', '2026-09-19T17:44:58.168868+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (31, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:45:01.604885+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (32, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:45:04.053471+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (33, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 41.821365370755395}', '2026-09-19T17:45:10.529147+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (34, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 41.8213653707554}', '2026-09-19T17:45:13.732728+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (35, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 41.8213653707554}', '2026-09-19T17:48:49.852865+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (36, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:57:57.425183+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (37, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T17:59:50.425438+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (38, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.500278270819404}', '2026-09-19T17:59:56.653032+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (39, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.10701054782427}', '2026-09-19T18:00:09.794250+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (40, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.107010547824274}', '2026-09-19T18:00:12.780626+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (41, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 26.741790785124167}', '2026-09-19T18:00:17.623053+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (42, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.10701054782428}', '2026-09-19T18:00:20.457684+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (43, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.10701054782427}', '2026-09-19T18:00:23.549383+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (44, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 26.741790785124163}', '2026-09-19T18:00:34.645278+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (45, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 29.169959948551245}', '2026-09-19T18:00:39.012425+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (46, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T18:02:39.133244+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (47, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-19T18:02:41.133985+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (48, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-19T18:02:42.928853+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (49, 3, 'LOGIN', '{}', '2026-09-19T18:05:38.630330+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (50, 4, 'LOGIN', '{}', '2026-09-19T18:05:42.291498+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (51, 4, 'LOGIN', '{}', '2026-09-19T18:09:09.082745+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (52, 4, 'LOGIN', '{}', '2026-09-19T18:11:21.958589+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (53, 3, 'LOGIN', '{}', '2026-09-19T18:11:29.423887+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (54, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-19T18:11:32.619210+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (55, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.500278270819404}', '2026-09-19T18:11:38.965149+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (56, 3, 'LOGIN', '{}', '2026-09-21T08:52:53.863110+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (57, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:52:56.698465+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (58, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:52:58.221636+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (59, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "orange"}', '2026-09-21T08:52:59.725394+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (60, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-21T08:53:00.951273+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (61, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "kidneybeans"}', '2026-09-21T08:53:01.704503+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (62, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coconut"}', '2026-09-21T08:53:02.437512+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (63, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-21T08:53:03.129499+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (64, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-21T08:53:03.863995+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (65, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coconut"}', '2026-09-21T08:53:04.542945+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (66, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-21T08:53:07.405297+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (67, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.58627236090092}', '2026-09-21T08:53:14.938594+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (68, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 38.370767242001605}', '2026-09-21T08:53:17.022439+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (69, 4, 'LOGIN', '{}', '2026-09-21T08:53:28.593744+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (70, 4, 'LOGIN', '{}', '2026-09-21T08:53:44.440355+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (71, 3, 'LOGIN', '{}', '2026-09-21T08:53:48.991027+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (72, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:53:50.429646+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (73, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:53:51.998231+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (74, 3, 'LOGIN', '{}', '2026-09-21T08:56:42.856381+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (75, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:56:44.290806+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (76, 3, 'LOGIN', '{}', '2026-09-21T08:57:13.627172+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (77, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:57:16.621658+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (78, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-21T08:57:19.110021+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (79, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-21T08:57:27.319560+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (80, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:57:28.555684+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (81, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:57:30.195435+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (82, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "jute"}', '2026-09-21T08:57:35.505756+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (83, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-21T08:57:37.743515+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (84, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-21T08:57:38.560533+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (85, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "lentil"}', '2026-09-21T08:57:39.271294+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (86, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-21T08:57:40.484504+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (87, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "lentil"}', '2026-09-21T08:57:41.182044+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (88, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-21T08:57:42.444181+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (89, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "jute"}', '2026-09-21T08:57:43.147141+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (90, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-21T08:57:43.600375+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (91, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-21T08:57:44.090096+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (92, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-21T08:57:44.608029+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (93, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-21T08:57:44.806447+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (94, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "lentil"}', '2026-09-21T08:57:44.966681+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (95, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:45.126054+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (96, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-21T08:57:45.296702+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (97, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:45.444821+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (98, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:46.461523+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (99, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:47.194252+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (100, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:47.383157+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (101, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:47.525681+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (102, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:47.715315+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (103, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:47.884537+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (104, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:48.035194+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (105, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:48.268844+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (106, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:48.558226+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (107, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:48.748998+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (108, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:48.932203+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (109, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:49.070865+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (110, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:49.246302+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (111, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "cotton"}', '2026-09-21T08:57:49.478269+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (112, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-21T08:57:51.343473+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (113, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:57:53.048613+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (114, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:57:54.167018+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (115, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-21T08:57:54.904000+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (116, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-21T08:57:58.803017+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (117, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.586272360900924}', '2026-09-21T08:58:05.050378+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (118, 3, 'LOGIN', '{}', '2026-09-22T02:02:06.464561+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (119, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-22T02:02:08.820578+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (120, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-22T02:02:10.725207+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (121, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:12.291724+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (122, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:13.105493+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (123, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "kidneybeans"}', '2026-09-22T02:02:14.497390+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (124, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:15.227491+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (125, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:16.004620+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (126, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:16.749790+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (127, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:17.474659+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (128, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:18.812426+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (129, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:19.363018+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (130, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:19.678510+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (131, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:19.890331+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (132, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.062044+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (133, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.258905+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (134, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.398009+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (135, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.514835+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (136, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.700627+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (137, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:20.916059+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (138, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:21.743134+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (139, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:21.970063+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (140, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:22.274108+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (141, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:22.480519+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (142, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:22.677282+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (143, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:22.873160+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (144, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:23.051851+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (145, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:23.242969+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (146, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:23.425958+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (147, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:23.623742+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (148, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:23.787998+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (149, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "kidneybeans"}', '2026-09-22T02:02:23.936859+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (150, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:24.036091+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (151, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:24.210152+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (152, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:24.367016+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (153, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:24.521168+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (154, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:24.688895+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (155, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:24.867968+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (156, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:25.045693+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (157, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:25.234817+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (158, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:25.358416+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (159, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:25.525147+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (160, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-22T02:02:25.692959+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (161, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:25.850950+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (162, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:26.020568+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (163, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:26.239318+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (164, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:26.409991+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (165, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-22T02:02:26.580233+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (166, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:26.782657+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (167, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:26.886613+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (168, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:27.045024+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (169, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:30.700127+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (170, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:33.541550+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (171, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:33.713544+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (172, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:33.910747+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (173, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-22T02:02:34.706541+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (174, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-22T02:02:35.902835+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (175, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "grapes"}', '2026-09-22T02:02:45.103875+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (176, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "banana"}', '2026-09-22T02:02:48.049723+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (177, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "grapes"}', '2026-09-22T02:02:49.601117+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (178, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-22T02:02:58.353771+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (179, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.58627236090093}', '2026-09-22T02:03:06.536218+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (180, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.063555886085098}', '2026-09-22T02:03:13.436782+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (181, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.0635558860851}', '2026-09-22T02:03:15.388699+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (182, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-22T02:03:27.795945+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (183, 3, 'LOGIN', '{}', '2026-09-22T02:03:34.591670+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (184, 4, 'LOGIN', '{}', '2026-09-22T02:03:40.398318+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (185, 4, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 21.0635558860851}', '2026-09-22T02:56:40.711010+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (186, 3, 'LOGIN', '{}', '2026-09-22T02:59:40.421741+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (187, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-22T02:59:45.239978+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (188, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-22T02:59:49.482697+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (189, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-22T02:59:51.418966+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (190, 3, 'LOGIN', '{}', '2026-09-28T10:30:39.542875+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (191, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-28T10:30:41.396594+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (192, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-28T10:30:43.416706+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (193, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-28T10:30:58.810806+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (194, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.586272360900935}', '2026-09-28T10:31:05.216428+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (195, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.58627236090091}', '2026-09-28T10:31:06.122488+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (196, 4, 'LOGIN', '{}', '2026-09-28T10:32:10.684938+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (197, 3, 'LOGIN', '{}', '2026-09-28T11:01:49.096134+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (198, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-28T11:01:50.892242+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (199, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-28T11:01:52.720774+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (200, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-28T11:01:54.138232+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (201, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "chickpea"}', '2026-09-28T11:01:57.515807+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (202, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "chickpea"}', '2026-09-28T11:01:58.300665+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (203, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-28T11:01:59.053987+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (204, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-28T11:01:59.615924+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (205, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mungbean"}', '2026-09-28T11:02:00.098628+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (206, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-28T11:02:00.644811+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (207, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-28T11:02:01.043138+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (208, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mango"}', '2026-09-28T11:02:01.571773+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (209, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "chickpea"}', '2026-09-28T11:02:01.946425+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (210, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "chickpea"}', '2026-09-28T11:02:03.545551+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (211, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-09-28T11:10:44.684578+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (212, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-28T11:10:48.843435+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (213, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-28T11:10:49.803362+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (214, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-09-28T11:10:50.030525+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (215, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "grapes"}', '2026-09-28T11:10:50.925841+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (216, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "orange"}', '2026-09-28T11:10:52.276042+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (217, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-28T11:10:52.959427+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (218, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-28T11:10:53.126407+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (219, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "coffee"}', '2026-09-28T11:10:53.280191+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (220, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "mothbeans"}', '2026-09-28T11:10:53.478794+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (221, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "orange"}', '2026-09-28T11:10:53.869328+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (222, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-28T11:10:56.869821+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (223, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-09-28T11:11:01.555058+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (224, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.58627236090091}', '2026-09-28T11:11:08.269316+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (225, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.58627236090092}', '2026-09-28T11:11:09.368852+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (226, 4, 'LOGIN', '{}', '2026-09-28T11:11:22.897473+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (227, 3, 'LOGIN', '{}', '2026-10-27T14:50:09.464047+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (228, 3, 'CROP_RECOMMENDATION_REQUESTED', '{}', '2026-10-27T14:50:11.384962+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (229, 3, 'CROP_RECOMMENDATION_VIEWED', '{"recommended_crop": "rice"}', '2026-10-27T14:50:13.304713+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (230, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-10-27T14:50:16.699039+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (231, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.586272360900924}', '2026-10-27T14:50:23.771553+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (232, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-10-27T14:50:35.003782+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (233, 3, 'PRICE_PREDICTION_REQUESTED', '{"predicted_price": 23.586272360900917}', '2026-10-27T14:50:45.759618+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (234, 3, 'MARKET_PRICE_VIEWED', '{}', '2026-10-27T14:51:23.034625+00:00');
INSERT INTO `backend_researchevent` (`id`, `user_id`, `event_type`, `metadata`, `timestamp`) VALUES (235, 4, 'LOGIN', '{}', '2026-10-27T14:51:28.030582+00:00');

-- -----------------------------------------------------------------
-- Table structure for `backend_tamsurvey`
-- -----------------------------------------------------------------
DROP TABLE IF EXISTS `backend_tamsurvey`;
CREATE TABLE `backend_tamsurvey` (
    `id` INTEGER PRIMARY KEY,
    `user_id` INTEGER REFERENCES backend_user(id),
    `perceived_usefulness` INTEGER NOT NULL,
    `perceived_ease_of_use` INTEGER NOT NULL,
    `comments` TEXT,
    `created_at` DATETIME NOT NULL
);

-- Dumping data for `backend_tamsurvey` (2 records)
INSERT INTO `backend_tamsurvey` (`id`, `user_id`, `perceived_usefulness`, `perceived_ease_of_use`, `comments`, `created_at`) VALUES (1, 3, 5, 4, 'AI dynamic pricing matches real market rates accurately.', '2026-10-27T15:26:39.424334+00:00');
INSERT INTO `backend_tamsurvey` (`id`, `user_id`, `perceived_usefulness`, `perceived_ease_of_use`, `comments`, `created_at`) VALUES (2, 4, 5, 5, 'Very convenient direct farmer marketplace, transparent prices.', '2026-10-27T15:26:39.430399+00:00');

