#!/bin/bash

now=$(date +%Y%m%d-%H0000 -d  "1 hour ago")

echo "$now.log sikistiriliyor"
tar -czvf "20160926-070000.log.tar.gz" "20160926-070000.log"
#scp ile dosya gondermeyi otomatiklestirmek icin
#1-authentication key olustur
#ssh-keygen -t rsa
#2-ssh ile kars@kars-SATELLITE-C640 uzerinde ~/.ssh dosyasi olustur 
#pi@raspberry:~> ssh kars@kars-SATELLITE-C640 mkdir -p .ssh
#3-yeni public key kars'a ekle
#pi@raspberry:~> cat .ssh/id_rsa.pub | ssh kars@kars-SATELLITE-C640 'cat >> .ssh/authorized_keys'
#4-ssh ile test et
#pi@raspberry:~>ssh kars@kars-SATELLITE-C640

scp 
