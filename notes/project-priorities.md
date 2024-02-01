TS
Express (vs Flask)
React
Attractiveness

What are our goals for this?
Pleasing looks, presentable, portfoilio-ready, curb-appeal


Pix.ly: Image lighttable / editor»

(Login/authentication isn’t required; any web user can do everything)

✓ A1 Images themselves are stored to Amazon S3, not in the database

✓ A2 Users can add a JPG photo using an upload form and picking a file on their computer (you’ll need to learn how to allow image uploads!)

✓ A3 Users can view photos stored in the system

1/2 A4 (Added by Nick and Matt: get it looking nice)

Styled like poloroid?
Spread the stack out instead of a simple grid?


# cool things / nice to haves  (probably choose ONE)

## Image Data
System will retrieve metadata from the photo (location of photo, model of camera, etc) and store it into the database (you’ll need to learn how to read the metadata from photos)

Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)


## Image Edits

Users can perform simple image edits (for example):
-turning color photos into B&W   (some kind of photo api to use?)
-adding sepia tones
-reducing the size of the image
-adding a border around the image