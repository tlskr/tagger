# Validate JSON file against schema using jsonschema

JSON_FILE=$1
SCHEMA_FILE=$2

jsonschema -i $JSON_FILE $SCHEMA_FILE
