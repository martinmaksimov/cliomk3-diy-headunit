<p align="center">
  <img src="assets/images/emanuel.svg" />
</p>

### DIY head unit for Clio Mk3 enabling Android Auto, Apple Carplay, and other mods.

I love my Clio 197, aka [Emanuel the Clio](https://www.instagram.com/emanuel_the_clio/), but it is lacking in some creature comforts like navigation and a decent way to stream and control music. I really did not want to buy one of those big aftermarket touchsreen units and have always tried to keep all of the modifications on my car sort of OEM+.

In this spirit, I decided to try and repurpose the original TomTom navigation housing and update its internals with modern components. Thus this project was born. A lot of people have shown interest in replicating it so I am putting together this guide and I hope people can enjoy their Clios for longer!

If you have found this useful and enjoy project like this, please consider following Emanuel's adventures and supporting him on Instagram at [@emanuel_the_clio](https://www.instagram.com/emanuel_the_clio/)

Good luck and happy building!

---

**DISCLAIMER**

**To make this project work you will need to do some coding, wiring, plastic cutting (hopefully not for long). If you have absolutely no coding/tech experience I would advice against trying this. The good thing is that it is all reversible and non-destructive (except the screen housing) so if you were to not get it right, you can just plug back in your old factory screen.**

# Table of Contents

- [Parts List](#parts)
  - [Software](#software)
  - [Hardware](#hardware)
  - [Tools](#tools)
- [Assembly](#assembly)
  - [Installing OpenAuto Pro: Steps 1 to 3](#1-3)
  - [Assembling Components: Steps 4-7](#4-7)
  - [Dry Testing and Optional CarPlay: Steps 8-9](#8-9)
  - [Setting Up CarPiHat: Steps 10-13](#10-13)
  - [Wiring and Housing: Steps 14-15](#14-15)
  - [Enabling Automation Services: Step 16](#16)
  - [Enabling Bluetooth Audio: Steps 17-19](#17-19)
- [Additional Notes](#notes)

<a id="parts"></a>

# Parts List

The build revolves around a piece of software called [OpenAuto](https://bluewavestudio.io/). I have used the Pro paid version since it allows a lot of freedom and the add-ons that I need to make everything work. Using the free open-source version might also work but the price is really not high so I decided to go with the Pro version.

The software supports Android Auto out of the box. If you also want Apple Carplay you will need an additional adapter and a software plug-in to make it work.

**DISCLAIMER**

**This is an open-source project and a lot of effort has been put to making this available to everyone for free. Some of the links in the Parts List below are affiliate links. They do not change the cost for you but clicking on them and purchasing the item in that manner will support the project and its future development. Thank you for the support!**

<a id="software"></a>

## Software

- [OpenAuto Pro](https://bluewavestudio.io/shop/openauto-pro-car-head-unit-solution/) software license
- [OpenAuto CarPlay Plugin](https://bluewavestudio.io/shop/plugin-carplay-autobox-for-openauto-pro/) [OPTIONAL]
- [Renault Loading Screen](https://bluewavestudio.io/shop/splash-screens-package/) [OPTIONAL]

<a id="hardware"></a>

## Hardware

- [Raspberry Pi 4 Model B 4Gb](https://amzn.to/47HWIYH)
- [CarPiHat](https://thepihut.com/products/carpihat-car-interface-hat-for-raspberry-pi?variant=41600908492995)
- [32Gb MicroSD Card](https://amzn.to/460NxBj)
- [7 Inch Touch Screen Monitor for Raspberry Pi](https://amzn.to/3FXschf)
- [External Stereo Sound Card](https://amzn.to/471crCb)
- [Bluetooth 4.0 USB Adapter](https://amzn.to/3QQKFlZ)
- [RN-C24 24-pin Adapter](https://amzn.to/3Su6EAB)
- [Renault Car Stereo Bluetooth Adapter](https://amzn.to/3Qu7pqv)
- [Clio Mk3 TomTom SatNav Housing](https://www.ebay.co.uk/itm/194181732840)
- [Carlinkit CCPA Adapter](https://amzn.to/3ss2WwG) [OPTIONAL]
- [Renault Car Stereo Aux In](https://amzn.to/49rOWn8) [OPTIONAL]
- [Car Stereo Microphone](https://amzn.to/49mFXUx) [OPTIONAL]
- [Bluetooth 4.0 OBD2 ELM327 Adapter](https://amzn.to/49uw1s4) [OPTIONAL]

<a id="tools"></a>

## Tools

- [Cable Crimping Tool Set](https://amzn.to/3Qxden3)
- [Digital Multimeter](https://amzn.to/3FPoBBR) [OPTIONAL]

Here is a [list](https://docs.google.com/spreadsheets/d/1OFVzR3P-o9TuCRibHxrFXSt-syTtQHrRWYO4-cv3wwE/edit?usp=sharing) of the hardware and software components in a tabular form. There is some additional information and notes for each item as well if you are interested.

<a id="assembly"></a>

# Assembly

<a id="1-3"></a>

1. First we will need to burn and install the software onto our SD card. The [OpenAuto Forum](https://bluewavestudio.io/community/) is a great resource with a lots of guides on how to do mostly everything software related if you ever get lost. Before you start, go ahead and purchase an OpenAuto Pro License. It can take up to 12 hours for them to get back to you with your licensed file and activation key.

2. Once you have received your file and activation key refer to [this](https://www.youtube.com/watch?v=fb5lxQvdhbI) video on how to flash the OpenAuto software to the Micro SD card. I used a free program called [Balena Etcher](https://etcher.balena.io/).

3. Insert the flashed Micro SD card into the Raspberry Pi Micro SD slot

<a id="4-7"></a>

4. Install the Raspberry Pi to the back of the screen and connect the screen to the Pi using one of the provided ribbon cables. I secured the Pi to the screen with just two of the screws (top left and bottom right). I used the other two to secure the CarPiHAT to the Pi. Ideally you can use some long screws to screw in everything together if you can get a hold of those but this has worked just fine for me.

5. Install the CarPiHAT on top of the Pi using the remaining two screws

6. Plug in the USB Bluetooth Adapter and the USB Stereo Audio Card. I advise you to also get a USB wireless keyboard so that you can easily navigate the Pi and be able to troubleshoot things in the future while in the unit is installed in the car without taking it out. Also plug in the Carlinkit adapter if you are going to use CarPlay.

7. At this point you can use a power bank or USB-C charger to give power to the Pi via the USB-C port. You should be taken to the OpenAuto Pro activation screen and follow the instructions on inputting your license key.

<a id="8-9"></a>

8. Once you are successfully loaded in the OpenAuto home screen, you can use a USB cable to connect your phone and test if either Android Auto or Apple Carplay works, depending on which one you want.

   - If you are planning to use Carplay, go to the CarPlay section in the Additional Notes at the bottom to read about the CarPlay Plug-in before you continue.

   - For Android Auto plug the cable directly into the Pi, for Carplay plug into the Carlinkit adapter if it enables wired connection (the CCPA from the Parts List does). Once plugged in the corresponding software should load up automatically which will confirm for you that all of your hardware peripherals are compatible with the OpenAuto Software.

9. The next step is to enable wireless Android Auto and Apple Carplay. To do that you need to connect your phone to the Raspberry Pi via Bluetooth. You can do that my connecting your phone to the Open Auto using the **Telephone** -> **Add menu**. It will walk you through a user friendly setup procedure. Once your phone is connected, you should see a **Wi-Fi** button when you go into either Android Auto or Autobox (this is CarPlay) menus.

<a id="10-13"></a>

10. Now that you have made sure the base software works as expected and connects successfully, it is time to wire things into the car. What we want to achieve is for the unit to start up with ignition and then to gracefully shut down (not cut power and crash) when ignition is off. To achieve that, we will need to convert the car's 12V power down to 5V and have a relay that switches and runs a script that shuts down the unit when ignition is off. Fortunatelly, there is a great solution for exactly this application called [CarPiHAT](https://github.com/gecko242/CarPiHat/wiki). You can refer to the [Quick Start Guide](https://github.com/gecko242/CarPiHat/wiki/Quick-Start-Guide) if you get into trouble but I will describe the steps necessary to make this work below.

11. We want to create a script that monitors a couple of GPIO pins on the Pi and manages power based on those inputs. There is a great explanation and examples of this in the CarPiHat Quick Start Guide. In order to do that we will have to get out of OpenAuto and go to the Raspberian OS. You can do that by clicking on the power button in OpenAuto towards the bottom and then click Return which will bring you do the OS. At this point you WILL require at least a keyboard connected. Press `Ctrl+Alt+T` to open up the terminal. I am assuming that you have a basic understanding of terminal commands if you are attempting this project. If you are struggling please refer to this [Quick Guide for the Command Line](https://raspberrypi-guide.github.io/programming/working-with-the-command-line).

12. We are going to create a new python file called `carPiHat.py`

    1. `Ctrl+Alt+T`to get to the terminal. You should already be in the `/pi` folder, if not navigate to that using the `cd` and `ls` commands.
    2. Type in `sudo nano carPiHat.py` and press `Enter` to create a new file. This will bring up the nano file editor which we will use to create our script.
    3. Copy and paste the contents of the **carPiHat.py** file that is in the source code of this repository.
    4. To save press `Ctrl+X`, then `Y` to confirm, then `Enter` to exit back to the Terminal. You now have the script required to safely turn on and off the Pi with the car's ignition.

13. We now need to create a service that will trigger this script. A service is a program that runs in the background without the need of user interaction. There is a great guide on how to do that [here](https://github.com/gecko242/CarPiHat/wiki/Safe-Shutdown-using-a-Service). I will run down through the commands below.
    1. Make the `carPiHat.py` script executable by running the following command in the Terminal and pressing `Enter`
       - `chmod +x /home/pi/carPiHat.py`
    2. Create the service file by running the following command in the Terminal and pressing `Enter`
       - `sudo nano /etc/systemd/system/carpihat.service`
    3. Copy and paste the contents of the `carpihat.service` file that is in the source code of this repository
    4. To save press `Ctrl+X`, then `Y` to confirm, then `Enter` to exit back to the Terminal.

---

**IMPORTANT**
Before you finish this setup and enable the service that you just created, you HAVE to wire up the Pi with the car's ignition and constant 12V power. After you enable the service and restart the Pi, you WILL NOT be able to run it and continue any further setup or troubleshooting using power through the USB-C port. I suggest you enable the service once you have power through the car to avoid any extra work (learned that from experience).

---

<a id="14-15"></a>

14. The [CarPiHat Quick Start Guide](https://github.com/gecko242/CarPiHat/wiki/Quick-Start-Guide) has a handy pinout diagram
    ![Alt text](https://github.com/gecko242/CarPiHat/raw/master/Datasheet_latest.png)

- We are interested in the Main Loom pins 1,2,3, and 5.

  - **Pin 1** is ground which we will connect to ground in the car's radio screen wiring loom
  - **Pin 2** is Illumination which we can use to enable light and dark mode based on if the car has the lights turned on or off.
  - **Pin 3** is constant 12V power.
  - **Pin 5** is ignition power which we use to trigger the on and off script and service.

- Below is a photo of the car's radio screen wiring loom. We are interested in the second row of pins (on the bottom of the picture), pins 13-24.
  ![Alt text](/assets/images/radio_screen_loom.JPG)
  - **Pin 15** (blue wire) - Illumination
    - Wire this to **Pin 2** on the CarPiHat
  - **Pin 17** (yellow wire) - Ignition 12V
    - Wire this to **Pin 5** on the CarPiHat
  - **Pin 21** (red wire) - 12V Constant
    - Wire this to **Pin 3** on the CarPiHat
  - **Pin 23** (black wire) - Ground
    - Wire this to **Pin 1** on the CarPiHat
- I used a Crimping Tool Set to wire up the mini molex cables that come with the CarPiHat to a RN-25 adapter that I found. The adapter I used came from an AV cable that I had to cut and de-pin. It also had some extra plastic guides on the inside which prevented the car loom to go in and clip in. I cut those off with my trusty Swiss knife. The resulting setup looked like this:

  ![Alt text](/assets/images/wiring_1.JPG)
  ![Alt text](/assets/images/wiring_2.JPG)
  ![Alt text](/assets/images/wiring_3.JPG)
  ![Alt text](/assets/images/wiring_4.JPG)

15. Once you have tackled that it is time to fit everything in the TomTom housing. As you have probably already noticed, the 7 inch screen is just a little bit too tall for the original screen opening. There are also some brackets on the inside holding the original TomTom that are in the way, especially on the side opposite to the airbag light (we obviously want to keep that operational). Again, with the use of my trusty Swiss knife, I hacked off about a centimeter from the top of the housing to be able to fit the screen. I also removed a lot of the existing clasps on the back. Some patience and different grits of sanding paper later you can see the result below. I have used so 3M adhesive soft strips to hold the screen in places and demove any potential rattles. Everything fits just nicely with the housing closed up.

![Alt text](/assets/images/housing_1.JPG)
![Alt text](/assets/images/housing_2.JPG)
![Alt text](/assets/images/housing_3.JPG)
![Alt text](/assets/images/housing_4.JPG)
![Alt text](/assets/images/housing_5.JPG)
![Alt text](/assets/images/housing_6.JPG)
![Alt text](/assets/images/housing_7.JPG)
![Alt text](/assets/images/housing_8.JPG)

- Ideally it would be best if we can make a 3D scan of the original housing and create a 3D model that fits and clips all of the components perfectly while maintaining the factory look. I am working with somebody on creating that so follow this space! If you have experience in this kind of work and are willing to help please chime it too!

<a id="16"></a>

16. We are now ready to go to the car and finish the installation. Connect the unit to the car's radio display loom and turn on ignition. The unit should start and bring you to the OpenAuto home screen. We need to finish enabling the service that we created earlier. To do that, exit OpenAuto and open a Terminal window. Type in the following commands, pressing `Enter` after each one to execute

    - `sudo systemctl deamon-reload`
    - `sudo systemctl enable carpihat.service`
    - `sudo systemctl start carpihat.service`
    - `sudo systemctl status carpihat.service`

    Restart the Pi to test the service. You can do that by executing `sudo reboot` in the terminal. When the Pi reboots, turn off ignition and open the driver's side door to cut all power. The Pi should "gracefully" shut down after 10 seconds.

<a id="17-19"></a>

17. The last thing to do is connect the Pi to the factory radio's Bluetooth so that it can stream audio through the speakers. What I have done works for the Update List Renault radios. I purchased a Renault Bluetooth AUX adapter which connects to the back of the radio through two ISO connectors(the green and blue ones on the right) as follows:

![Alt text](/assets/images/radio_bluetooth.JPG)

18. This enables Bluetooth streeming through the AUX Source option on the radio. We now need to connect the Pi to the Bluetooth module. To do that we will need to acquire the MAC address of the Bluetooth module. You can do that through the Terminal and start scanning which will bring a list of devices and their characteristics. If you have parked somewhere where there is a bunch of Bluetooth devices around you it may be hard to identify which one is the radio (this was a pain living in the city). To start scanning we will use the `bluetoothctl` agent of Raspberry Pi through the Terminal.

    1. Open a Terminal window
    2. Execute `bluetoothctl scan on`
    3. Find your Bluetooth device and take note of the MAC address. It should be under the following format XX:XX:XX:XX:XX:XX
    4. Execute `bluetoothctl pair XX:XX:XX:XX:XX:XX`. You may be prompted to enter a passcode or something depending on your module.
    5. Execute `bluetoothctl trust XX:XX:XX:XX:XX:XX` to add the device to trusted devices
    6. Execute `bluetoothctl connect XX:XX:XX:XX:XX:XX` to connect to the device.
    7. You should have audio running to factory radio now! Try streming some music through OpenAuto to test that.

19. The only thing left to do is create a small script that will connect the Pi to the radio's Bluetooth on startup so that you do not have to do that manually every time.

    1. Open a Terminal window and execute `sudo nano bluetooth_radio.py` to create a new file. This will bring up the nano file editor which we will use to create our script.
    2. Copy and paste the contents of the `bluetooth_radio.py` file that is in the source code of this repository. Make sure to replace the example MAC address with the MAC address of your Bluetooth Device
    3. To save press `Ctrl+X`, then `Y` to confirm, then `Enter` to exit back to the Terminal.
    4. Execute `sudo nano /etc/rc.local` to edit the file
    5. Add `python /home/pi/bluetooth_radio.py` as a new line at the bottom of the file which will start the script when the Pi boots
    6. To save press `Ctrl+X`, then `Y` to confirm, then `Enter` to exit back to the Terminal.

20. You have done it! Try rebooting the Pi and make sure that the Bluetooth radio connects on boot automatically.

21. Install the unit with in the designated spot. Everything just clips in place, first the front part followed by the rear cover.

![Clio MK3 Head Unit](/assets/images/headunit.JPG)

<a id="notes"></a>

# Additional Notes

### Apple Carplay

CarPlay requires an additional dongle and an additional software plug-in for OpenAuto Pro. Once you have purchased and receive the license, the email will have instructions for how to install it. You will require to connect the Pi to Wi-Fi and run a command in the Terminal which will download the plug-in. Then you will be able to activate it with the attached license key inside OpenAuto.

### Renault Loading Screen

This is not necessary but it is a very nice addition to make the entire experience OEM. Again it is a small plug-in that give you a Renault badge overlay while the system is booting - a nice touch. The setup is similar to the CarPlay plug-in and comes with detailed instructions in an email.

### AUX In

It is possible to bypass steps 17-19 by installing a direct AUX In cable. You would need to connect that to the USB Audio Card connected to the Pi. I did not go that route because you need to take out the whole dashboard or do some magic cable fishing to route that cable behind the AC vents and down to the radio.

### Microphone

If you want to do handsfree calls, you can buy a car microphone and plug it into the USB Audio Card. I believe that if you want the Mic to work you will have to also use the wired AUX In for the Audio as well.

### Steering Wheel Controls

The steering wheel controls for volume and mute currently do not work. It seems like they only work if some additional pins on the Radio Screen are also connected. I am working with a Renault Tech to figure out which ones exactly but that should be enabled soon! Just French stuff...

### Radio Code

The Renault Radio requires an activation code if the battery gets disconnected for some reason. If you do not know your code you can hold 1 and 6 on the radio and a 4 digit code will show up. You can then use a decoder app (I use [this](https://apps.apple.com/gb/app/radio-decoder-for-renault/id1457616100) one) to get the unlock code. Since you will not have the original radio screen anymore, it is worth knowing your code and the activation procedure without a screen. If that happens, you need to enter the 4 digit code. Procedure is as follows, example for an activation code of 5678:

1. The radio starts with the first number flasing at the value of 0 and ready to enter. If your first number is 5 then press 1 on the radio five times to change it to 5.
2. Pressing a different number (2,3, or 4) will select a different position to enter a number.
3. Press 2 on the radio to select the second number position. It will then start flashing and it will be at 0.
4. Repeat the same for all 4 numbers.
5. After you have put in all four numbers, press and hold 6 to confirm.
6. The radio should be active again.

### Radio Sources

You might not have an aux port at all in your car but that does not mean you do not have aux capabilities! [This](https://www.youtube.com/watch?v=NG0VxEwU6Vc) video explains very well how to set up the SRC or different source options on your radio and also how to enable AUX. I have left just FM and AUX turned ON on mine so that I can easily switch between listening to radio or going back to Bluetooth.
