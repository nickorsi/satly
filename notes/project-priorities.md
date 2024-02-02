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

✓ A4 (Added by Nick and Matt: get it looking nice)

### Photos page
    ✕ Consistent sizing of photos
    ✓ Center the title and caption and photo like the homepage

✓ Get the new photo to show up as #1
✓ Get new photo to not duplicate?
✓ Docstrings
✓ Refactoring -- (TODO: more after Friday)
Stop at 11:45 to get demo ready

Styled like poloroid?
Spread the stack out instead of a simple grid?


# cool things / nice to haves  (probably choose ONE)

## Image Data
System will retrieve metadata from the photo (location of photo, model of camera, etc) and store it into the database (you’ll need to learn how to read the metadata from photos)

Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)


## Image Edits

Users can perform simple image edits (for example):
✓ turning color photos into B&W   (some kind of photo api to use?)
- adding sepia tones
- reducing the size of the image
- adding a border around the image




# 2027 goals
- remove the white part from the eye - s killer mode


# Presentation Outline

- M: Demo the site  (~90 seconds)
- M: Discuss priorities     (~90 seconds)
- N: Discuss the tech stack / diagram (~90 seconds)
- N: Database - start with one photo URL and then discuss how to do it
    - One source of truth discussion
    - Does the real world do it like this? Who knows?
- M&N Cool stuff section
    - N: Form encoding (multipart)
    - M&N: How to grab photo, make changes (or just add), upload (use staging)
    - M: Pillow
- M&N Where next?
    - TESTS...
    - Refactoring photo edits (sepia, borders, saltiness, etc)
    - EXIF (would have been nice...)
    - Marketing
    - Hosting


