#!/usr/bin/python
# coding=utf-8
import os
import fnmatch
import sys
import time
import subprocess

filePathIn = raw_input("Enter file directory path: ")
filePath = filePathIn.rstrip()
filePath = filePath.replace("\\", "")
outputPathIn = str(object=raw_input("Enter output path: "))
outputPath = outputPathIn.rstrip()
if outputPath[-1:] == "/":
	outputPath = outputPath[:-1]
rawFiles = []
files = []
fileNames = []
total = 0

rawFiles = [
	os.path.join(dirpath, f)
	for dirpath, dirnames, filenames in os.walk(filePath)
	for f in fnmatch.filter(filenames, "*.mkv")  # edit here for another file format
]

for file in rawFiles:
	if file.endswith("sample.mkv"):
		print "Ignoring sample file: " + file
	else:
		print "File found: " + file
		fileNames.append(file.replace(filePath, ""))
		files.append(file)

if (len(files) == 0):
	print "There are no .mkv files in this directory."
else:
	s = 0
	while (s < len(files)):
		durationSec = subprocess.check_output("ffprobe -i \'" + filePath + os.sep + fileNames[s] + "\' -show_format -v quiet | sed -n 's/duration=//p'", shell=True)
		duration = durationSec.split(".")
		duration = duration[0]
		newDirCommand = "mkdir -p \'" + outputPath + "/" + fileNames[s][:-4][1:] + "\'"
		os.system(newDirCommand)
		s += 1
		i = 0
		durations = []
		while (i < 3):
			i += 1
			print "Creating screenshots of " + fileNames[s - 1] + "... (" + str(object=i) + "/3)"
			int(i)
			durations.insert(i - 1, ((int(duration) / 4) * i + 1))
			str(object=i)
			inPath = files[s - 1]
			outPath = outputPath + fileNames[s - 1][:-4] + os.sep
			newCommand = "ffmpeg -ss " + str(object=durations[i - 1]) + " -i \'" + inPath + "\' -vframes 1 -v quiet \'" + outPath + "img-" + str(object=i) + ".png\'"
			process = subprocess.call(newCommand, shell=True)
			total += 1
			int(i)

print "Done. Total number of screenshots: %i" % total
