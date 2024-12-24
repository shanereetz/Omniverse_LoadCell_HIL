# Load Cell Simulation

This NVIDIA Omniverse extension demonstrates using a load cell as a source for physics data inside a simulation. This is a concept known as Hardware-In-The-Loop (HIL), where real hardware is being connected to a simulation.

Currently, it's in a demo state. This documentation and the extension is being made more portable.

Below is a suggested set of hardware that is fairly cheap and easy to get started with. The extension makes some assumptions about this hardware being used (baudrate, message format).
Any serial interface can be substituted as the extension simply reads from a serial device.
https://www.youtube.com/watch?v=NinARMVomnYa

## Getting Started

### Hardware

#### Load Cell Amplifier ($5.95)
Adafruit NAU 7802
https://www.adafruit.com/product/4538

#### Load Cell ($3.95)
Pick a weight that makes sense for your application.
https://www.adafruit.com/product/4630

#### Arduino Uno ($27.60)
Basically any microcontroller with I2C should be sufficient.
https://github.com/adafruit/Adafruit_NAU7802

Arduino code for the NAU 7802 is available here, along with installation instructions:
https://github.com/adafruit/Adafruit_NAU7802

### Instructions

#### Preparing the hardware
- Connect load cell to NAU 7802
- Connect NAU 7802 to microcontroller. If using Arduino, use pins A4 (SDA) and A5 (SCL).
- Connect the Arduino to your computer
- Install the Adafruit library https://github.com/adafruit/Adafruit_NAU7802
- From file->examples, load the sample code
- Adjust samples per second as necessary
- Check that baud rate matches between OV extension (115200 by default) and the Arduino
- Test readings using the Serial Monitor in the Arduino IDE

#### Using the extension
- Add extension to search paths under Window->Extensions
- Determine the COM device or address of Arduino (#TODO add more detail here)
- Open the extension UI from the top menu bar of Omniverse
- Input that address into the Extension UI
- Connect (#TODO currently the prim association is hardcoded, you'll need to modify the extension to apply this value to your own tools)
- Edit the extension code to apply the (#TODO write values to a generic prim attribute so it can be used elsewhere, with OmniGrpah, etc)
