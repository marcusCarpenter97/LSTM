#!/bin/bash
mv /mnt/c/Users/mc844/OneDrive\ -\ University\ of\ Exeter/Project/Literature/*.txt ~
mv /mnt/c/Users/mc844/OneDrive\ -\ University\ of\ Exeter/Project/Literature/Read/*.txt ~
mv /mnt/c/Users/mc844/OneDrive\ -\ University\ of\ Exeter/Project/Literature/To\ read/*.txt ~

#for f in *.pdf; do
#  #xapers scandoc $f | head -n1
#  id=`xapers scandoc $f | head -n1`
#  echo $f $id
#  if [ ! -z "$id" ];
#  then
#	  url="http://dx.doi.org/"$id
#	  echo "`curl -LH 'Accept: application/x-bibtex' $url`"$'\n' >> bibfile.txt
#  fi
#done
