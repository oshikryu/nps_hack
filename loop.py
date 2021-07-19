from check_future_camps import main
from datetime import datetime
import time

while True:
    print(str(datetime.now()))
    main()
    print('--------------')
    time.sleep(15)
