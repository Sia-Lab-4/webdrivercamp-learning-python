#!/usr/bin/python3
var = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."
var = var.replace("There should be one-- and ", "")
var = var.replace("--obvious way to do it. lthough that ", "")
var = var.replace("may not be obvious at first ", "")
var = var.replace(" you're Dutch.", "")
print(var)

