#!/bin/bash
# send GET request to URL and display the body of the response
curl -sfL "$1" -X GET
