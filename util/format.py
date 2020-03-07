
def asbool(val):
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    val = str(val).strip().lower()
    return val in ('t', 'true', 'y', 'yes', 'on', '1')

def asint(val, minimum=None, maximum=None):
    if val is None:
        val = 0
    val = int(val)
    val = min(val, maximum if maximum else val)
    val = max(val, minimum if minimum else val)
    return val


def aslist(val):
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return str(val).replace(' ', '').split(',')

def byte(val, fmt='{:.2f}'):
    for unit in ['', 'Ki', 'Mi', 'Gi']:
        if val < 1024.0:
            return '{}{}B'.format(fmt, unit).format(val)
        val /= 1024.0
    return '{}GiB'.format(fmt).format(val*1024.0)

def duration(duration, compact=False, unit=False):
    duration = int(duration)
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    suf = 'm'
    res = '{:02d}:{:02d}'.format(minutes, seconds)
    if hours > 0:
        if compact:
            res = '{:02d}:{:02d}'.format(hours, minutes)
        else:
            res = '{:02d}:{}'.format(hours, res)
        suf = 'h'

    return '{}{}'.format(res, suf if unit else '')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
