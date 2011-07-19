echo "<gpx xmlns='http://www.topografix.com/GPX/1/1'></gpx>" > all.tmp

find . -name "*.gpx" -exec gpsbabel -t -i gpx -f all.tmp -f {} -o gpx -F all.tmp \;

mv all.tmp all.gpx