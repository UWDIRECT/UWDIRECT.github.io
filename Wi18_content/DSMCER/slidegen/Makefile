all: mpl.png

mpl.dot: dotgen.py
	python dotgen.py > mpl.dot

mpl.svg: mpl.dot
	dot -Tsvg -ompl.svg mpl.dot

mpl.png: mpl.svg
	convert mpl.svg mpl.png

clean:
	\rm -rf mpl.png mpl.svg mpl.dot
