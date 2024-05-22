import zipfile

passw = "pass1"
zfile = zipfile.ZipFile("dat.zip")
try:
    zfile.extractall(pwd=passw.encode('utf-8'))
except Exception as error:
    print(error)