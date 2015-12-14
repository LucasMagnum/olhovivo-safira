package parse_test

import (
    "olhovivo/parse"
    "testing"
)


func BenchmarkParseResources(b *testing.B){
    for i := 0; i < b.N; i++ {
        parse.ParseResources(RESOURCES_FILE)
    }
}

func BenchmarkGroupByCategory(b *testing.B){
    resources := parse.ParseResources(RESOURCES_FILE)

    for i := 0; i < b.N; i++ {
        parse.GroupByCategory(resources)
    }
}
