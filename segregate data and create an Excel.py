import pandas as pd

# Sample data
data = [
    {"text": "My HP printer keeps jamming", "user": "user1", "timestamp": "2022-01-01 10:00:00", "sentiment": "complaint"},
    {"text": "I love my new HP printer", "user": "user2", "timestamp": "2022-01-02 11:00:00", "sentiment": "appreciation"},
    {"text": "HP printer wifi setup is a nightmare", "user": "user3", "timestamp": "2022-01-03 12:00:00", "sentiment": "complaint"},
    {"text": "My HP printer is working great", "user": "user4", "timestamp": "2022-01-04 13:00:00", "sentiment": "appreciation"},
    {"text": "HP printer ink is too expensive", "user": "user5", "timestamp": "2022-01-05 14:00:00", "sentiment": "complaint"}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Segregate the data based on sentiment
complaints = df[df["sentiment"] == "complaint"]
appreciations = df[df["sentiment"] == "appreciation"]

# Create an Excel writer object
writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")

# Write the data to separate sheets in the Excel file
complaints.to_excel(writer, sheet_name="Complaints")
appreciations.to_excel(writer, sheet_name="Appreciations")

# Save the Excel file
writer.save()
