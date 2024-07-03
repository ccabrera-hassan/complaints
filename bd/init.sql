-- Database: bd_complaints

-- DROP DATABASE IF EXISTS bd_complaints;

CREATE DATABASE bd_complaints
    WITH
    OWNER = admin
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


	   CREATE TABLE complaints (
    Product TEXT,
    Sub_product TEXT,
    Issue TEXT,
    Sub_issue TEXT,
    Consumer_complaint_narrative TEXT,
    Company_public_response TEXT,
    Company TEXT,
    State TEXT,
    ZIP_code TEXT,
    Tags TEXT,
    Consumer_consent_provided TEXT,
    Submitted_via TEXT,
    Company_response_to_consumer TEXT,
    Timely_response TEXT,
    Consumer_disputed TEXT,
    Complaint_ID INTEGER,
    Date_received DATE,
    Date_sent_to_company DATE
);




