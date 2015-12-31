GO_TEST=go test olhovivo/ olhovivo/parser olhovivo/api -v

clean:
	rm olhovivo
	go clean

docs:
	gnome-open http://127.0.0.1:6060/pkg/olhovivo/
	godoc --http=:6060 --play=true -v=true

run:
	go install olhovivo/parser
	go install olhovivo/api
	go run main.go

save-resources:
	scrapy crawl resources -o downloads/resources.json

setup:
	sudo apt-get install golang-go
	sudo apt-get install golang-go.tools

test:
	$(GO_TEST)

test-benchmark:
	$(GO_TEST) -bench=.
