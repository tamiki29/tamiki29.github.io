# input: 
# - a csv file with city names and coordinates
# 
# output: 
# - a javascript block that creates city objects and lines that connect them 
#   (as in https://www.amcharts.com/demos/animations-along-lines/#code)
# 
# example usage: 
# awk -f csv2map.awk kimitravels.csv

BEGIN {
  FS=","
  lastlocation=""
  count=0
}

{
  sub(/\r/,"");
  if ( $0 ~ /^\/\// ) {
    print $0
  } else if ($0 ~ /^;/) {
    print ""
  } else {
    # print "\"" $1 "\"" " = " "\"" $2 "\";"
    print "var city_" count " = addCity({ \"latitude\": " $9 ", \"longitude\": " $10 " }, \"" $5  "\");"
    print "addLine(city_" count-1 ", city_" count ");"
    count++
  }
}
