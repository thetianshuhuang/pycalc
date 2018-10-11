ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

install:
	echo "alias pycalc='python3 -i \"$(ROOT_DIR)/pycalc.py\"'" >> ~/.bashrc

install-py2:
	echo "alias pycalc='python -i \"$(ROOT_DIR)/pycalc.py\"'" >> ~/.bashrc
