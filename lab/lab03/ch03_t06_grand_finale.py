from datetime import datetime

now = datetime.now()

print(%02dd:%04d' % (now.hour, now.minute, now.second))
