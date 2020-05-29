clear
clc

%import data dengan menggunakan low level i/o
filename = 'molekul.txt';
fid = fopen(filename,'r');

kalimat = fgetl(fid);

fclose(fid);