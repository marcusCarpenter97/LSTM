#!/bin/bash

for f in *.txt; do
	sed -i.bak '/</d' ./$f
	sed -i.bak '/>/d' ./$f
	sed -i.bak '/DOI resolution requires both the prefix and the suffix./d'
	awk 'NF' $f > $f.done
done
