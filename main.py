import os, shutil
from dotenv import load_dotenv
from mega import Mega

def getAccount():
    mega = Mega()
    return mega.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

def compareSizes(path, account):
    print("Comparing sizes")
    filename = os.path.basename(path)
    createZip(path)
    if account.find(f"{filename}.zip") is None or account.find(f"{filename}.zip")[1]["s"] != os.stat(f"{filename}.zip").st_size:
        uploadZip(path, account)
    removeZip(path)

def createZip(path):
    shutil.make_archive(os.path.basename(path), 'zip')
    print("Created zip locally")

def removeZip(path):
    os.remove(f"{os.path.basename(path)}.zip")
    print("Removed zip locally")

def uploadZip(path, account):
    filename = os.path.basename(path) 
    folder = account.find('Backups', exclude_deleted=True)
    old = account.find(f'Backups/{filename}.zip', exclude_deleted=True)
    if old:
        older = account.find(f'Backups/{filename}_old.zip', exclude_deleted=True)
        if older:
            account.destroy(older[0])
            print("Deleted old backup")
        account.rename(old, f'{filename}_old.zip')
        print("Created old backup")
    try:
        account.upload(f"{filename}.zip", folder[0])
        print("Uploaded zip to mega")
    except:
        print("Something went wrong. Do you have enough space available on mega?")

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