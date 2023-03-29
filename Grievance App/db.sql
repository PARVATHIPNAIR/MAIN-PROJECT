/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - grievance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`grievance` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `grievance`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `ctid` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(500) NOT NULL,
  `category` varchar(500) NOT NULL,
  PRIMARY KEY (`ctid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`ctid`,`type`,`category`) values 
(10,'Hostel','Room'),
(11,'Hostel','Ragging');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `complaints` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `ctid` int(11) NOT NULL,
  `status` varchar(500) NOT NULL,
  `forwordstatus` varchar(500) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cid`,`lid`,`complaints`,`date`,`ctid`,`status`,`forwordstatus`) values 
(1,12,'gsdhgsbnbsn','2023-03-24',10,'completed','null'),
(2,20,'proper notes','2023-03-27',8,'pending','null');

/*Table structure for table `hostel` */

DROP TABLE IF EXISTS `hostel`;

CREATE TABLE `hostel` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `place` varchar(500) NOT NULL,
  `pin` int(11) NOT NULL,
  `post` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `hostel` */

insert  into `hostel`(`hid`,`lid`,`name`,`place`,`pin`,`post`,`phone`) values 
(6,21,'Men\'s Hostell','Kuttippuram',679538,'kuttippuram',9074657832),
(10,29,'Womes Hostel','Kuttippuram',658976,'kuttippuram',9074657832),
(12,34,'Men\'s Hostel 2','Kuttippuram',654576,'kuttippuram',4892271159);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `type` varchar(500) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'Hostel','hostel123','hostel'),
(3,'weeee','cgfgggff','hostel'),
(8,'sneha123','sneha123','staff'),
(9,'paru123','paru123','staff'),
(10,'varsha123','varsha123','staff'),
(12,'gopika','gopika123','student'),
(14,'','','student'),
(15,'abc','abc','student'),
(17,'czc','fdg','student'),
(18,'','','student'),
(20,'farsana','farsana','student'),
(21,'hostel2','hostel2','hostel'),
(23,'navaneetha','navaneetha','student'),
(24,'navaneetha','navaneetha','student'),
(26,'kavya','kavya','student'),
(29,'hostel','hostel','hostel'),
(31,'gouri123','gouri123','staff'),
(32,'raveena','raveena','student'),
(33,'raveena','raveena','student'),
(34,'hostel3','hostel3','hostel'),
(38,'','','student'),
(39,'hari','hari','staff'),
(40,'sarath','sarath','staff'),
(41,'gouri','gouri','staff'),
(42,'','','student'),
(43,'','','student'),
(44,'','','student'),
(45,'','','student');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `reply` */

DROP TABLE IF EXISTS `reply`;

CREATE TABLE `reply` (
  `replyid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `reply` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  PRIMARY KEY (`replyid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `reply` */

insert  into `reply`(`replyid`,`cid`,`reply`,`date`) values 
(1,1,'ahdssvb','2023-03-27'),
(2,1,'fdfdfd','2023-03-27'),
(3,1,'fdfdfd','2023-03-27'),
(4,1,'okk','2023-03-27'),
(5,1,'fsdfg','2023-03-28');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `status` varchar(500) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `report` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `stid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `firstname` varchar(500) NOT NULL,
  `lastname` varchar(500) NOT NULL,
  `Department` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  PRIMARY KEY (`stid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`stid`,`lid`,`firstname`,`lastname`,`Department`,`email`,`phone`) values 
(8,39,'Hari','S','CS','hari@gmail.com',7087564356),
(10,41,'Gouri','T','IT','gouri@gmail.com',8767565654);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `first name` varchar(500) NOT NULL,
  `last name` varchar(500) NOT NULL,
  `Age` int(11) NOT NULL,
  `department` varchar(500) NOT NULL,
  `year` varchar(11) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `Type` varchar(500) NOT NULL,
  `Gender` varchar(500) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`sid`,`lid`,`first name`,`last name`,`Age`,`department`,`year`,`email`,`phone`,`Type`,`Gender`) values 
(5,12,'Gopika','G',21,'Others','First Year','gopika@gmail.com',7689098765,'',''),
(8,20,'farsana','pv',22,'Others','First Year','farsana@gmail.com',9087678954,'',''),
(9,24,'Navaneetha','M',22,'MCA','Second Year','navaneetha@gmail.com',9087675643,'Hosteler',''),
(11,26,'Kavya','v',23,'IT','Fourth Year','kavya@gmail.com',8909878765,'Hosteler',''),
(12,45,'','',0,'radiobutton','EEE','Third Year',0,'','Day Scholer');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
