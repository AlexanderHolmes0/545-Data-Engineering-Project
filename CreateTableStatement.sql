
SET @@auto_increment_increment=1;
CREATE TABLE `users` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `Created` date DEFAULT NULL,
  `Value1` int(11) DEFAULT NULL,
  `Value2` char(4) DEFAULT NULL,
  `Value3` char(5) DEFAULT NULL,
  `Value4` decimal(3,2) DEFAULT NULL,
  `Value5` int(11) DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
