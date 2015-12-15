package api

import (
    "encoding/json"
    "net/http"
    "olhovivo/parse"
    "path/filepath"
)

var RESOURCES_FILE, _ = filepath.Abs("downloads/resources.json")


// ResourceList returns resource in json format grouped by category
func ResourceList(rw http.ResponseWriter, r *http.Request) {
    resources := parse.GroupByCategory(parse.ParseResources(RESOURCES_FILE))
    jsonResponse, err := json.Marshal(resources)

    if err != nil {
        http.Error(rw, err.Error(), http.StatusInternalServerError)
        return
    }

    rw.Header().Set("Content-Type", "application/json; charset=utf-8")
    rw.Write(jsonResponse)
}
