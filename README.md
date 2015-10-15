# tool_line_filter
A python tool to filter out unwant lines in dump csv text file.  

# Usage:
```
./filter.py 
Usage:  ./filter.py <InputFilePath> <Separator, e.g. '|', ';', ',', etc.> <OutputFilePath>
```
The <OutputFilePath> will be appended a suffix "_filtered.txt"  

# Example:
```
./filter.py TestDatas/test-China-All-Poi.dmp ',' TestDatas/test-China-All-Poi.dmp
aInputFilePath:TestDatas/test-China-All-Poi.dmp
aSeparator:,
aOutputFilePath:TestDatas/test-China-All-Poi.dmp
Skip Compressed Poi Header [1]:Category ID, Name, Address, Phone, X, Y, HasIcon, Icon, RichInfoType, IsCamera, Speed, SpeedType, CameraType, ByteOffset
```
Before filtered:  
```
Category ID, Name, Address, Phone, X, Y, HasIcon, Icon, RichInfoType, IsCamera, Speed, SpeedType, CameraType, ByteOffset
7310, 正新轮胎, , , 10004923, 2169670, NoIcon, 0, NoAdditionalInformation, NoCamera, , , , 25589
7310, Zhengxin Tires, , , 10004923, 2169670, NoIcon, 0, NoAdditionalInformation, NoCamera, , , , 25607
```
After filtered:  
```
7310, 正新轮胎, , , 10004923, 2169670, NoIcon, 0, NoAdditionalInformation, NoCamera, , , , 25589
```
