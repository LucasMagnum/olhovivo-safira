package parser_test

import (
    "olhovivo/parser"
    "path/filepath"
    "testing"
)

var RESOURCES_FILE, _ = filepath.Abs("fixtures/resources.json")


func TestParseResources(t *testing.T){
    t.Log("ParseResources first item should be 'Assistência Social'")

    resources := parser.ParseResources(RESOURCES_FILE)
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

    resources := parser.ParseResources(RESOURCES_FILE)

    if resourcesLength := len(resources); resourcesLength != 8 {
        if resourcesLength > 8 {
            t.Error("Parsed more resources than necessary")
        } else {
            t.Error("Missing resources values")
        }
    }
}


func TestGroupByCategoryReturns(t *testing.T) {
    t.Log("GroupByCategory returns a map with category and total year value")

    resources := parser.ParseResources(RESOURCES_FILE)
    groupedResources := parser.GroupByCategory(resources)

    groupedResource := groupedResources[0]

    if groupedResource.Category != "Assistência Social" {
        t.Error("Error in grouping categories")
    }

    if groupedResource.TotalYear != 1484623.00 {
        t.Error("Error in grouping values")
    }
}

