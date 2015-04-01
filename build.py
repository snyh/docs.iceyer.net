#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import markdown
import codecs

if __name__ == "__main__":
    print("Genarator mkdocs.yml")
    shutil.copyfile("mkdocs.yml.base","mkdocs.yml")

    fp = codecs.open("mkdocs.yml", mode="a+", encoding="utf-8")
    directory = "docs"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                path = root + "/" + file
                fmd = codecs.open(path, mode="r", encoding="utf-8")
                text = fmd.read()
                md = markdown.Markdown(extensions = ['meta'])
                md.convert(text)
                category = md.Meta["category"]
                title = md.Meta["title"]
                path = path.replace(directory+"/", "", 1)
                page_item = "    - ['" + path + "', '"+ category[0] + "', '" + title[0] + "']"
                print("Add:", page_item)
                fp.write(page_item+"\n")

    fp.close()
