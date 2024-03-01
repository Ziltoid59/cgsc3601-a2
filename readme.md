To run this code, do the following:

# macOS
1) Download the code from Brightspace
2) Move the downloaded folder to your desktop
3) Make sure the folder is named A2
3) Open your Terminal app and type the following:

```bash
cd Desktop/A2
```
4) Create a new virtual enviornment by running the following command in your Terminal app

```bash
python3 -m venv venv
```

5) Activate your virtual enviornment by running the following command in your Terminal app
```bash
source venv/bin/activate
```
6) Install the assignment into your newly create virtual enviornment
```bash
pip install ./a2
```
7) Next, we are going to run the run_me.py file by running the following command in your Terminal app
```bash
python3 run_me.py
```
8) This will prompt you to enter the full path to the folder that contains your .txt review files
9) Entering this path will run the NLP code and save a file called "results.csv" in your A2 folder
10) Use this csv file to do your analyses in Weka