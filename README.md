# nps_hack
A scripts to poll the NPS website for yosemite day passes that free up.

Install related libraries:
```
pip3 install -r requirements.txt
```

### Install twilio dependencies

```
brew tap twilio/brew && brew install twilio
```

Set your twilio env variables for notifications in a .env file or `export` explicitly:
```
TWILIO_ACCOUNT_SID="YOUR SID"
TWILIO_AUTH_TOKEN="YOUR AUTH TOKEN"
TWILIO_FROM_PHONE=15551234567
PHONE=15551234567
```

### Run scripts
Comment out the REAL and TEST env variables
#### arguments
```
-t # run twilio SMS notification
-b # open browser if a campsite is available
```

#### Check all camps: 
```
python3 check_future_camps.py -t
```

#### Infinite loop watcher
Default timeout is 30s
```
python3 loop.py -t -b
```

#### Run day pass script: 
```
python3 yosemite_day_pass.py
```

#### Run upper pines campsite script: 
```
python3 upper_pines_camping.py
```

#### Example output for upper pines:
```
ryuta:~/projects/nps_hack ∴ python3 upper_pines_camping.py                                                                                                                                                                                                       
Number of available campsites: 18
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '102', 'site': '046', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '108', 'site': '006', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-14T00:00:00Z', 'day_of_week': 'Monday', 'site_id': '169', 'site': '073', 'loop': 'UP2'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '172', 'site': '083', 'loop': 'UP2'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '176', 'site': '098', 'loop': 'UP3'}
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '176', 'site': '098', 'loop': 'UP3'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '205', 'site': '003', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '257', 'site': '041', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '257', 'site': '041', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '269', 'site': '139', 'loop': 'UP4'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '271', 'site': '153', 'loop': 'UP4'}
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '271', 'site': '153', 'loop': 'UP4'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '290', 'site': '075', 'loop': 'UP2'}
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '290', 'site': '075', 'loop': 'UP2'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '300', 'site': '116', 'loop': 'UP3'}
{'status': 'Available', 'date': '2020-09-09T00:00:00Z', 'day_of_week': 'Wednesday', 'site_id': '82', 'site': '025', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-10T00:00:00Z', 'day_of_week': 'Thursday', 'site_id': '82', 'site': '025', 'loop': 'UP1'}
{'status': 'Available', 'date': '2020-09-14T00:00:00Z', 'day_of_week': 'Monday', 'site_id': '87', 'site': '030', 'loop': 'UP1'}
Campsites are available for 09/2020
Recreation.gov url: https://www.recreation.gov/camping/campgrounds/232447
button returned:OK
```
