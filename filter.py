#! /usr/bin/python
import sys
import os
import codecs
import re

################################################################################
# Usage
################################################################################
class FileFilter():
  def __init__(self, aInputFilePath, aSeparator, aOutputFilePath):
    print "aInputFilePath:%s" % (aInputFilePath)
    print "aSeparator:%s" % (aSeparator)
    print "aOutputFilePath:%s" % (aOutputFilePath)

    # Open result file
    resultFileSuffix = "_filtered.txt"
    self._resultFile = codecs.open(aOutputFilePath + resultFileSuffix, "w", "utf-8")

    self._lineNumber = 0

    file = open(aInputFilePath)
    for query in file:
      self._lineNumber += 1

      if ("#" == query[0]) or (";" == query[0]):
        # print "\nSkip [%d]:%s" % (self._lineNumber, query)
        continue

      query = query.strip()
      if (query == ''):
        print "\nSkip empty line [%d]" % (self._lineNumber)
        continue
      # print "\n[%d]:%s" % (self._lineNumber, query)

      # Filter out Non-Chinese lines in POI dump format
      if (self.GetIsCompressedPoiHeader(query)):
        print "Skip Compressed Poi Header [%d]:%s" % (self._lineNumber, query)
        continue;

      # Re-Construct the input query string
      self._inputList = query.split(aSeparator, 13)
      poiName = self._inputList[1].strip(' ')
      # Non-Chinese query string will be skipped
      if (self.HasChineseCharacter(poiName) == False):
        # print "Skip Compressed Poi Header Non-Chinese [%d]:%s" % (self._lineNumber, query)
        continue;
      # Write this query line to new file
      print >> self._resultFile, "%s" % (query.decode('utf-8'))

  def GetIsCompressedPoiHeader(self, aString):
    if (aString[0].isdigit() == False):
      return True;
    else:
      return False;

  def HasChineseCharacter(self, aString):
    for char in aString.decode('utf-8'):
      if (char >= u'\u4e00' and char <= u'\u9fff'):
        return True
    return False;

def show_usage():
  print "Usage: ", sys.argv[0], "<InputFilePath> <Separator, e.g. '|', ';', ',', etc.> <OutputFilePath>"

# ----------------------------------
# -------------- Main --------------
# ----------------------------------
if __name__ == "__main__":
  if len(sys.argv) < 4:
    show_usage()
    sys.exit(1)

  inputFilePath = sys.argv[1]
  if (os.path.isfile(inputFilePath) == False):
    print "Please input a correct file path..."
    show_usage()
    sys.exit(1)

  separator = sys.argv[2]
  if (len(separator) != 1):
    print "Invalid separator length..."
    show_usage()
    sys.exit(1)

  outputFilePath = sys.argv[3]

  FileFilter(inputFilePath, separator, outputFilePath)

