# mayaTornado
Python script to generate a particle systems vortex and assigns an Arnold volume shader for rendering.  You may also use mayaSimpleTornado to generate the particle system without the Arnold shader.

This script creates a sphere and a particle emitter attached to the sphere. It also adds a turbulence field and a vortex field to create a swirling motion, simulating a tornado effect. You can adjust the parameters (like rate in the emitter, magnitude in the vortex, etc.) to fine-tune the appearance of the tornado.

This script also creates an Arnold Standard Volume shader and assigns it to the particle system. The aiStandardVolume shader is used here because it's suitable for volumetric effects like the ones created by particle systems.

Please note that fine-tuning the appearance of the particles and the shader will require adjusting various attributes in the shader, as well as the particle system settings. Also, the availability and exact behavior of these features can vary depending on the version of Maya and Arnold you are using.

To use this script:

Open Maya.
Open the Script Editor.
Paste this script into a Python tab.
Execute the script.

You can also drag the script to the shelf and create a button to execute.
