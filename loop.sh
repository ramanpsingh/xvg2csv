for FILE in *.xvg; do
	sed -i '/^#\|^@/d' $FILE
	python3 xvg2csv.py -file $FILE -cw 2
done
paste -d , *.csv > merged.csv

mkdir csv
mv *.csv csv/
mkdir xlsx
mv *.xlsx xlsx/
