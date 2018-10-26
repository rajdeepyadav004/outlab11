NAME = '170050034-170050094-170050096-outlab11'

all:
		tar -zcvf ${NAME}.tar.gz ${NAME}/P*/*.txt ${NAME}/P*/*.py
.PHONY: all
