from src.Exceptions import IncorrectShipPlacement
from src.Ship import *

def validate_ship_position(segments, pos, log, status):
    try:
        i = 0
        for segment in segments:
            if segment.get_rect().collidepoint(pos[0], pos[1]):
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

                            available = (90, 91)
                            return i, available
                        else:
                            raise IncorrectShipPlacement

                    else:
                        if (segments[i-10].status == -1 or segments[i-10].status == status) and \
                                (segments[i + 10].status == -1 or segments[i+10].status == status) and \
                                segments[i - 9].status == -1 and segments[i + 11].status == -1  and \
                                (segments[i + 1].status == -1 or segments[i + 1].status == status):

                            available = (i - 10, i + 10, i - 1, i + 1)
                            return i, available
                        else:
                            raise IncorrectShipPlacement

                elif i % 10 == 9:
                    if i == 9:
                        if (segments[8].status == -1 or segments[8].status == status) and \
                                (segments[19].status == -1 or segment[19].status == status) and \
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

                            available = (i - 10, i + 10, i+1, i - 1)
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

            else:
                i += 1
    except IncorrectShipPlacement:
        log.print("Incorrect ship placement: ships cannot be connected.", (255, 0, 0))
        return -100, (-10, -10)