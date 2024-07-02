#!/usr/bin/python3
""" method that determines if all the boxes can be opened """

def canUnlockAll(boxes):
    if not boxes:
        return False
    
    # Set to keep track of opened boxes
    opened = set()
    
    # Stack for DFS
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < len(boxes):
                    stack.append(key)
    
    # Check if all boxes are opened
    return len(opened) == len(boxes)
