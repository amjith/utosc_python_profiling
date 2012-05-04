SOURCE = profiling.rst
TEX = profiling.tex
OUTPUT = profiling.pdf
#TEX_PROG = /usr/texbin/pdflatex
PROG = ./rst2beamer.py
TEX_PROG = pdflatex
#VIEWER = open
VIEWER = evince

all:
	$(PROG) --codeblocks-use-pygments --overlaybullets='' $(SOURCE) $(TEX)
	$(TEX_PROG) $(TEX)
	$(VIEWER) $(OUTPUT)
