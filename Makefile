# Makefile using GNU make standard syntax

programs  := $(null)
documents := index.html

.PHONY: all
all: $(programs) $(documents)

%.html: %.markdown
	cat $< > $@
