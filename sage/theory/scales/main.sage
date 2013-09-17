load "pureTones.sage"
load "equalApprox.sage"

#pList = getPureTones(0) + getEqualApprox(51, 1) + getEqualApprox(31, 2) + getEqualApprox(12, 3)
g = plot(getPureTones(0), legend_label='Ptolemaic scale')
h = plot(getEqualApprox(12, 3), legend_label='12 tone equally tempered scale')
(g+h).save('/home/chiel/Projects/Thesis/figures/equally_temperedness.png', figsize=[8, 1])
