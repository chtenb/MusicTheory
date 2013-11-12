cat $1 | python3 ./elr2csound.py > score.sco
csound ./orchestra.orc ./score.sco
