all: mpl.png dropout1.png dropout2.png dropout3.png

mpl.dot: dotgen.py
	python dotgen.py > mpl.dot

mpl.svg: mpl.dot
	dot -Tsvg -ompl.svg mpl.dot

mpl.png: mpl.svg
	convert mpl.svg mpl.png

dropout1.dot: dotgen_dropout.py
	python dotgen_dropout.py

dropout2.dot: dotgen_dropout.py
	python dotgen_dropout.py

dropout3.dot: dotgen_dropout.py
	python dotgen_dropout.py

dropout1.png: dropout1.dot
	dot -Tsvg -odropout1.svg dropout1.dot
	convert dropout1.dot dropout1.png

dropout2.png: dropout2.dot
	dot -Tsvg -odropout2.svg dropout.dot
	convert dropout2.dot dropout2.png

dropout3.png: dropout3.dot
	dot -Tsvg -odropout3.svg dropout3.dot
	convert dropout3.dot dropout3.png

clean:
	\rm -rf mpl.png mpl.svg mpl.dot dropout?.png dropout?.dot dropout?.svg
