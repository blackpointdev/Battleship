from src.Exceptions import IncorrectShipPlacement
import random

def coord_to_index(pos, segments):
    i = 0
    for segment in segments:
        if segment.get_rect().collidepoint(pos[0], pos[1]):
            return i
        i += 1

def validate_ship_position(segments, log, status, i):
    try:
        if i % 10 == 0:
            if i == 0:
                if (segments[1].status == -1 or segments[1].status == status) and \
                        (segments[10].status == -1 or segments[10].status == status) and \
                        segments[11].status == -1:

                    available = (1, 10)
                    return i, available
                else:
                    raise IncorrectShipPlacement

            elif i == 90:
                if (segments[91].status == -1 or segments[91].status == status) and \
                        segments[80].status == -1 or segments[90].status == status and \
                        segments[81].status == -1:

                    available = (80, 91)
                    return i, available
                else:
                    raise IncorrectShipPlacement

            else:
                if (segments[i-10].status == -1 or segments[i-10].status == status) and \
                        (segments[i + 10].status == -1 or segments[i+10].status == status) and \
                        segments[i - 9].status == -1 and segments[i + 11].status == -1  and \
                        (segments[i + 1].status == -1 or segments[i + 1].status == status):

                    available = (i - 10, i + 10, i + 1)
                    return i, available
                else:
                    raise IncorrectShipPlacement

        elif i % 10 == 9:
            if i == 9:
                if (segments[8].status == -1 or segments[8].status == status) and \
                        (segments[19].status == -1 or segments[19].status == status) and \
                        segments[18].status == -1:

                    available = (8, 19)
                    return i, available
                else:
                    raise IncorrectShipPlacement
            elif i == 99:
                if (segments[98].status == -1 or segments[98].status == status) and \
                        (segments[89].status == -1 or segments[89].status == status) and \
                        segments[88].status == -1:

                    available = (89, 98)
                    return i, available
                else:
                    raise IncorrectShipPlacement

            else:
                if (segments[i - 10].status == -1 or segments[i - 10].status == status) and \
                        (segments[i + 10].status == -1 or segments[i + 10].status == status) and \
                        segments[i + 9].status == -1 and segments[i - 11].status == -1 and \
                         (segments[i - 1].status == -1 or segments[i - 1].status == status):

                    available = (i - 10, i + 10, i - 1)
                    return i, available
                else:
                    raise IncorrectShipPlacement

        elif i > 0 and i < 10:
            if (segments[i - 1].status == -1 or segments[i - 1].status == status) and \
                    (segments[i + 1].status == -1 or segments[i + 1].status == status) and \
                    segments[i + 9].status == -1 and segments[i + 11].status == -1 and \
                    (segments[i + 10].status == -1 or segments[i + 10].status == status):

                available = (i - 1, i + 1, i + 10)
                return i, available
            else:
                raise IncorrectShipPlacement

        elif i > 90 and i < 100:
            if (segments[i + 1].status == -1 or segments[i + 1].status == status) and \
                    (segments[i - 1].status == -1 or segments[i - 1].status == status) and \
                    segments[i - 9].status == -1 and segments[i - 11].status == -1 and \
                    (segments[i - 10].status == -1 or segments[i - 10].status == status):

                available = (i + 1, i - 1, i - 10)
                return i, available
            else:
                raise IncorrectShipPlacement


        else:
            if (segments[i - 1].status == -1 or segments[i - 1].status == status) and \
                    (segments[i + 1].status == -1 or segments[i + 1].status == status) and \
                    (segments[i - 10].status == -1 or segments[i - 10].status == status) and \
                    (segments[i + 10].status == -1 or segments[i + 10].status == status) and \
                    segments[i - 11].status == -1 and segments[i + 11].status == -1 and \
                    segments[i - 9].status == -1 and segments[i + 9].status == -1:

                available = (i - 1, i + 1, i - 10, i + 10)
                return i, available
            else:
                raise IncorrectShipPlacement

    except IncorrectShipPlacement:
        log.print("Incorrect ship placement: ships cannot be connected.", (255, 0, 0))
        return -100, (-10, -10)


def spotted_shot(i):

    if i % 10 == 0:
        if i == 0:
            available = [1, 10]
            return available

        elif i == 90:
            available = [80, 91]
            return available

        else:
            available = [i - 10, i + 10, i + 1]
            return available

    elif i % 10 == 9:
        if i == 9:
            available = [8, 19]
            return available

        elif i == 99:
            available = [89, 98]
            return available

        else:
            available = [i - 10, i + 10, i - 1]
            return available

    elif i > 0 and i < 10:
        available = [i - 1, i + 1, i + 10]
        return available

    elif i > 90 and i < 100:
        available = [i + 1, i - 1, i - 10]
        return available

    else:
        available = [i - 1, i + 1, i - 10, i + 10]
        return available


def create_ship(board, size, ammount):
    for i in range(ammount):
        while True:
            remove = []
            while True:
                pos = random.randint(0, 99)
                if pos not in board.ships:
                    index, available = validate_ship_position(board.segments, board.log,
                                                              board.ship_status, pos)
                    if index >= 0:
                        break

            board.ships.append(index)
            board.segments[index].status = board.ship_status
            remove.append(index)

            error = False
            for k in range(size-1):
                for j in range(16):
                    direction = random.randint(0, len(available) - 1)
                    tmp, tmp2 = validate_ship_position(board.segments, board.log,
                                                       board.ship_status, available[direction])

                    if size != 2:
                        if tmp >= 0 and board.ships[-2] != available[direction]:
                            board.ships.append(available[direction])
                            board.segments[available[direction]].status = board.ship_status
                            remove.append(available[direction])
                            available = tmp2
                            break
                    else:
                        if tmp >= 0:
                            board.ships.append(available[direction])
                            board.segments[available[direction]].status = board.ship_status
                            remove.append(available[direction])
                            available = tmp2
                            break

                else:
                    error = True
                    for element in remove:
                        board.ships.remove(element)
                        board.segments[element].status = -1
                    break
            if not error:
                break

        board.ship_status += 1

        if size == 2:
            board.number_of_ships[0] -= 1
        elif size == 3:
            board.number_of_ships[1] -= 1
        elif size == 4:
            board.number_of_ships[2] -= 1
        elif size == 6:
            board.number_of_ships[3] -= 1