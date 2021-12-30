import os
import shutil
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=writeMode('overwrite'))
        
def main():
    access_token = 'sl.A5TdktkIPsxFMlyxhFSMBI7XdyHoIp3ZTZfjplbi9HhnCiZFf28-8axUIGOCi4kik85a4m2AWiWdNkaaiHCsHN-DmCo4J-2FfmA-LBA_CdorKnHGbvbVRAMMkauVDmsUKOFkzjsWMJHZ'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    file_to = input("Enter the Name of the File in dropbox: ")


TransferData.upload_file(file_from, file_to)
print("The file has been moved.")

main()
