'''Bu ornek sub metodunun kullanilmasini gostermektedir.
Bu metod ile search and replace yapilabilir''' 
#!/usr/bin/python
import re

tarih = "29-10-1923 # bu onemli bir tarihtir"

# comment olan kisimlari sil
tarih = re.sub(r'#.*$', "", tarih)
print("Tarih : ", tarih)

# digitten farkli olan kisimlari sil
tarih = re.sub(r'\D', "", tarih)    
print("Tarih : ", tarih)
