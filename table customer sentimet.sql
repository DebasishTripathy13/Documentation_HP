-- Create a table to store customer sentiments about HP printers
CREATE TABLE hp_printer_sentiments (
    id SERIAL PRIMARY KEY,
    text TEXT,
    user_name TEXT,
    timestamp TIMESTAMP,
    sentiment TEXT,
    printer_model TEXT
);

-- Insert sample data
INSERT INTO hp_printer_sentiments (text, user_name, timestamp, sentiment, printer_model)
VALUES
    ('My HP printer keeps jamming', 'user1', '2022-01-01 10:00:00', 'complaint', 'OfficeJet Pro 9015e'),
    ('I love my new HP printer', 'user2', '2022-01-02 11:00:00', 'appreciation', 'ENVY Pro 6455'),
    ('HP printer wifi setup is a nightmare', 'user3', '2022-01-03 12:00:00', 'complaint', 'LaserJet Pro MFP M148fdw'),
    ('My HP printer is working great', 'user4', '2022-01-04 13:00:00', 'appreciation', 'DeskJet 3755'),
    ('HP printer ink is too expensive', 'user5', '2022-01-05 14:00:00', 'complaint', 'OfficeJet Pro 9025e');

-- Query to retrieve all posts talking about wifi issue in any HP printer model
SELECT * FROM hp_printer_sentiments WHERE sentiment = 'complaint' AND text LIKE '%wifi%' ORDER BY timestamp DESC;
