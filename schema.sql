DROP TABLE IF EXISTS `Causality`;
CREATE TABLE IF NOT EXISTS `Causality` 
(
    `concave points_mean` FLOAT NOT NULL,
    `radius_worst` FLOAT NOT NULL,
    `concave points_worst` FLOAT NOT NULL,
    `perimeter_worst` FLOAT NOT NULL,
    `area_mean` FLOAT NOT NULL,
    `perimeter_mean` FLOAT NOT NULL,
    `radius_mean` FLOAT NOT NULL,
    `diagnosis` TEXT NOT NULL,
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;