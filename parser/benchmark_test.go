package parser_test

import (
    "olhovivo/parser"
    "testing"
)


func BenchmarkParseResources(b *testing.B){
    for i := 0; i < b.N; i++ {
        parser.ParseResources(RESOURCES_FILE)
    }
}

func BenchmarkGroupByCategory(b *testing.B){
    resources := parser.ParseResources(RESOURCES_FILE)

    for i := 0; i < b.N; i++ {
        parser.GroupByCategory(resources)
    }
}
