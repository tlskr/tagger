#   from the schema, get the << tags >> property of the top-level << properties
#   >> property

jq '.properties.tags' schema.json
