# nps_hack
A scripts to poll the NPS website for yosemite day passes that free up.

Install related libraries:
```
   pip3 install -r requirements.txt
```

Run day pass script: 
```
   python3 yosemite_day_pass.py
```

Run upper pines campsite script: 
```
   python3 upper_pines_camping.py
```

Example output for upper pines:
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

Run all yosemite campsites check: 
```
   python3 check-all-camps.py
```
