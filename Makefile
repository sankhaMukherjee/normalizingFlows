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

banana:
	python3 src/examples/banana-npy.py

planarFlowTarget:
	python3 src/examples/planarFlows/target.py

run:
	python3 src/examples/planarFlows/experiment.py