#BUGS
-Default value not recognized in Photo model at DB level
-(Pdb) *** flask.debughelpers.DebugFilesKeyError: You tried to access the file 'file' in the request.files dictionary but it does not exist. The mimetype for the request is 'application/x-www-form-urlencoded' instead of 'multipart/form-data' which means that no file contents were transmitted. To fix this error you should provide enctype="multipart/form-data" in your form.

The browser instead transmitted some file names. This was submitted: 'Canon_40D.jpg'
WHERE THE F**K IS OUR FILE?????



#Victores
-Successful upload to S3 from python
-Succseful access to others S3 files
-Successfully received file data from a form, LOOK AT ENCTYPE ATTRIBUTE ON FORM