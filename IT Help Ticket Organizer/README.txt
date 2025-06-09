This Python script automates the process of classifying and triaging IT Help Tickets. 
Ex. "My laptop won't boot after the latest update" --> Hardware

Given a .csv file of customer submitted problem statements, this script categorizes these tickets
into their corresponding category of issue. This script outputs an overview of the number of tickets
in each issue category in the command terminal, as well as a separate categorized_tickets.csv file
containing an additional label next to each ticket entry containing the corresponding issue
category.

In the command terminal the user will be prompted to enter the complete file path to the .csv file
containing the ticket id, and description of the issue as collected by the ticketing software.
Ex. 1,My laptop won't boot after the latest update

Additionally, this script can be easily customized and scaled to accommodate integration with
various ticketing softwares, the classification of more issue categories, or to produce various
visualizations to monitor the current status of IT Help Tickets.

You can run this script on your own files, or you can use the tickets.csv file in the test_files
folder of this project.

Developed by Megan Kundra
