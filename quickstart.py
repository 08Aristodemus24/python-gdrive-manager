from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import sys


class FileOperations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def list_files(drive, is_structured=False) -> str | list:
        # Auto-iterate through all files that matches this query
        files = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        stringified_files = ""
        for file in files:
            stringified_files += "title: {}, id: {}\n".format(file['title'], file['id'])
            
        return stringified_files if is_structured == True else files

    @staticmethod
    def upload_file(drive) -> None:
        folder = drive.CreateFile({
            'title': 'Project Solzhenitsyn',
            'mimeType': 'application/vnd.google-apps.folder'
        })

        folder.Upload()
        
        file = drive.CreateFile({'parents': [{'id': folder['id']}]})
        file.SetContentFile('D:/MIG/samples.txt')
        file.Upload()

        # goal is to create a file 
        # and then use self.SetContentFile(path of your file to be uploaded)    
        # self.CreateFile(  )
    
    @staticmethod
    def delete_file():
        pass

if __name__ == "__main__":
    gauth = GoogleAuth()

    # Creates local webserver and auto handles authentication.
    gauth.LocalWebserverAuth() 

    drive = GoogleDrive(gauth)
    # FileOperations.upload_file(drive)

    # list all files given absolute path
    print(sys.argv)
    abs_path = sys.argv[1]
    # # for file in os.listdir(abs_path):
    # #     print(file, end='\n')

    # use os.walk to recursively scan and return all the files of the tree of the directory
    for root, sub_dirs, files in os.walk(abs_path):
        print(root)
        # print('--\nroot = ' + root)

        # for sub_dir in sub_dirs:
        #     print('\t- subdirectory ' + sub_dir)

        # for file in files:
        #     file_path = os.path.join(root, file)

        #     print('\t- file %s (full path: %s)' % (file, file_path))
    


    