-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: discordo
-- ------------------------------------------------------
-- Server version	5.7.33-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `biomes`
--

DROP TABLE IF EXISTS `biomes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biomes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT 'Morenka',
  `description` longtext,
  `monster_count` int(10) unsigned DEFAULT NULL,
  `loot_count` int(10) unsigned DEFAULT NULL,
  `biome_probability` enum('COMMON','RARE','EPIC') NOT NULL,
  `dark` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biomes`
--

LOCK TABLES `biomes` WRITE;
/*!40000 ALTER TABLE `biomes` DISABLE KEYS */;
INSERT INTO `biomes` VALUES (1,'Las bombolasty','W tym lesie rosna drzewa :+)',5,2,'RARE',0);
/*!40000 ALTER TABLE `biomes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `stat1` int(10) DEFAULT NULL,
  `stat2` int(10) DEFAULT NULL,
  `stat3` int(10) DEFAULT NULL,
  `stat4` int(10) DEFAULT NULL,
  `type` enum('GOLD','WEAPON','USEABLE','MISC') NOT NULL,
  `value` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'Miecz',10,20,NULL,NULL,'WEAPON',69),(2,'Mikstura metalu',20,-25,NULL,NULL,'USEABLE',120);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items_regions`
--

DROP TABLE IF EXISTS `items_regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items_regions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_item` int(10) unsigned DEFAULT NULL,
  `id_region` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items_regions`
--

LOCK TABLES `items_regions` WRITE;
/*!40000 ALTER TABLE `items_regions` DISABLE KEYS */;
INSERT INTO `items_regions` VALUES (1,1,1),(2,2,1);
/*!40000 ALTER TABLE `items_regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monster_regions`
--

DROP TABLE IF EXISTS `monster_regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monster_regions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_monster` int(10) unsigned DEFAULT NULL,
  `id_region` int(10) unsigned DEFAULT NULL,
  `hp` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monster_regions`
--

LOCK TABLES `monster_regions` WRITE;
/*!40000 ALTER TABLE `monster_regions` DISABLE KEYS */;
INSERT INTO `monster_regions` VALUES (1,1,1,20),(2,2,1,23);
/*!40000 ALTER TABLE `monster_regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monsters`
--

DROP TABLE IF EXISTS `monsters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monsters` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT 'Zygfryd',
  `biome` int(10) unsigned NOT NULL,
  `starthp` int(10) unsigned NOT NULL DEFAULT '10',
  `attack` int(10) unsigned NOT NULL DEFAULT '10',
  `defense` int(10) unsigned NOT NULL DEFAULT '10',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monsters`
--

LOCK TABLES `monsters` WRITE;
/*!40000 ALTER TABLE `monsters` DISABLE KEYS */;
INSERT INTO `monsters` VALUES (1,'Creeper, aww man',1,50,3,4),(2,'Mech Queen',1,100,1,4);
/*!40000 ALTER TABLE `monsters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `discord_id` bigint(20) unsigned NOT NULL,
  `first_msg_date` date NOT NULL,
  `last_msg_date` date DEFAULT NULL,
  `seen_tutorial` tinyint(1) NOT NULL DEFAULT '0',
  `current_region_id` int(10) unsigned NOT NULL,
  `health` int(11) DEFAULT '100',
  `mana` int(11) DEFAULT '100',
  `gold` int(11) DEFAULT '0',
  `exp` int(11) DEFAULT '0',
  PRIMARY KEY (`discord_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (666,'1999-03-03','2003-04-03',0,1,10,NULL,NULL,NULL),(723094920923054100,'2021-03-20','2021-03-20',0,1,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `biom_id` int(10) unsigned NOT NULL,
  `north_region_id` int(10) unsigned NOT NULL,
  `east_region_id` int(10) unsigned NOT NULL,
  `south_region_id` int(10) unsigned NOT NULL,
  `west_region_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
INSERT INTO `regions` VALUES (1,1,0,0,0,0);
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-20 19:46:38
