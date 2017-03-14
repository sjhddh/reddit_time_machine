# In case of ASCII horror,
# need to get rid of this in the future.

def ascii_saver(s):
    try:
        s = s.encode('ascii', errors='ignore')
    except:
        print('ascii cannot save', s)
    return s
