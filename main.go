package main

import (
    "net/http"
    "olhovivo/api"
)

func main(){
    http.HandleFunc("/", api.ResourcesList)
    http.ListenAndServe(":5000", nil)
}
