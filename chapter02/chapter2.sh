#10
wc -l hightemp.txt
#11
cat hightemp.txt | tr '\t' ' '
#12
cut -f 1 hightemp.txt > col1.txt
cut -f 2 hightemp.txt > col2.txt
#13
paste col1.txt col2.txt
#14
head -n10 hightemp.txt
#15
tail -n10 hightemp.txt
#16
split -l5 hightemp.txt
#17
sort -u col1.txt
#18
sort -r -k3 hightemp.txt
#19

