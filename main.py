import os, shutil
from dotenv import load_dotenv
from mega import Mega

def getAccount():
    mega = Mega()
    return mega.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

def compareSizes(path, account):
    filename = os.path.basename(path)
    createZip(path)
    if account.find(f"{filename}.zip") is None or account.find(f"{filename}.zip")[1]["s"] != os.stat(f"{filename}.zip").st_size:
        uploadZip(path, account)
    removeZip(path)

def createZip(path):
    shutil.make_archive(os.path.basename(path), 'zip')

def removeZip(path):
    os.remove(f"{os.path.basename(path)}.zip")

def uploadZip(path, account):
    #TODO: Handle old backups
    folder = account.find('Backups', exclude_deleted=True)
    filename = os.path.basename(path) 
    account.upload(f"{filename}.zip", folder[0])

def main():
    load_dotenv()
    acc = getAccount()
    paths = os.getenv('PATHS').split(';')
    folder = acc.find('Backups', exclude_deleted=True)
    if folder:
        for path in paths: 
            compareSizes(path, acc)
    else:
        acc.create_folder('Backups')
        for path in paths:
            createZip(path)
            uploadZip(path, acc)
            removeZip(path)

if __name__ == "__main__":
    main()