
from tokenizer import TokenType
def execute_tokens(tokens, my_drone):
    
    i = 0


    while i < len(tokens):
        token = tokens[i]

        if token.type == TokenType.MOVE:
            value = int(tokens[i + 1].lexeme)
            my_drone.forward(value)
            i += 2

        elif token.type == TokenType.TURN:
            direction = tokens[i + 1].lexeme
            value = int(tokens[i + 2].lexeme)

            if direction.upper() == "LEFT":
                my_drone.ccw(value)
            else:
                my_drone.cw(value)

            i += 3

        elif token.type == TokenType.FLIP:
            direction = tokens[i + 1].lexeme.lower()
            my_drone.flip(direction)
            i += 2

        elif token.type == TokenType.REPEAT:
            count = int(tokens[i + 1].lexeme)

            # Find block start
            i += 3  # skip REPEAT N [

            block_start = i
            depth = 1

            # find matching ]
            while depth > 0:
                if tokens[i].type == TokenType.LBRACKET:
                    depth += 1
                elif tokens[i].type == TokenType.RBRACKET:
                    depth -= 1
                i += 1

            block_end = i - 1

            block = tokens[block_start:block_end]

            for _ in range(count):
                execute_tokens(block, my_drone)

        else:
            i += 1