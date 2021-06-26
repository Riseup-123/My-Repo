/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.5.20-log : Database - riseup
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`riseup` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `riseup`;

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) DEFAULT NULL,
  `password` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`) values 
(2,'anju@gmail.com','sha256$WZ45vQTG$1fcd8457d921effd2811a8f79959410443c8bb9917b4'),
(3,'anna@gmail.com','<md5 HASH object @ 0x000000EB672A86C0>'),
(4,'johny@gmail.com','<md5 HASH object @ 0x0000007BCDBC8BC0>'),
(5,'maya@gmail.com','3c637af21d03fb6f5add9fd86b36bad9'),
(6,'admin@gmail.com','21232f297a57a5a743894a0e4a801fc3'),
(7,'meena@gmail.com','f8cfa9ea0362a2295d24d55851aac2bb');

/*Table structure for table `my_token` */

DROP TABLE IF EXISTS `my_token`;

CREATE TABLE `my_token` (
  `my_token_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `token` varchar(60) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`my_token_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `my_token` */

insert  into `my_token`(`my_token_id`,`lid`,`token`,`date`) values 
(1,6,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQ2OTA4NjE','2021-06-26'),
(2,6,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQ2OTA5OTA','2021-06-26'),
(3,7,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQ2OTEwNDU','2021-06-26');

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `credit` varchar(900) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `month` varchar(60) DEFAULT NULL,
  `year` varchar(60) DEFAULT NULL,
  `status` varchar(70) DEFAULT 'active',
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `news` */

insert  into `news`(`news_id`,`subject`,`content`,`url`,`credit`,`date`,`month`,`year`,`status`) values 
(1,'\"+subject+\"','\"+content+\"','\"+url+\"','\"+credit+\"','\"+date+\"','\"+month+\"','\"+year+\"',NULL);

/*Table structure for table `requirments` */

DROP TABLE IF EXISTS `requirments`;

CREATE TABLE `requirments` (
  `requirments_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(60) DEFAULT NULL,
  `age` varchar(60) DEFAULT NULL,
  `gender` varchar(60) DEFAULT NULL,
  `requirement` varchar(900) DEFAULT NULL,
  `quantity` varchar(60) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  `bystander` varchar(60) DEFAULT NULL,
  `bystander_contact` varchar(60) DEFAULT NULL,
  `patient_status` varchar(100) DEFAULT NULL,
  `permission` varchar(60) DEFAULT NULL,
  `info` varchar(1000) DEFAULT NULL,
  `pincode` varchar(60) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `status` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`requirments_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `requirments` */

insert  into `requirments`(`requirments_id`,`patient_name`,`age`,`gender`,`requirement`,`quantity`,`location`,`bystander`,`bystander_contact`,`patient_status`,`permission`,`info`,`pincode`,`date`,`status`) values 
(1,'anu','987',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `timeline` */

DROP TABLE IF EXISTS `timeline`;

CREATE TABLE `timeline` (
  `timeline_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `month` varchar(60) DEFAULT NULL,
  `year` varchar(60) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `status` varchar(60) DEFAULT 'active',
  PRIMARY KEY (`timeline_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `timeline` */

insert  into `timeline`(`timeline_id`,`name`,`date`,`month`,`year`,`url`,`pic`,`status`) values 
(1,'\"+name+\"',NULL,NULL,'0000-00-00','\"+url+\"','\"+pic.filename+\"',NULL),
(2,'\"+name+\"','\"+date+\"','\"+month+\"','\"+year+\"','\"+url+\"','\"+pic.filename+\"','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
