HOW TO USE (super detailed full guide)

Step 1 - find a suitable .obj file

Look around the widths of the world wide web, an example would be [https://free3d.com]
and find a [cool looking model]
Once youve found your [cool looking model] you may check its triangle count, I personally use
[https://3dviewer.net/] for that.
(This site will also let you flip the model when exporting and convert it to .obj too iirc)
Your object should have 22.222 triangles or less.
I sincerely recommend it to have less, but feel free to push the limits,
turbowarp should somehow handle it as long as you dont fly too close or into to the object.
That reminds me to remind you to use the turbowarp version of this project
[https://turbowarp.org/1130638876/fullscreen?hqpen&clones=Infinity&limitless&offscreen],
which makes it faster and prettier.


Step 2 - use the super cool helper program

For basic functionality youll only need extract_triangles.py.
Place it into the same folder as your .obj file. Make sure to RENAME your .obj file to "model.obj".
Now you can run the program, you should also install Python before that if you dont have it :3.
If this worked, you should now have a file called triangles.txt in the same folder as your .obj and .py files.

if you want, you can run the extract_angles.py aswell, it will give you the angle of the normal
of each triangle to the comparison vector (default is [1┃1┃1]) in a angles.txt file.

Step 3 - import into Scratch

When inside the Scratch project, that is hopefully running on Turbowarp, press h to display the two import lists.
Right click the import_own list, press import and select your triangles.txt.
Same goes for the import_angles list and angles.txt.
When you did this, press h again to hide the lists, then press 9 and pray that everything worked.
If it did, you should now see youf object somewhere.

It might be tiny, it might be HUGE, it might be flipped in unwanted directions, at the moment there is
no way to fix those issues inside the scratch
project, as it is just a very simplistic viewer.

I hope you have fun with my project,
feel free to feedback it, and and check out my other stuff on scratch if you got time :3


