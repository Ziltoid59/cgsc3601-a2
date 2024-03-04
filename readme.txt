To run this code, do the following:

# macOS
1) Download the code from Brightspace
2) Move the downloaded folder to your desktop
3) Make sure the folder is named A2
4) Open your Terminal app and type the following:

cd Desktop/A2

5) Create a new virtual enviornment by running the following command in your Terminal app

python3 -m venv venv

6) Activate your virtual enviornment by running the following command in your Terminal app

source venv/bin/activate

7) Install the assignment into your newly create virtual enviornment

pip install ./a2

8) Install the required corpora

python3 -m textblob.download_corpora

9) Next, we are going to run the run_me.py file by running the following command in your Terminal app

python3 run_me.py

10) This will prompt you to enter the full path to the folder that contains your .txt review files. If you do not know 
how to get the full path to your folder, please consult [the internet](https://macpaw.com/how-to/copy-file-path-mac#:~:text=Control%2Dclick%20or%20right%2Dclick%20on%20the%20file%20in%20Finder,path%20wherever%20you%20need%20it).
11) Entering this path will run the NLP code and save a file called "results.csv" in your review folder
12) Use this csv file to do your analyses in Weka

# Windows
1) Download the code from Brightspace
2) Move the downloaded folder to your desktop
3) Make sure the folder is named A2
4) Open your Command Prompt app and type the following:

cd Desktop\A2

5) Create a new virtual enviornment by running the following command in your Command Prompt app

python -m venv venv

6) Activate your virtual enviornment by running the following command in your Command Prompt app

venv\Scripts\activate.bat

7) Install the assignment into your newly create virtual enviornment

pip install ./a2

8) Install the required corpora

python -m textblob.download_corpora

9) Next, we are going to run the run_me.py file by running the following command in your Command Prompt app

python run_me.py

10) This will prompt you to enter the full path to the folder that contains your .txt review files. If you do not know 
how to get the full path to your folder, please consult [the internet](https://www.howtogeek.com/670447/how-to-copy-the-full-path-of-a-file-on-windows-10/).
11) Entering this path will run the NLP code and save a file called "results.csv" in your review folder
12) Use this csv file to do your analyses in Weka
