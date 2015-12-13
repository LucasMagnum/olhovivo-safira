package parse_test

import (
    "fmt"
    "olhovivo/parse"
    "path/filepath"
    "testing"
)

var RESOURCES_FILE, _ = filepath.Abs("fixtures/resources.json")


func TestParseResources(t *testing.T){
    t.Log("ParseResources first item should be 'Assistência Social'")

    resources := parse.ParseResources(RESOURCES_FILE)
    resource := resources[0]

    if resource.Category != "Assistência Social" {
        t.Error("Expected Assistência Social")
    }

    if resource.TotalYear != 1372248.00 {
        t.Error("Total year is incorrect")
    }

}


func TestParseResourcesReturnsAllResources(t *testing.T) {
    t.Log("ParseResources should return 8 resources from file")

    resources := parse.ParseResources(RESOURCES_FILE)

    if resourcesLength := len(resources); resourcesLength != 8 {
        if resourcesLength > 8 {
            t.Error("Parsed more resources than necessary")
        } else {
            t.Error("Missing resources values")
        }
    }
}



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



func ExampleParseResources(){
    fmt.Println(parse.ParseResources(RESOURCES_FILE))
    // Output: [{Assistência Social 1.372248e+06} {Saúde 150000} {Educação 38986.72} {Saúde 105310.37} {Encargos Especiais 13830.15} {Educação 103200} {Encargos Especiais 10784.46} {Assistência Social 112375}]

}


func ExampleGroupByCategory(){
    resources := parse.ParseResources(RESOURCES_FILE)

    fmt.Println(parse.GroupByCategory(resources))
    // Output: map[Assistência Social:1.484623e+06 Saúde:255310.37 Educação:142186.72 Encargos Especiais:24614.61]
}


func ExampleCleanValue(){
    fmt.Println(parse.CleanValue("127.000,54"))
    fmt.Println(parse.CleanValue("55.513,12"))

    // Output:
    // 127000.54 <nil>
    // 55513.12 <nil>
}
