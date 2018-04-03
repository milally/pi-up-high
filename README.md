# pi-up-high
Lally Homeschool Pi-Up-High project

This repo attempts to document what we've done in the Lally Homeschool for our high altitude balloon (HAB) project, named "pi-up-high" by the kids. This isn
t a curriculum, per se, but certainly a guideline with the code we wrote.

We started this project by just watching HAB launches on YouTube to understand the scope of the project as well as the art of the possible for something we had never done before. My main goals were to tech the kids practical applications of science and engineering in every day life, but also to have some fun!

# The Plan
The goals we set out at the beginning:
1. Use a base microcontroller that wasn't too difficult for two 9-year-olds, a 5-year-old and a 4-year-old to wrap their heads around
2. Get the balloon/payload to an altitude 100,000 ft
3. Capture still images and video in at least 2 different angles with a stretch goal of using 3 video cameras and 1 still camera.
4. In real-time, track the payload's altitude, atmospheric pressure, GPS location, and the forces exterted upon it
5. Do Step 3 in more than one way so we had some redundancy
6. Solder some stuff (the kids *REALLY* wanted to try their hands at soldering)
7. Have fun!

# Bill of Materials
1. I had a RaspberryPi Model 2B sitting around unused, so that seemed to fit item #1 of the plan. We could write our code mostly in Python and I could help the kids understand some Linux basics in the meantime. Plus I had the Raspberry Pi Camera Rev 1.3 to go with it (more on that later) so we had at least one camera taken care of.
2. For an acceleromter we used the MPU-6050 3-axis Gyro with Accelerometer
3. We used the GY-68 with BMP180 module to capture temperature, altitude and pressure
4. For GPS/compass we used the GYGPSV5-NEO with UBLOX NEO-M8N and HMC5983
5. To communicate with the ground, we thought SMS messages would be good below 4000ft and some type of radio transciever *should* be good for the duration, assuming ample radio power and antennas.
    1. To that extent we mistakenly bought a SIM800C GPRS GSM module (stupid 2G expiration in the US) which was later replaced by a SIM5320E module to work with 3G Us networks.
    2. For radios we found 1W RFM23BP LORA radios from HopeRF that we *think* will have a range of ~40 miles
    3. We'll use two HG908P-RSP 8dBi flat patch antennas from L-com to TX from the payload and RX on the ground.
    4. Some FTDI232 adapters will be needed to connect the radios to our Pi and the ground-chasing laptop
6. For other cameras we bought three EKEN H9R 4K Sports Action Cameras
7. We found some 3.7V 2000mAh LiPo batteries and MB102 breakout boards for clean power, at least for the radio and GSM module
8. Balloon is TBD
9. Parachute is TBD
10. Payload box is TBD
