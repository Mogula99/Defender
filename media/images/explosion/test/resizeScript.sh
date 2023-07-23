#!/bin/bash

for x in {1..12}
do
	convert $x.png -resize 96x96 $x.png
done
