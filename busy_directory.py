#!/usr/bin/env python3
import asyncio
from ftplib import FTP

ftp_host = "127.0.0.1"
ftp_user = "ftpuser"
ftp_password = "1"

source_ftp_directory = "files"
destination = "/home/mshahbazi/os_dir"

class FTPConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.ftp = None

    def __enter__(self):
        self.ftp = FTP(self.host)
        self.ftp.login(user=self.user, passwd=self.password)
        return self.ftp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ftp.quit()


with FTPConnection(ftp_host, ftp_user, ftp_password) as ftp:
    subdirectories = []
    ftp.cwd(source_ftp_directory)
    for i in range(10):
        subdirectory = f"subdirectory_{i}"
        ftp.mkd(subdirectory)
        subdirectories.append(subdirectory)
    
    file_list = ftp.nlst()
    for file_name in file_list:
        subdirectory = subdirectories[
            hash(file_name) % 10
        ]
        try:
            ftp.rename(file_name, f"{subdirectory}/{file_name}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

async def move_subdirectory(subdirectory):
    process = await asyncio.create_subprocess_exec(
        "rclone",
        "move",
        subdirectory,
        destination,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, _ = await process.communicate()


async def main():
    tasks = [move_subdirectory(subdirectory) for subdirectory in subdirectories]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
