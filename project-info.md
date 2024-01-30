# Questions

- How to minify photos?
- How to see exif data on photos? (Maybe a python 3rd party library?) Answer: probably Pillow.


# Notes

Not every photo has exif data!
So make sure that if you do exif stuff, ensure the photo actually has exif data.
See iggy for an example of exif data:
    https://github.com/ianare/exif-samples/blob/master/jpg/Canon_40D.jpg

Scaffold it in such a way that you can test as you go.

No access to patch or delete:
The form is doing all the work -- no api exists.
look back to flask api lecture notes in a cool little box
e.g.: links are GETs only
forms are only POSTS

If you're going the template route, then just make post requests


