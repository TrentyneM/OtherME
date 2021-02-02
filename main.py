# Import Libraries
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Global Variables
weeklyClassBlockLetters = ""	# Weekly A/B Day Letters
scheduleDataVar = []			# Week Data is loaded into a referenceable List

# Time Variables
dateTimeVar = datetime.now()
todays_date = datetime.now()

# Index Variables
scheduleDataVarIndex = 0		# Index Locator for ScheduleDataVar
characterIndex = 1

# Repl.it Specific Arguments
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Web Driver
try:
	driver = webdriver.Chrome(options=chrome_options, executable_path="C:\chromedriver.exe")
except selenium.common.exceptions.WebDriverException:
	print("Chromedriver is Not Reachable, Please Restart.")

# My Student Info
studentID = 0 
studentEmail = "example@example.com"
studentPassword = "examplepassword" 	

# Startup Message
def applicationStart():
  print("Attendance Bot: 1.1\nCreated By: Trentyne Morgan\n")
  # Check for the Week Data
  weeklyDataRead()
  
# == A-Day Bot Navigation ===
# Period-1A
def firstPeriodMode():
   # Global Variables
   global studentID
   global studentEmail
   global studentPassword
   # Navigate to Microsoft Teams
   driver.get("https://teams.microsoft.com")
   # Login with Email and Password
   driver.find_element_by_id("i0116").send_keys(studentsEmail)
   time.sleep(2)
   driver.find_element_by_id("idSIButton9").send_keys(Keys.ENTER)  
   time.sleep(3)
   # Enter the Password on the second login form
   driver.find_element_by_id("passwordInput").send_keys(studentPassword)
   driver.find_element_by_id("submitButton").send_keys(Keys.ENTER)  
    
# Time Check A
def timeCheckA():
  # Global Variables
  global dateTimeVar
  # Time Stuff
  timeHour = (todays_date.hour)
  timeMinutes = (todays_date.minute)
  # ==Period 1A Detection==
  if timeHour == range(7,8):
     firstPeriodModeA() 
  # ==Period 2A Detection==
  if timeHour == range(8,10):
     secondPeriodModeA()
  # ==Period 3A Detection==
  if timeHour == range(10,12):
     thirdPeriodModeA()
  # ==Period 4A Detection==
  if timeHour == range(12,2):
     fourthPeriodModeA()
 
# If the Check the Current Day and Go to the Set for that Day1
def timeCheck():
  if (scheduleDataVar[scheduleDataVarIndex]) == "A":
    timeCheckA()
    if (ScheduleDataVar[scheduleDataVarIndex]) == "B":
      timeCheckB()

# Read Weekly Data
def weeklyDataRead():
	# Global Variables
	global WeeklyDataVar
	global weeklyDataFile
	global scheduleDataVarIndex
	global characterIndex
	# Check if the Week Data Is Present
	try:
		# Open the file just once and then close it to check if the file is there
		weeklyDataFile = open("weekdata.txt")
		weeklyDataFile.close()
		# Load Week Data into Schedule Variable and Check the Time
		weeklyDataFile = open("weekdata.txt", "r")
		for x in range(1,5):
			scheduleDataVar.insert(ScheduleDataVarIndex, weeklyDataFile.read(CharacterIndex))
			# Increment The Index Locator Values
			scheduleDataVarIndex += 1
			CharacterIndex += 1
		# If the maximum characters are read, Check the Time and Determine which meeting to join.
		if CharacterIndex == "5":
		   print("Schedule Routine Loaded.")
		   timeCheck()	     
	# Throw an error if not present and redirect user to create a new week data file
	except IOError:
		print("Error: Week Data File Not Present. Creating a New One.")
	finally:
		classLetterWeekPrompt()
	
# Ask for Student A/B Week List
def classLetterWeekPrompt():
	# Global Variables
	global weeklyClassBlockLetters
	# We're going to use the letter data to determine which class to go to
	weeklyClassBlockLetters = input("Enter Each Letter of the Week  (example: ABAAB): >")
	# Save the input into a file (If it doesn't already exist, create one.)
	weeklyDataFile = open('weekdata.txt', 'w')
	weeklyDataFile.write(weeklyClassBlockLetters)
	# Close the File and Read it Again .
	weeklyDataFile.close()
	print("Week Data File Saved.")
	weeklyDataRead()
    
# App Run
applicationStart()
	
