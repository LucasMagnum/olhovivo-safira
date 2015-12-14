package parse_test

import (
    "fmt"
    "olhovivo/parse"
)

func ExampleParseResources(){
    fmt.Println(parse.ParseResources(RESOURCES_FILE))
    // Output: [{Assistência Social 1.372248e+06} {Saúde 150000} {Educação 38986.72} {Saúde 105310.37} {Encargos Especiais 13830.15} {Educação 103200} {Encargos Especiais 10784.46} {Assistência Social 112375}]
}


func ExampleGroupByCategory(){
    resources := parse.ParseResources(RESOURCES_FILE)
    fmt.Println(parse.GroupByCategory(resources))
    // Output: [{Assistência Social 1.484623e+06} {Saúde 255310.37} {Educação 142186.72} {Encargos Especiais 24614.61}]
}


func ExampleCleanValue(){
    fmt.Println(parse.CleanValue("127.000,54"))
    fmt.Println(parse.CleanValue("55.513,12"))

    // Output:
    // 127000.54 <nil>
    // 55513.12 <nil>
}
