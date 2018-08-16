-- filter on whether tag_metadata includes top-level key "size"

select
      vendor_id
    , tag_metadata

from 
    tag

where
    tag_metadata?'size'

limit 10
