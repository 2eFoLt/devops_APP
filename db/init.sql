DROP TABLE IF EXISTS `ascend_stat`;
CREATE TABLE `ascend_stat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `height_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_height_id_idx` (`height_id`),
  KEY `fk_group_id_idx` (`group_id`),
  CONSTRAINT `fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
  CONSTRAINT `fk_height_id` FOREIGN KEY (`height_id`) REFERENCES `heights` (`id`)
);


DROP TABLE IF EXISTS `group_to_user`;
CREATE TABLE `group_to_user` (
  `group_id` int NOT NULL,
  `user_id` int NOT NULL,
);

INSERT INTO `group_to_user` VALUES (1,1),(1,2),(2,3),(2,4);


DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_name` varchar(45) NOT NULL,
  `ascend_start_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

INSERT INTO `groups` VALUES (1,'Name1','2023-02-11 15:00:00'),(2,'Name2','2023-02-15 15:00:00');


DROP TABLE IF EXISTS `heights`;
CREATE TABLE `heights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `height` int NOT NULL COMMENT 'in metres',
  `country` varchar(45) NOT NULL,
  `ascend_counter` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

INSERT INTO `heights` VALUES (1,'Аннапурна',8091,'Непал',0),(2,'Килиманджаро',5881,'Танзания',0),(3,'Эльбрус',5642,'Россия',0),(4,'Монблан',4810,'Швейцария',0),(5,'Казбек',5033,'Россия/Грузия',0),(6,'Фудзияма',3776,'Япония',0);


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ascend_counter` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

INSERT INTO `users` VALUES (1,'test_user','example@mail.com','test_pasword','2023-10-19 15:35:43',0),(2,'test_admin','example1@mail.com','test_password','2023-10-19 17:28:24',0),(3,'kayle','kayle@mail.com','kayle','2023-10-19 17:31:06',0),(4,'mike','mike@mail.com','mike','2023-10-19 17:41:52',0);
