from ftplib import FTP
from contextlib import contextmanager

@contextmanager
def ftp_connection(host, user, password):
    ftp = FTP(host)
    ftp.login(user, password)
    try:
        yield ftp
    finally:
        ftp.quit()

with ftp_connection('ftp.example.com', 'username', 'password') as ftp:
    # Perform FTP operations
    ftp.cwd('path/to/directory')
    files = ftp.nlst()
    print(files)