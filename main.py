import os, shutil
from dotenv import load_dotenv
from mega import Mega

def getAccount():
    mega = Mega()
    return mega.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

def createBackupDir(account): #TODO RETHINK
    paths = os.getenv('PATHS').split(';')
    folder = account.find('Backups', exclude_deleted=True)
    if folder is None:
        for path in paths:
            account.create_folder(f'Backups/{os.path.basename(path)}')
    return folder
            
# def compareSizes():
    # createZip()

def uploadZip(directory, account):
    folder = account.find('Backups', exclude_deleted=True)
    filename = os.path.basename(directory)
    shutil.make_archive(filename, 'zip')
    account.upload(f"{filename}.zip", folder[0])
    os.remove(f"{filename}.zip")

def main():
    load_dotenv()
    acc = getAccount()
    folder = acc.find('Backups', exclude_deleted=True)
    if folder:
        #compareSizes()
        pass
    else:
        acc.create_folder('Backups')
        paths = os.getenv('PATHS').split(';')
        for path in paths: 
            uploadZip(path, acc)

if __name__ == "__main__":
    main()