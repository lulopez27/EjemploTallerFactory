from Memento import *

if __name__ == "__main__":        

    editor = Editor()
    history = History()

    while 1:

        new_content = input(">>")

        if new_content == "/undo":
            
            last_state = history.pop()
            editor.undo(last_state)

        elif new_content == "/close":
            break

        
        else:
            new_state = editor.save_state()
            history.push(new_state)

            current_content = editor.get_content()

            editor.set_content(current_content + "\n" + new_content)


        print(editor.get_content())




