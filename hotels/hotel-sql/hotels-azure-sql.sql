-- Create a table on Azure SQL Database
DROP TABLE IF EXISTS tbl_hotels;
CREATE TABLE tbl_hotels
(
    Id TINYINT PRIMARY KEY,
    Modified DateTime NULL DEFAULT '0000-00-00 00:00:00',
    IsDeleted TINYINT,
    HotelName VARCHAR(40),
    Category VARCHAR(20),
    City VARCHAR(30),
    State VARCHAR(4),
    Description VARCHAR(500)
);


-- Insert rows
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (1, CURRENT_TIMESTAMP, 0,  'Stay-Kay City Hotel', 'Boutique', 'New York', 'NY', 'This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of Americas most attractive and cosmopolitan cities.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (10, CURRENT_TIMESTAMP, 0, 'Countryside Hotel', 'Extended-Stay', 'Durham', 'NC', 'Save up to 50% off traditional hotels. Free WiFi, great location near downtown, full kitchen, washer & dryer, 24\/7 support, bowling alley, fitness center and more.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (11, CURRENT_TIMESTAMP, 0, 'Royal Cottage Resort', 'Extended-Stay', 'Bothell', 'WA', 'Your home away from home. Brand new fully equipped premium rooms, fast WiFi, full kitchen, washer & dryer, fitness center. Inner courtyard includes water features and outdoor seating. All units include fireplaces and small outdoor balconies. Pets accepted.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (12, CURRENT_TIMESTAMP, 0, 'Winter Panorama Resort', 'Resort and Spa', 'Wilsonville', 'OR', 'Plenty of great skiing, outdoor ice skating, sleigh rides, tubing and snow biking. Yoga, group exercise classes and outdoor hockey are available year-round, plus numerous options for shopping as well as great spa services. Newly-renovated with large rooms, free 24-hr airport shuttle & a new restaurant. Rooms\/suites offer mini-fridges & 49-inch HDTVs.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (13, CURRENT_TIMESTAMP, 0, 'Luxury Lion Resort', 'Luxury', 'St. Louis', 'MO', 'Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (14, CURRENT_TIMESTAMP, 0, 'Twin Vortex Hotel', 'Luxury', 'Dallas', 'TX', 'New experience in the making. Be the first to experience the luxury of the Twin Vortex. Reserve one of our newly-renovated guest rooms today.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (15, CURRENT_TIMESTAMP, 0, 'By the Market Hotel', 'Budget', 'New York', 'NY', 'Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (16, CURRENT_TIMESTAMP, 0, 'Double Sanctuary Resort', 'Resort and Spa', 'Seattle', 'WA', '5 Star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in\/out, Fitness Center & espresso in room.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (17, CURRENT_TIMESTAMP, 0, 'City Skyline Antiquity Hotel', 'Boutique', 'New York', 'NY', 'In vogue since 1888, the Antiquity Hotel takes you back to bygone era. From the crystal chandeliers that adorn the Green Room, to the arched ceilings of the Grand Hall, the elegance of old New York beckons. Elevate Your Experience. Upgrade to a premiere city skyline view for less, where old world charm combines with dramatic views of the city, local cathedral and midtown.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (18, CURRENT_TIMESTAMP, 0, 'Ocean Water Resort & Spa', 'Luxury', 'Tampa', 'FL', 'New Luxury Hotel for the vacation of a lifetime. Bay views from every room, location near the pier, rooftop pool, waterfront dining & more.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (19, CURRENT_TIMESTAMP, 0, 'Economy Universe Motel', 'Budget', 'Redmond', 'WA', 'Local, family-run hotel in bustling downtown Redmond. We are a pet-friendly establishment, near expansive Marymoor park, haven to pet owners, joggers, and sports enthusiasts. Close to the highway and just a short drive away from major cities.');
INSERT INTO tbl_hotels (Id, Modified, IsDeleted, HotelName, Category, City, State, Description) VALUES (20, CURRENT_TIMESTAMP, 0, 'Delete Me Hotel', 'Unknown', 'Nowhere', 'XX', 'Test-case row for change detection and delete detection . For change detection, modify any value, and then re-run the indexer. For soft-delete, change IsDelete from zero to a one, and then re-run the indexer.');


-- Read
SELECT * FROM tbl_hotels;

-- Update (test for change detection)
UPDATE tbl_hotels SET Category = 'Test' WHERE Id = 20;
SELECT * FROM tbl_hotels;

-- Update (test for deletion detection)
UPDATE tbl_hotels SET IsDelete = 1 WHERE Id = 20;
SELECT * FROM tbl_hotels;

-- Delete
DELETE FROM tbl_hotels WHERE Id = 20;
SELECT * FROM tbl_hotels;