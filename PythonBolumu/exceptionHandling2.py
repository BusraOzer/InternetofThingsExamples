import sys

try:
    f = open('regexTest1')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Data integer'a cevrilemedi.")
except:
    print("Beklenilmeyen bir hata olustu:", sys.exc_info()[0])
    raise
