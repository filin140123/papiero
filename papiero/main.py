from time import sleep
import json
import os
from datetime import datetime as dt

menu_msg = "1. Create a note\n"\
           "2. List of notes\n"\
           "0. Exit"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu_msg)
    action = input('---> Enter a number: ')
    if action == '1':
        # creating a note
        nm = input('Name: ')
        note = input('#: ')
        tp = dt.now().strftime('%c')
        with open('papers.json', 'r', encoding='utf-8') as jf:
            obj = json.load(jf)
        with open('papers.json', 'w', encoding='utf-8') as jf:
            obj.append({'name': nm, 'body': note, 'timepoint': tp})
            json.dump(obj, jf)
        print('Saved!')
        sleep(1)

    elif action == '2':
        # list notes, view or delete a note
        with open('papers.json', 'r', encoding='utf-8') as jf:
            papers = json.load(jf)
        for i in papers:
            print('>', end=' ')
            print(i['name'])
        to_open = input("Enter name of the note (or 'back' to return)\n"
                        "...or print '!' before name to delete the note: ")
        if to_open:
            if to_open == 'back':
                continue
            delete = False
            for idx, i in enumerate(papers):
                if to_open[0] == '!':
                    delete, to_open = True, to_open[1:]
                if to_open == i['name'] and not delete:
                    print(f"\n--- {i['name']} ---")
                    print(i['body'])
                    print(f"--- {i['timepoint']} ---\n")
                    input('> Any key to return back...')
                    break
                elif to_open == i['name'] and delete:
                    del papers[idx]
                    with open('papers.json', 'w', encoding="utf-8") as jf:
                        json.dump(papers, jf)
                    print("Deleted!")
                    sleep(1)
                    break
            else:
                input("> Note not found. Any key to return back...")
    elif action == '0':
        print("Exiting...")
        sleep(1)
        quit()
