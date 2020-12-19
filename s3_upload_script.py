import os

os.chdir('reddit/')
files = []
for _,_,file1 in os.walk('./'):
	files.append(file1)

files = files[0]
files.sort()
print(files)
files.remove("RC_2015-05")
files.remove("upload_id.txt")
files.remove("upload.sh")
print(files)


def execute(cmd):
   print("input ==>",cmd)
   stream = os.popen(cmd)
   output = stream.read()
   print("output ==>",output)



for i,j in enumerate(files):
	execute("aws s3api upload-part --bucket dsml-vasu-simar-daniel --key RC_2015-05 --part-number {} --body {} --upload-id 9Tjyb8UqV13EFUpJo5IIeCY4zHvm7pbLjbsY.OgTsjN20YYM4eyPMq0Awb4vfVeeCaZZHDVCSlGLbJj5X0W5XRe8QksS7cvQwmJwK5Fhs9y1VggZNJev.lGQL8GO.iZ8LvwPfwkw6hbbDsUhnB94dg--".format(i+1,j))
