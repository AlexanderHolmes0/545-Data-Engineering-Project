CREATE TABLE "Feature_Store" (
  "index" int NOT NULL AUTO_INCREMENT,
  "salesdate" date DEFAULT NULL,
  "productid" int DEFAULT NULL,
  "region" char(1) DEFAULT NULL,
  "freeship" tinyint DEFAULT NULL,
  "discount" decimal(3,2) DEFAULT NULL,
  "itemssold" int DEFAULT NULL,
  "error_code" varchar(255) DEFAULT NULL,
  PRIMARY KEY ("index")
);
