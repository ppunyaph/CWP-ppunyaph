def checkmate(board:str):
    kln=[]
    for ln in board.strip().split('\n'):
        if ln:
         kln.append(ln)
    if not kln:
     print("Fail")
     return
    
    Size = len(kln)
    King = None
    for r in range(Size):
        for c in range(Size):
            if kln[r][c] == 'K':
                King = (r, c)
                break
        if King:
            break
    if not King:
        print("Fail")
        return
    kr, kc = King
    pawn_atk = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for r, c in pawn_atk:
        if 0 <= r < Size and 0 <= c < Size:
            if kln[r][c] == 'P':
                print("Success")
                return
            
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < Size and 0 <= c < Size:
            piece = kln[r][c]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < Size and 0 <= c < Size:
            piece = kln[r][c]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")