clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

save-resources:
	scrapy crawl resources -o ../downloads/resources.json

install:
	pip install -r requirements.txt
