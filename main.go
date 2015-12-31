package main

import (
    "net/http"
    "olhovivo/api"
)

func main() {

    http.HandleFunc("/api/resources", api.ResourceList)

    http.Handle("/", http.FileServer(http.Dir("public")))
    http.ListenAndServe(":5000", nil)

}
