import click, json, time

def isRead(arg1, arg2):
	if arg2 == None and arg1 != "what":
		return False
	else: 
		return True

def readHistory():
	with open('history.json') as history_json:
		history = json.load(history_json)
		return history

def writeHistory(str, date, time):
	if (str != None and str != ""):
		with open('history.json') as infile:
			history = json.load(infile)
			with open('history.json', 'w') as outfile:
				history.append({
					"date": date, 
					"time": time, 
					"task": str
				})
				json.dump(history, outfile)
		

@click.command()
@click.argument('arg1', required = False)
@click.argument('arg2', required = False)
def main(arg1, arg2):
	if (isRead(arg1, arg2)):
		for task in readHistory():
			click.echo(task['time'] + ' ' + task['task'])
	else:
		local_time = time.asctime( time.localtime(time.time()) )
		date_readable = local_time[4:10] + local_time[19:]
		time_readable = local_time[10:16]
		writeHistory(arg1, date_readable, time_readable)




