# Vocabulary-Enrichment
Project report for Vocabulary Enrichment

This Python script displays a "Word of the Day" notification on your Windows desktop, helping you build your vocabulary in a fun and consistent way.

📌 Features
i. Automatically picks words based on today's date
ii. Selects a random word that starts with the daily letter
iii. Fetches words and meanings from a local JSON dictionary
iv. Displays a beautiful Windows toast notification every 15 seconds
v. Includes a notification sound and optional icon (wod.png)

 How It Works:-
-> The day of the month (1–31) maps to a letter (1 → a, 2 → b, ..., 26 → z, wraps around for 27–31).
-> A .json file (dictionary.json) contains words and their meanings.
-> From all words starting with the selected letter, one is randomly picked and shown via the winotify library.
-> A loop sends this notification every 15 seconds (for demo purposes; can be changed).
