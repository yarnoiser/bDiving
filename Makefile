.PHONY: clean rmpycache

rmpycache:
	$(RM) -r __pycache__

clean: rmpycache
	$(RM) *.blend1
