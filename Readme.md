## Automatic Backup Script - Readme

This project is a Python script that archives specified locations on your computer and sends them to a web hosting service as backups. The backups are stored as zip files with names corresponding to the location archived (e.g., `desktop.zip`, `downloads.zip`).

You can use Windows task scheduler to execute this script every night. You can follow the steps outlined below:

### Step 1: Prerequisites

1. Make sure you have Python installed on your Windows machine. 

### Step 2: Set up the Environment

1. Clone the repository
```git clone https://github.com/Gruzjan/backup.git```

2. Download the required Python packages by running the following command in your command prompt or terminal:
```pip install -r requirements.txt```

3. Remove `.example` from your `.env` and adjust it to your needs. Note the backslashes and semicolons to seperate multiple paths:
```
LOGIN = your_mega_login
PASSWORD = your_mega_password
PATHS = your_path_1;your_path_2
```

### Step 3: Schedule the Script Execution

To schedule the script to run automatically at 2 am every day, you can use the Windows Task Scheduler.

1. Open the Task Scheduler by pressing `Win + R` and typing `taskschd.msc`.

2. Click on "Create Basic Task" in the "Actions" pane on the right.

3. Provide a name and description for the task (e.g., "Backup Script").

4. Choose "Daily" as the trigger and set the recurring frequency to "1" day. Select the desired start date and set the start time to "2:00 AM". Click "Next".

5. Choose "Start a program" as the action and browse to select the Python executable (`python.exe`). If you installed Python in the default location, the path should be something like `C:\Python39\python.exe`. In the "Add arguments" field, enter the path to the `backup_script.py` file. Click "Next".

6. Review the task summary and click "Finish" to create the scheduled task.

The script will now be executed automatically every day at 2 am, and the specified locations will be backed up to your Mega account.

Feel free to customize the script and the scheduled task settings according to your requirements :))
