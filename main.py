import os
import time
import json
from art import tprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_track):
			extension = filename.split('.')
			if len(extension) > 1 and (extension[1].lower() in data['data'][0]['format']):
				file = folder_track + '/' + filename
				new_path = folder_dest + '/' + filename
				if not os.path.isfile(new_path):
					os.rename(file, new_path)
					print(f'[INFO] Файл {filename} перенесен в {folder_dest}')

tprint('sortfile')

with open('sort.json') as f:
	print('[!] Json файл загружен.')
	data = json.load(f)

folder_track = data['data'][0]['from']
folder_dest = data['data'][0]['to']
observer = Observer()

def main():
	handle = Handler()
	observer.schedule(handle, folder_track, recursive=True)
	observer.start()

if __name__ == '__main__':
	main()
	try:
		while(True): time.sleep(10)
	except KeyboardInterrupt: 
		print('[!] Завершение программы.')
		observer.stop()
	except FileExistsError:
		print('[!] Данный файл уже перенесен!')
	observer.join()