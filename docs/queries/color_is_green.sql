-- filter on whether tag_metadata includes top-level key "color" has value "green"

select
      vendor_id
    , tag_metadata

from 
    tag

where
    tag_metadata->'color' = '"green"'


limit 10
