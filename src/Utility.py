from src.Exceptions import IncorrectShipPlacement
from src.Ship import *

def validate_ship_position(segments, pos, log):
    try:
        i = 0
        for segment in segments:
            if segment.get_rect().collidepoint(pos[0], pos[1]):
                if i % 10 == 0:
                    if i == 0:
                        if (segments[1].status == -1 or segments[1].status == segment.status) and \
                                (segments[10].status == -1 or segments[10].status == segment.status) and \
                                segments[11].status == -1:
                            return segment  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement
                    elif i == 90:
                        if (segments[91].status == -1 or segments[91].status == segment.status) and \
                                segments[80].status == -1 or segments[90].status == segment.status and \
                                segments[81].status == -1:
                            segments[i].status = True  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement
                    else:
                        if not segments[i - 10].is_active and not segments[i + 10].is_active \
                                and not segments[i - 9].is_active and not segments[i + 11].is_active \
                                and not segments[i + 1].is_active:
                            segments[i].is_active = True  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement
                elif i % 10 == 9:
                    if i == 9:
                        if not segments[8].is_active and not segments[19].is_active and not \
                                segments[18].is_active:
                            segments[i].is_active = True  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement
                    elif i == 99:
                        if not segments[98].is_active and not segments[89].is_active and not \
                                segments[88].is_active:
                            segments[i].is_active = True  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement
                    else:
                        if not segments[i - 10].is_active and not segments[i + 10].is_active \
                                and not segments[i + 9].is_active and not segments[i - 11].is_active \
                                and not segments[i - 1].is_active:
                            segments[i].is_active = True  # TODO Creation of new ship here
                        else:
                            raise IncorrectShipPlacement

                elif i > 0 and i < 10:
                    if not segments[i - 1].is_active and not segments[i + 1].is_active \
                            and not segments[i + 9].is_active and not segments[i + 11].is_active \
                            and not segments[i + 10].is_active:
                        segments[i].is_active = True  # TODO Creation of new ship here
                    else:
                        raise IncorrectShipPlacement

                elif i > 90 and i < 100:
                    if not segments[i + 1].is_active and not segments[i - 1].is_active \
                            and not segments[i - 9].is_active and not segments[i - 11].is_active \
                            and not segments[i - 10].is_active:
                        segments[i].is_active = True  # TODO Creation of new ship here
                    else:
                        raise IncorrectShipPlacement

                else:
                    if not segments[i - 1].is_active and not segments[i + 1].is_active \
                            and not segments[i - 10].is_active and not segments[i + 10].is_active \
                            and not segments[i - 11].is_active and not segments[i + 11].is_active \
                            and not segments[i - 9].is_active and not segments[i + 9].is_active:
                        segments[i].is_active = True  # TODO Creation of new ship here
                    else:
                        raise IncorrectShipPlacement
            else:
                i += 1
    except IncorrectShipPlacement:
        log.print("Incorrect ship placement: ships cannot be connected.")