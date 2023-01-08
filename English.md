# unlock-bilibili-uwp
Translated by machine.  
Decrypt the downloaded video of bilibili UWP version.
# Bilibili UWP Version Video Unlock
After an update, due to copyright issues, the UWP version of station B encrypted the downloaded MP4 files;  
In order to open it in a normal player, I studied the encryption method and wrote a piece of code to realize automatic decryption.
# Principle
The program principle is very simple:  
It can be seen from the hexadecimal editor that the encryption method of the file is to add 3 bytes of "FF" to the file header;  
Deleting these "FF" can complete the decryption of the video;  
The program obtains the file information by obtaining the command line parameters, opens the file through the Python binary, deletes the first 3 bytes and rewrites it to realize the decryption function.
# How To Use
You can download the source code to compile and run by yourself, or download the compiled version in Releases;  
Just drag the downloaded MP4 file onto the exe file to decrypt it;  
You can also double-click to open the program, and enter the file name or path to complete the decryption.
