CREATE TABLE `cdw_sapp_branch` (
  `BRANCH_CITY` text,
  `BRANCH_CODE` bigint DEFAULT NULL,
  `BRANCH_NAME` text,
  `BRANCH_PHONE` text,
  `BRANCH_STATE` text,
  `BRANCH_STREET` text,
  `BRANCH_ZIP` bigint NOT NULL,
  `LAST_UPDATED` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `cdw_sapp_customer` (
  `APT_NO` text,
  `CREDIT_CARD_NO` text,
  `CUST_CITY` text,
  `CUST_COUNTRY` text,
  `CUST_EMAIL` text,
  `CUST_PHONE` text,
  `CUST_STATE` text,
  `CUST_ZIP` text,
  `FIRST_NAME` text,
  `LAST_NAME` text,
  `LAST_UPDATED` text,
  `MIDDLE_NAME` text,
  `SSN` bigint DEFAULT NULL,
  `STREET_NAME` text,
  `Residence` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `cdw_sapp_credit_card` (
  `BRANCH_CODE` bigint DEFAULT NULL,
  `CREDIT_CARD_NO` text,
  `CUST_SSN` bigint DEFAULT NULL,
  `DAY` bigint DEFAULT NULL,
  `MONTH` bigint DEFAULT NULL,
  `TRANSACTION_ID` bigint DEFAULT NULL,
  `TRANSACTION_TYPE` text,
  `TRANSACTION_VALUE` double DEFAULT NULL,
  `YEAR` bigint DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `cdw_sapp_loan_application` (
  `Application_ID` text,
  `Application_Status` text,
  `Credit_History` bigint DEFAULT NULL,
  `Dependents` text,
  `Education` text,
  `Gender` text,
  `Income` text,
  `Married` text,
  `Property_Area` text,
  `Self_Employed` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

