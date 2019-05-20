#/bin/bash

images=(
bicubic.jpg
blotched2.jpg
smashed2.jpg
chinoiseries.JPG
rainbow.jpg
Sigma.jpg
linea.jpg
4x4.jpg
libellule_et_papillons.jpg
notte6.jpg
Spring.jpg
)


cd ../images
for i in "${images[@]}"; 
do
	# terrible syntax!!
	# https://stackoverflow.com/a/2664746 
	s=${i##*/}
	BASE=${s%.jpg}
	convert $i -resize 500 ${BASE}-small.jpg 
done
