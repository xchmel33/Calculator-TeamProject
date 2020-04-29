## @file Makefile
# @brief makefile for easy manipulating with program
# @date april 2020
#

.PHONY: all pack doc clean test run profile

#target all does not compile anything, but installs all necessary dependencies
all:
	sudo -H apt-get -y update
	sudo -H apt-get install python3.8
	sudo -H apt-get install python3.pip
	sudo -H pip3 install pyqt5==5.14

#pack project
pack: clean doc
	mkdir -p ../../xchmel33_xhurba03_xkrama06_xlisci01/doc
	mkdir -p ../../xchmel33_xhurba03_xkrama06_xlisci01/install
	mkdir -p ../../xchmel33_xhurba03_xkrama06_xlisci01/repo
	cp -a ../doc/* ../../xchmel33_xhurba03_xkrama06_xlisci01/doc
	cp -a ../installer/* ../../xchmel33_xhurba03_xkrama06_xlisci01/install
	cp -a ../* ../../xchmel33_xhurba03_xkrama06_xlisci01/repo
	rm -rf ../../xchmel33_xhurba03_xkrama06_xlisci01/repo/doc
	rm -rf ../../xchmel33_xhurba03_xkrama06_xlisci01/repo/installer
	cd ../.. && zip -r xchmel33_xhurba03_xkrama06_xlisci01.zip xchmel33_xhurba03_xkrama06_xlisci01

#generate doxygen documentation
doc:
	cd .. && rm -rf doc
	doxygen Doxyfile
	cd .. && mkdir doc
	mv latex ../doc
	mv html ../doc

#remove unnecessary files
clean:
	rm -rf __pycache__ ../doc

#run tests
test: test.py
	python3 -m unittest test.py

#run program
run: gui.py
	python3 gui.py

#run program for computing standard error of mean with implicit input file
profile: stddev.py
	python3 stddev.py < ../profiling/test1000values
