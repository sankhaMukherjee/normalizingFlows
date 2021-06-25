.PHONY: docs

docs:
	rm -rf docs
	cd myDocs && make clean html
	mv myDocs/build/html docs
	touch docs/.nojekyll

run:
	python3 src/examples/banana-npy.py