from importlib import import_module

def display_text(scene, dialogue_number):
    dialogues = getattr(import_module(scene), "dialogues")
    if dialogue_number+2>=len(dialogues):
        dialogue_number = len(dialogues)-1-2
    return [dialogues[dialogue_number], dialogues[dialogue_number+1], dialogues[dialogue_number+2]]
    