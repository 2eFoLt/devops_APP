-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: devops_app
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ascend_groups`
--

DROP TABLE IF EXISTS `ascend_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ascend_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_name` varchar(45) NOT NULL,
  `ascend_start_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ascend_groups`
--

LOCK TABLES `ascend_groups` WRITE;
/*!40000 ALTER TABLE `ascend_groups` DISABLE KEYS */;
INSERT INTO `ascend_groups` VALUES (1,'Name1','2023-02-11 15:00:00'),(2,'Name2','2023-02-15 15:00:00'),(3,'Name3','2023-02-10 15:00:00'),(5,'Test1','2018-07-22 08:19:00');
/*!40000 ALTER TABLE `ascend_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ascend_stat`
--

DROP TABLE IF EXISTS `ascend_stat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ascend_stat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `height_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_height_id_idx` (`height_id`),
  KEY `fk_group_id_idx` (`group_id`),
  CONSTRAINT `fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `ascend_groups` (`id`),
  CONSTRAINT `fk_height_id` FOREIGN KEY (`height_id`) REFERENCES `heights` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ascend_stat`
--

LOCK TABLES `ascend_stat` WRITE;
/*!40000 ALTER TABLE `ascend_stat` DISABLE KEYS */;
INSERT INTO `ascend_stat` VALUES (1,1,1),(2,2,2),(3,2,1),(4,2,3),(5,1,5);
/*!40000 ALTER TABLE `ascend_stat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_to_user`
--

DROP TABLE IF EXISTS `group_to_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_to_user` (
  `group_id` int NOT NULL,
  `user_id` int NOT NULL,
  KEY `fk_user_to_group_idx` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_to_user`
--

LOCK TABLES `group_to_user` WRITE;
/*!40000 ALTER TABLE `group_to_user` DISABLE KEYS */;
INSERT INTO `group_to_user` VALUES (1,1),(1,2),(2,3),(2,4),(3,6);
/*!40000 ALTER TABLE `group_to_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heights`
--

DROP TABLE IF EXISTS `heights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `height` int NOT NULL COMMENT 'in metres',
  `country` varchar(45) NOT NULL,
  `ascend_counter` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heights`
--

LOCK TABLES `heights` WRITE;
/*!40000 ALTER TABLE `heights` DISABLE KEYS */;
INSERT INTO `heights` VALUES (1,'Аннапурна',8091,'Непал',2),(2,'Килиманджаро',5881,'Танзания',4),(3,'Эльбрус',5642,'Россия',0),(4,'Монблан',4810,'Швейцария',0),(5,'Казбек',5033,'Россия/Грузия',0),(6,'Фудзияма',3776,'Япония',0),(7,'test',123,'test',0),(8,'Вершина1',1234,'Страна1',0);
/*!40000 ALTER TABLE `heights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `a_test` varchar(45) NOT NULL,
  `b_test` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
INSERT INTO `test_table` VALUES (1,'a_value1','b_value1');
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ascend_counter` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test_user','example@mail.com','test_pasword','2023-10-19 15:35:43',2),(2,'test_admin','example1@mail.com','test_password','2023-10-19 17:28:24',2),(3,'kayle','kayle@mail.com','kayle','2023-10-19 17:31:06',1),(4,'mike','mike@mail.com','mike','2023-10-19 17:41:52',1),(6,'SirReas','SirReas@gmail.com','123123123','2023-11-24 02:53:43',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-21 23:52:13
