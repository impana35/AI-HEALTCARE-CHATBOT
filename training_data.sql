-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
-- Host: 127.0.0.1
-- Generation Time: CURRENT_TIMESTAMP
-- Server version: 10.0.17-MariaDB
-- PHP Version: 5.5.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `healthchatbot_db`;
USE `healthchatbot_db`;

-- --------------------------------------------------------

-- Table structure for `training_data`

CREATE TABLE `training_data` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `MainKeyword` VARCHAR(200) NOT NULL,
  `Helping1` VARCHAR(200) NOT NULL,
  `Helping2` VARCHAR(200) NOT NULL,
  `Helping3` VARCHAR(200) NOT NULL,
  `Helping4` VARCHAR(200) NOT NULL,
  `Output` VARCHAR(500) NOT NULL,
  `Score` INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

-- Inserting data into `training_data`

INSERT INTO `training_data` (`MainKeyword`, `Helping1`, `Helping2`, `Helping3`, `Helping4`, `Output`, `Score`) VALUES
('hello', 'hello', 'hi', 'hey', 'good morning', 'Hello! How can I assist you today?', 0),
('fever', 'high temperature', 'chills', 'shivering', 'body ache', 'You may have a fever. Stay hydrated, rest, and take Paracetamol. Consult a doctor if symptoms persist.', 0),
('dizziness', 'lightheaded', 'vertigo', 'nausea', 'weakness', 'You may be experiencing dizziness. Try resting and drinking water. Seek medical attention if it continues.', 0),
('headache', 'migraine', 'tension', 'throbbing', 'sinus pain', 'For headaches, rest in a quiet place and take Ibuprofen or Acetaminophen if necessary.', 0),
('muscle pain', 'cramps', 'stiffness', 'fatigue', 'strain', 'Apply a warm compress, stay hydrated, and take muscle relaxants if needed.', 0),
('gratitude', 'thanks', 'thank you', 'appreciate', 'bye', 'You are welcome! Stay healthy and take care.', 0),
('weight management', 'weight loss', 'obesity', 'diet', 'exercise', 'A balanced diet and regular exercise can help maintain a healthy weight.', 0),
('insomnia', 'difficulty sleeping', 'stress', 'restlessness', 'fatigue', 'Try relaxation techniques, avoid caffeine before bed, and maintain a consistent sleep schedule.', 0),
('food poisoning', 'vomiting', 'diarrhea', 'stomach pain', 'nausea', 'Drink plenty of fluids and eat light foods like rice or toast. Seek medical attention if symptoms worsen.', 0),
('doctor consultation', 'appointment', 'specialist', 'physician', 'medical advice', 'For medical concerns, it is best to consult a healthcare professional.', 0),
('diabetes', 'high blood sugar', 'insulin', 'glucose', 'excessive thirst', 'Monitor blood sugar levels and follow a diabetic-friendly diet. Consult your doctor for medication.', 0),
('hypertension', 'high blood pressure', 'stress', 'heart disease', 'stroke', 'Reduce salt intake, exercise regularly, and monitor blood pressure.', 0),
('cold and flu', 'runny nose', 'sore throat', 'cough', 'sneezing', 'Stay hydrated, get plenty of rest, and consider taking antihistamines.', 0),
('depression', 'low mood', 'anxiety', 'stress', 'mental health', 'Talk to a trusted person or professional. Therapy and medication may help.', 0),
('allergy', 'itching', 'rash', 'sneezing', 'swelling', 'Avoid allergens and take antihistamines if necessary. Seek medical attention for severe reactions.', 0),
('skinrash', 'redness', 'itchy', 'irritation', 'infection', 'Apply anti-inflammatory creams or take antihistamines. Consult a doctor if persistent.', 0),
('vaccination', 'immunization', 'flu shot', 'booster', 'covid vaccine', 'Vaccines are crucial for immunity. Consult your doctor for recommendations.', 0),
('cancer treatment', 'tumor', 'chemotherapy', 'oncologist', 'radiation', 'Cancer treatment varies. Consult an oncologist for the best approach.', 0),
('stomach pain', 'gas', 'bloating', 'indigestion', 'cramps', 'Drink warm water, avoid spicy food, and take antacids if needed.', 0),
('asthma', 'breathing difficulty', 'wheezing', 'shortness of breath', 'chest tightness', 'Use your inhaler and avoid allergens. Seek emergency help for severe attacks.', 0),
('heart attack', 'chest pain', 'tightness', 'nausea', 'shortness of breath', 'Seek immediate emergency medical help. Do not ignore chest pain.', 0),
('stroke', 'weakness', 'numbness', 'blurred vision', 'dizziness', 'Seek emergency medical attention. Stroke is a medical emergency.', 0),
('arthritis', 'joint pain', 'stiffness', 'swelling', 'difficulty moving', 'Stay active, apply heat/cold therapy, and consult a doctor for pain management.', 0),
('pregnancy', 'morning sickness', 'fatigue', 'cravings', 'nausea', 'Take prenatal vitamins and maintain a healthy diet. Consult your doctor regularly.', 0);

-- --------------------------------------------------------

-- Add Indexing for Faster Searches
ALTER TABLE `training_data`
ADD FULLTEXT (`MainKeyword`, `Helping1`, `Helping2`, `Helping3`, `Helping4`);
