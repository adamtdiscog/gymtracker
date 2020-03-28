# gymtracker

Purchase list
1. https://www.amazon.com/dp/B07P8ZCJCG/?coliid=IKN9SL3D7BJ4N&colid=1Q0EO0PUMHINQ&psc=1&ref_=lv_ov_lig_dp_it
2. https://www.amazon.com/LABISTS-Raspberry-Complete-Preloaded-Heatsinks/dp/B07YRSYR3M/ref=sxin_3_osp35-ba0f8bee_cov?ascsubtag=amzn1.osa.ba0f8bee-ff67-4e52-9ec3-fd1b06c8e77b.ATVPDKIKX0DER.en_US&creativeASIN=B07YRSYR3M&cv_ct_cx=raspberry+pi+4&cv_ct_id=amzn1.osa.ba0f8bee-ff67-4e52-9ec3-fd1b06c8e77b.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_wn=osp-search&dchild=1&keywords=raspberry+pi+4&linkCode=oas&pd_rd_i=B07YRSYR3M&pd_rd_r=eeb66938-e58a-4917-9dc7-fe0b32ea4c55&pd_rd_w=oXxh9&pd_rd_wg=vQz2n&pf_rd_p=3494954a-3e59-449e-91eb-b8736f013ede&pf_rd_r=GPGP5Y8JXXBQHAZ2F892&qid=1585364066&s=electronics&sr=1-2-32a32192-7547-4d9b-b4f8-fe31bfe05040&tag=heavy0013-20


Use the gymtracker, email, and new_excel files for the foundation of your tracker while using a cronjob to
set the automatic email and creation of a new tab in the excel sheet. 

See below for crontab config:
  
  Crontab -e
59 23 * * 6 python3 yagmail.py ##This sends an email Saturday at 23:59
01 0 * * 7 python3 new_excel.py ##This creates new excel for the week on Sunday at 00:01
02 0 * * * python3 reboot.py ##This reboots the pi on Sunday at 00:02 to reset counter



Also need to run python script on startup

sudo nano /etc/xdg/lxsession/LXDE/autostart




This will allow you to add an element to run when the LXDE desktop session begins (the raspian default GUI if setup to do from raspi-config)

It will probably have entries like these:

@lxpanel --profile LXDE
@pcmanfm --desktop --profile LXDE
@xscreensaver -no-splash

It's just a matter of adding your script there as well

@lxpanel --profile LXDE
@pcmanfm --desktop --profile LXDE
@xscreensaver -no-splash
@python /home/pi/gymtracker/tracker.py