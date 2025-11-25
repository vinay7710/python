def solution (recording):
    """Count how many time the user changed keys while typing the sequence.uppercase and lowercase of the same letter are treated as the same key
    Args:
        recording(list[str]):list of single-letter strings (A-Z or a-z)
    Retuns:
    int:number of key changes (number of consecutive pairs where keys difer)"""
    if not recording:
        return 0
    changes = 0
    prev_key = recording[0].lower()
    for ch in recording[1:]:
        curr_key = ch.lower()
        if curr_key != prev_key:
            changes += 1
        prev_key = curr_key
        return changes
    # Example tests from the prompt:
    example1 =['W', 'w', 'a', 'A', 'a', 'b', 'B']
    example2 = ['w', 'w', 'a', 'w', 'a',]

    print(solution(example1))  
    #2 (note:the prompt contains a conflicting '3' value; correct is 2)
    print(solution(example2))