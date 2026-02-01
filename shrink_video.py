Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from moviepy.editor import VideoFileClip
... import os
... 
... # 1. Load the big video
... print("Loading video...")
... clip = VideoFileClip("public/athena-demo.mov")
... 
... # 2. Write it as a new compressed MP4
... # MoviePy's default settings are great for web compression
... print("Compressing... this might take a minute...")
... clip.write_videofile("public/athena-demo-compressed.mp4", codec="libx264", audio_codec="aac")
... 
... # 3. Clean up
... clip.close()
