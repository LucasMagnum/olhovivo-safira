clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	rm *.json
	rm olhovivo

docs:
	gnome-open http://127.0.0.1:6060/pkg/olhovivo/
	godoc --http=:6060 --play=true -v=true

run:
	go run main.go

save-resources:
	scrapy crawl resources -o downloads/resources.json

setup:
	sudo apt-get install golang-go
	sudo apt-get install golang-go.tools

test:
	go test olhovivo/ olhovivo/parse

test-benchmark:
	go test olhovivo/parse olhovivo/ -bench=.
