# jq to get all possible paths in a json object?
#       https://github.com/stedolan/jq/issues/243

FILE=$1

jq 'path(recurse(if type|. == "array" or . =="object" then .[] else empty end))' $FILE
