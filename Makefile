clean: FILES=$(shell find -path "*~")
clean:
	[ "$(FILES)" != "" ] && rm -f $(FILES)
