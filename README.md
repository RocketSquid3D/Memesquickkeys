# Meemee's Quick Keys

Meemee (Grandma) likes to type stories and journal entries to print and share with the family.  However, she's trying to do this on an iPad, and for someone in their 80's manuevering around the iOS interface can be downright esoteric.  A couple of nice, labeled command-key functions should hopefully make it easier.

This project doesn't do anything terribly fancy.  It uses a Pico to send keyboard commands to an ipad, which is plugged in through a Lightning-to-USB Camera Adapter.  Printing is about the fanciest thing it does, it will pull up the print dialogue, wait about 15 seconds (mainly to confirm the printer is connected) and then automatically confirms the print job.  Everything else is seriously just the command key + whatever makes a new document, opens a document, or inserts a new page.

I'm assuming you already know how to solder or have some other way to put this together

What you'll need:
  Hardware:
    1. Raspberry Pi Pico
    2. 4 Buttons of your choice
    3. A lightning to usb Camera Adapter (Apple's gotta get their pay, I guess) - https://www.apple.com/shop/product/MD821AM/A/lightning-to-usb-camera-adapter
    4. A 3D print of the case, found here - 
