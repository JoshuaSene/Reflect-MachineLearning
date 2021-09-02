CREATE TABLE `rules` (
  `id_rules` int(9) NOT NULL AUTO_INCREMENT,
  `relation` varchar(50) NOT NULL,
  `action_rules` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rules`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3

CREATE TABLE `product` (
  `id_product` int(9) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) NOT NULL,
  `id_rules` int(9) NOT NULL,
  PRIMARY KEY (`id_product`),
  KEY `id_rules_FK` (`id_rules`),
  CONSTRAINT `id_rules_FK` FOREIGN KEY (`id_rules`) REFERENCES `rules` (`id_rules`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3