.PHONY: docs

docs:
	rm -rf docs
	cd myDocs && make clean html
	mv myDocs/build/html docs
	touch docs/.nojekyll

