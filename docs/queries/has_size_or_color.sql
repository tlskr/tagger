-- filter on whether tag_metadata includes top-level key "size" or "color"

select
      vendor_id
    , tag_metadata

from 
    tag

where
    tag_metadata?|array['size', 'color']


limit 10
