f="${1%.*}.tex"
echo '\documentclass{article}' > $f
echo '\title{A rational music piece}' >> $f
echo '\author{A rational music composer}' >> $f
echo '\include{amsmath}' >> $f
echo '\begin{document}' >> $f
echo '\maketitle' >> $f
cat $1 | python elr2tex.py >> $f
echo '\end{document}' >> $f
#latexmk -dvi -c $f
pdflatex $f
xdg-open "${1%.*}.pdf"
rm $f
