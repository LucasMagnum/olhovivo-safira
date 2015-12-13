package main

import (
    "fmt"
    "olhovivo/parse"
    "path/filepath"
)

var RESOURCES_FILE, _ = filepath.Abs("downloads/resources.json")

func main(){
    fmt.Println(RESOURCES_FILE)
    resources := parse.GroupByCategory(parse.ParseResources(RESOURCES_FILE))

    for category, totalYear := range resources {
        fmt.Printf("Categoria: %s, Total ano: %0.2f \n", category, totalYear)
    }

}
