from datetime import datetime

now = datetime.now()

print('%02d02d:%04d' % (now.hour, now.minute, now.second))
