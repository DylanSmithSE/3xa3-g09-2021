docs:
	doxygen configFile
	cd latex && $(MAKE)

app:
	python main.py 

tests:
	pytest 

coverage:
	pytest --cov-report term-missing --cov=board --cov=piece 

clean:
	rm -rf html
	rm -rf latex
