TEXFILE = example

TEXFILE = example

$(TEXFILE).pdf: $(TEXFILE).tex
	knuth build $<

.PHONY: clean
clean:
	knuth clean

view: $(TEXFILE).pdf
	evince $<

