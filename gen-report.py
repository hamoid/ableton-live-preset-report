#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import re, os, sys, gzip
from lxml import etree

path = "Presets/"

i = 0
# find folders
for folder in os.listdir(path):

    # find files in folders
    for fileName in os.listdir(path + folder):
        filePath = path + folder + "/" + fileName

        print(str(i) + ". " + filePath)

        # assuming all found files are .adv
        # so we gunzip them
        with gzip.open(filePath, 'rb') as f:
            fileContent = f.read()
           
            # parse content of the file as xml
            root = etree.fromstring(fileContent)

            # print file size
            print("  %s bytes" % len(fileContent))

            # find all ParameterList elements in the file
            parameters = root.find("MxDeviceInstrument").find("ParameterList").find("ParameterList").findall("./")

            # print parameter count
            print("  %s parameters" % len(parameters))

            # for each parameter, print the values we are interested in
            for parameter in parameters:
                # in this example, we filter Reverb parameters only.
                # we could get rid of this to show all parameters.
                if "Reverb" in parameter.find("Name").attrib["Value"]:
                    print("  %-20s %-20s %-15s %-15s %-15s" % (
                        parameter.tag, 
                        parameter.find("Name").attrib["Value"],
                        parameter.find("MinValue").attrib["Value"],
                        parameter.find("MaxValue").attrib["Value"],
                        parameter.find("Timeable").find("Manual").attrib["Value"]
                        ))

        
        i = i + 1
        print()
