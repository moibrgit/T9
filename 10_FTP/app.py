import os 
import json
from ftplib import FTP
from pathlib import Path 
os.chdir(Path(__file__).parent)



# Read JSON
with open("./ftp.json", mode = "r", encoding="UTF-8") as file:
    content = file.read()
    cred = json.loads(content)
    
    


# Connection Data
FTP_SERVER = cred["server_name"]
FTP_USERNAME = cred["username"]
FTP_PASSWORD = cred["password"]
FTP_DIR = cred["dir_name"]


# Create FTP Client Connection
ftp = FTP(FTP_SERVER)

# Login into FTP Server
ftp.login(FTP_USERNAME, FTP_PASSWORD)


# Change Directory in FTP Server
ftp.cwd(FTP_DIR)
    


def upload_file():
    # Define the name of the file to upload
    file_to_upload = "file_to_upload.txt"
    
    # UPLOAD
    ftp.storbinary("STOR " + file_to_upload, open(file_to_upload, "rb")) 
    
    # Confirm
    print(("Uploaded Successfully..!"))


def download_files():
    # list of files and folders
    files = ftp.nlst()
    
    for file in files:
        # print(file)
        
        # Check if the file has an extension
        root, ext = os.path.splitext(file)
        
        if ext: # check if there is an extension
            print("Downloading:", file)
            
            # Start a local container
            local_file = open(root + "_downloaded" + ext, mode= "wb")
            
            # FTP Protocol -> RETREIVE
            ftp.retrbinary("RETR " + file, local_file.write )
    
            # Close the local file
            local_file.close()

def main():
    # upload_file() 
    download_files()



if __name__ == "__main__":
    main()


