from ftplib import FTP_TLS


def ftp_send(login, ftppswd, filename):
    ftp = FTP_TLS('ftp.zak.lodz.pl', login, ftppswd)
    ftp.prot_p()
    # ftp.cwd('SRZAK/postanowienia/kolegium/' + filename[:4])
    file = open(filename, 'rb')
    ftp.storbinary('STOR ' + filename, file)
    print(ftp.retrlines('LIST'))  # list directory contents
    file.close()  # close file and FTP
    ftp.quit()
