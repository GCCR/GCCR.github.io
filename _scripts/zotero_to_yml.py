#!/usr/bin/env python

from pyzotero import zotero
import yaml
import re
import os
from datetime import datetime

ZOTERO_KEY = os.environ["ZOTERO_KEY"]

z = zotero.Zotero(library_id=2503085, library_type="group", api_key=ZOTERO_KEY)

COVID = re.compile(r'\bcovid|\bcoronavirus\b|\bsars\b')
SMELL = re.compile(r'\bolfact|\bsmell\b|osmia\b')
TASTE = re.compile(r'\bgustat|\btaste\b|geusia\b')
CASE_REPORT = re.compile(r'\bcase\-?report\b')
VIRAL = re.compile(r'\bviral\b')
PREPRINT = re.compile(r'\bpreprint\b')
GENES = re.compile(r'\bgenes?\b|\bgenetic\b')

def get_tags(tags):
    """Convert a dict of Zotero tags to a standardized list of tags"""
    norm = []
    tags = " ".join(item["tag"] for item in tags).lower()
    for regex, tag in [
        (COVID, "covid19"),
        (SMELL, "smell"),
        (TASTE, "taste"),
        (CASE_REPORT, "case-report"),
        (VIRAL, "viral"),
        (PREPRINT, "preprint"),
        (GENES, "genes"),
    ]:
        if re.search(regex, tags):
            norm.append(tag)
    return norm

publications = []

for item in z.everything(z.items(sort="dateAdded", direction="desc")):
    if item["data"].get("itemType") != "journalArticle":
        continue
    data = {key: item["data"].get(key) for key in [
        "title", "creators", "publicationTitle", "journalAbbreviation", "date", "dateAdded", "DOI", "tags",
    ]}
    # abbreviate list of authors
    authors = data.pop("creators")
    firstname = '. '.join(name[0] if len(name) else name
                          for name in authors[0]['firstName'].split())
    name = f"{authors[0]['lastName']}, "{firstname}."
    name += " et al." if len(authors) > 1 else ""
    data["authors"] = name
    # abbreviate journal name if available
    long_name, short_name = data.pop("publicationTitle"), data.pop("journalAbbreviation")
    data["journal"] = short_name if short_name else long_name
    # extract year from date field
    year = re.findall(r'[1,2][0,9]\d{2}', data.pop("date"))
    if year:
        data["year"] = int(year[0])
    # prepare tags
    tags = data.pop("tags")
    if tags:
        data["tags"] = get_tags(tags)
        if not data["tags"]:
            data.pop("tags")
    # prepare to write
    if not data["DOI"]:
        data.pop("DOI")
        print(f"[WARNING] No DOI: {list(data.values())}")
    if not data["journal"]:
        print(f"[ERROR] No journal: {list(data.values())}")
        continue
    publications.append(data)

with open("_data/literature.yml", "w") as f:
    yaml.dump(publications, f)

with open("_data/last_update.yml", "w") as f:
    last_update = datetime.strptime(publications[0]["dateAdded"],
                                    "%Y-%m-%dT%H:%M:%SZ")
    f.write(last_update.strftime("%B %d, %Y"))