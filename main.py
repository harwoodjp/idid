import click, json

@click.command()
@click.argument('arg1')
def main(arg1):
	with open('history.json', 'w') as history_json:
		history = json.load(history_json)
		if arg1 == "what":
			for task in history:
				click.echo(task['task'])
		else:
			history.append({'task': arg1})
			click.echo(history)
			json.dump(history, history_json, ensure_ascii=False)

