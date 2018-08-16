select
      vendor_id
    , tag_metadata
    , tag_metadata->'type' as type_value
    , tag_metadata->>'type' as tv_as_text   -- object field as text

from 
    tag

where
    tag_metadata::text != '{}'

limit 10
