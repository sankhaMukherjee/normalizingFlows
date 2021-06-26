.PHONY: docs

docs:
	rm -rf docs
	cd myDocs && make clean html
	mv myDocs/build/html docs
	touch docs/.nojekyll

pushdocs:
	git add .
	git commit -m 'updated documentation'
	git push origin master

run:
	python3 src/examples/banana-npy.py