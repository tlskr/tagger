#   from the schema, get the schema for items in array << tags >> 

jq '.properties.tags.items' schema.json
