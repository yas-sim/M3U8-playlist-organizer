# Description
A simple, small Python script to organize the music playlist file in M3U8 format (which can be found in some music player software or music player device such as SONY Walkman series).  
The program sorts entries and remove duplicated entries.  
Output file name is fixed to '`output.m3u8`'.  

SONYのWalkmanやミュージックプレイヤーソフトなどで使われる.m3u8フォーマットのプレイリストをソートし、重複エントリーを削除するプログラムです。  
出力ファイル名は'`output.m3u8`'に固定です。  
Walkmanでプレイリストに適当に追加していくと、重複チェックしてくれないので同じ曲が複数入ってしまうんですよね。なので、ちょっと暇つぶしを兼ねて書いたスクリプトです。  

## How it works
The program is written in Python3 and platform agnostic. Just run the script with input .m3u8 filename, and you'll get '`output.m3u8`' file with entry sort and duplicate rejection.  

```sh
python3 m3u8_organizer.py input.m3u8
```
