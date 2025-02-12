from datetime import datetime, timedelta


bugin = datetime.now()

keshe = bugin - timedelta(days=1)
erten = bugin + timedelta(days=1)

print("Keshe:", keshe.strftime("%Y-%m-%d"))
print("Bugin:", bugin.strftime("%Y-%m-%d"))
print("Erten:", erten.strftime("%Y-%m-%d"))