import sys
import numpy as np
import pandas as pd

print('*** .M3U8 play list file organizer (sort and remove duplicates)')

if len(sys.argv)<2:
    print('Please specify .M3U8 file to process')
    sys.exit(-1)
fileName = sys.argv[1]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.DataFrame()

with open(fileName, 'rt', encoding='utf8') as f:
    for line in f:
        if line[:7] == "#EXTINF":
            items = f.readline().rstrip('\n').split('/')
            artist = items[0]
            file = items[-1]
            path = items[0]
            for p in items[1:-1]:
                path += '/' + p
            df = df.append({'artist':artist, 'path':path, 'file':file}, ignore_index=True)

original_len = len(df)
df = df.sort_values(['artist', 'file'])
df = df.drop_duplicates()
unique_len = len(df)
playList = df.to_numpy().tolist()

outputFileName = 'output.m3u8'
with open(outputFileName, 'wt', encoding='utf8') as f:
    print('#EXTM3U', file=f)
    for items in playList:
        print('#EXTINF:,', file=f)
        print('{}/{}'.format(items[2], items[1]), file=f)

print('{} entries are written to {} ({} duplicates removed)'.format(unique_len, outputFileName, original_len-unique_len))
