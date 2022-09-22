#!/bin/bash
# sends a req to $1 URL, display response status code only
curl -so /dev/null --write-out "%{http_code}" "$1"
