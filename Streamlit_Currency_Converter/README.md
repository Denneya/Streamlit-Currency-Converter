# FX Convertor

## Author
Name: Denneya Muscat
Student ID: 24418042

## Description
### Application Description
This application is a currency converter, which uses an open-source API called Frankfurter. Frankfurter is able to retrieve current and historical foreign exchange rates dating back to 4 January 1999.

The application takes an input amount from the user and allows them to choose the currency they wish to convert from and to. The user can then click a button to retrieve the conversion on the day of use, or they can choose a specific date and retrieve the historical conversion.

Not only does the application provide the converted amount, it also supplies the conversion rate and the inverse rate, which would lead the user back to their original amount and currency.

### Challenges Faced
Beginning this task was really difficult as I tried to complete the code for all four files and then run the Streamlit app.py file. There were so many misleading errors I didn't know where to begin. I also found it difficult to research how to attack this assignment as a lot of the videos I watched only used one file to create the app.

I attempted this task five times. The last version I decided to do everything within the app.py file to make sure the API worked, then the functions were defined correctly. I then moved these features one step at a time to the api.py and frankfurter.py files. Not only did this allow me to identify errors in each part of the script, but I learnt so much and began to understand why the errors were occurring and what was required to fix them. By the end of the task my coding skills had improved immensely and I was able to put some attention into the aesthetics of the app.

I also found I had to really think about the purpose of each file and where certain variables had to be assigned for the functions to run. I did deter slightly from the instructions provided in the files as I felt my method would allow for a smoother transition into the next file. This is evident in the currency.py file where I defined an extra format function for the historical conversion.

### Future Features
I had watched some YouTube videos on creating currency conversion apps in Streamlit and I saw some people adding graphics and images. I would like to change the layout of the app and create columns for the from and to currencies, with a graphic in between.

I would also like to present the list of available currencies in a nicer format, possibly a table.

## How to Setup
### Setting up the Environment
1. First, all applications need to be downloaded in order to create and edit python scripts in macos. The easiest way to do this is by downloading Visual Studio Code.
2. Import the folder with required python scripts. Open a script and go to the top right hand corner. Click "Run Python in Dedicated Terminal".
3. The terminal will open and your username should appear with a $. Click next to the $ and type "python -m venv venv".
4. A prompt asking if you want to select a new virtual environment for the workspace folder will appear. Click Yes.
5. Install the required packages to run each script.

### Python Version
The python version used was 3.10.8

### Packages Used
The packages required for the four scripts and the versions used were:
- Streamlit, version 1.27.0
- requests, version 2.28.1

## How to Run the Program
1. After the environment has been set up, it is important to install the two required packages within this environment. In the terminal, after the $, type "pip install streamlit". 
2. Once that has loaded, install the requests package by typing "pip install requests" after the $.
3. In the terminal, after the $, type "streamlit run app.py". After a few moments, a webpage should open
automatically.
4. Enter in the amount you wish to convert. If you don't enter in an amount a message will appear 
"Please enter the amount you wish to convert".
5. A list of available currencies will appear automatically. 
6. Choose the currency you wish to convert from and the currency you wish to convert to.
7. Click "Get Latest Rate" button for the current conversion rate and converted amount.
8. If you want a conversion from a past date, select the date required from the "Select Date" bar.
9. Click "Get Historical Rate" button for the conversion rate and converted amount for the selected date.

## Project Structure
api.py - This file is used to call the Frankfurter API. It is linked directly to the frankfurter.py file.

frankfurter.py - This file defines three functions, which either retrieve the latest currency codes and rates and the historical currency codes and rates. The frankfurter.py file provides the url's to retrieve these available lists of currencies and rates. This file links to both currency.py and app.py files and calls from the api.py file.

currency.py - This file takes the functions defined in the frankfurter.py file. It defines four functions. The first rounds the conversion rate to 4 decimal places. The second function uses the rounding function and takes the inverse of it. The last two functions perform the same role, formatting the sentence output, only the first format function is used for the latest conversions and the second format function is for the historical conversions. This file is linked directly to the app.py file and calls from the frankfurter.py file.

app.py - This file is used to communicate to the streamlit app. This is where headings, buttons, selectboxes, sidebars and input fields are created. This file calls from both currency.py and frankfurter.py files, depending on which function is required.

config.toml - This file was created and used to change the theme of the streamlit app.

## Citations

Frankfurter API (API retrieval) - https://www.frankfurter.app/docs/
Streamlit Library (streamlit commands) - https://docs.streamlit.io/library
Pythonology (intro to building currency converter in streamlit) - https://www.youtube.com/watch?v=BqetGHXQ-Q0
W3 Schools (creating functions in python) - https://www.w3schools.com/python/python_functions.asp
Geeks for Geeks (calling a function within another function) - https://www.geeksforgeeks.org/python-call-function-from-another-function/
Career Karma (assist with errors) - https://careerkarma.com/blog/python-local-variable-referenced-before-assignment/#:~:text=The%20UnboundLocalError%3A%20local%20variable%20referenced,you%20assign%20it%20a%20value.
Lab Exercises (particularly lab 4 exercises 1 & 2)