#!/usr/bin/env python3

import sys
import os
import json
from pathlib import Path


myname_ja = ["須藤 克仁", "須藤克仁"]
myname_en = ["Katsuhito Sudoh"]


def publication_date(obj):
    if 'publication_date' in obj:
        return tuple(map(int, obj['publication_date'].split("-")))
    else:
        return None


def main():
    script = Path(__file__).resolve()
    project_root = script.parent.parent
    outdir_ja = project_root / 'content' / 'ja' / 'research' / '_publications'
    outdir_en = project_root / 'content' / 'en' / 'research' / '_publications'

    source_dir = project_root / '.local'
    jsonl_files = sorted(source_dir.glob('*.jsonl'), key=os.path.getmtime, reverse=True)
    if not jsonl_files:
        raise FileNotFoundError(f"No researchmap JSONL file found in {source_dir}")
    jsonl = jsonl_files[0]

    DATA = {
            'journal': [],
            'reviewed_conf': [],
            'invited_talk': [],
            'unreviewed_conf': [],
            'domestic': [],
            'misc': []
            }

    with jsonl.open() as fp:
        for line in fp:
            obj = json.loads(line)
            data = obj['merge']
            if 'display' in data and data['display'] == 'disclosed':
                type = obj['insert']['type']
                if type == 'published_papers':
                    if data['published_paper_type'] == 'scientific_journal':
                        DATA['journal'].append(data)
                    elif data['published_paper_type'] == 'international_conference_proceedings':
                        if 'referee' in data and data['referee']:
                            DATA['reviewed_conf'].append(data)
                        else:
                            DATA['unreviewed_conf'].append(data)
                    else:
                        DATA['misc'].append(data)
                elif type == 'presentations' and data['invited']:
                    DATA['invited_talk'].append(data)
                elif type == 'misc':
                    if 'misc_type' in data and data['misc_type'] == 'summary_national_conference':
                        DATA['domestic'].append(data)
                    elif 'ja' in data['publication_name'] and ('大会' in data['publication_name']['ja'] or '研究会' in data['publication_name']['ja'] or '研究発表会' in data['publication_name']['ja']):
                        DATA['domestic'].append(data)
                    else:
                        DATA['misc'].append(data)
                elif type in ['misc', 'presentations']:
                    DATA['misc'].append(data)

    for type, datas in DATA.items():
        outfile_ja = outdir_ja / f"publication_{type}_ja.md_"
        outfile_en = outdir_en / f"publication_{type}_en.md_"
        with outfile_ja.open('wt') as ofp_ja, outfile_en.open('wt') as ofp_en:
            year = ''
            datas.sort(key=lambda x: publication_date(x), reverse=True)
            for data in datas:
                authors = data['authors'] if 'authors' in data else data['presenters']
                authors_ja = []
                if 'ja' in authors:
                    for _author in map(lambda x: x['name'], authors['ja']):
                        if _author in myname_ja: _author = "**" + _author + "**"
                        authors_ja.append(_author)
                authors_en = []
                if 'en' in authors:
                    for _author in map(lambda x: x['name'], authors['en']):
                        if _author in myname_en: _author = "**" + _author + "**"
                        authors_en.append(_author)
                authorstr_ja = ", ".join(authors_ja) if 'ja' in authors else ", ".join(authors_en)
                authorstr_en = ", ".join(authors_en) if 'en' in authors else ", ".join(authors_ja)

                title = data[list(filter(lambda x: x.endswith("_title"), data.keys()))[0]]
                titlestr_ja = title['ja'] if 'ja' in title else title['en']
                titlestr_en = title['en'] if 'en' in title else title['ja']

                link = ""
                if 'see_also' in data:
                    for seealso in data['see_also']:
                        if '@id' in seealso:
                            link += f" [[link]]({seealso['@id']})"
                            break

                publication = data['publication_name'] if 'publication_name' in data else data['event']
                publicationstr_ja = publication['ja'] if 'ja' in publication else publication['en']
                publicationstr_en = publication['en'] if 'en' in publication else publication['ja']

                tail = ""
                tail_en = ""

                tail += f", Vol. {data['volume']}" if 'volume' in data else ""
                tail += f", Vol. {data['number']}" if 'number' in data else ""
                tail += f", pp. {data['starting_page']}–{data['ending_page']}" if 'starting_page' in data and 'ending_page' in data else ""

                if 'publication_date' in data:
                    date = data['publication_date'].split("-")
                    tail += f", {date[0]}"
                    if year != date[0]:
                        year = date[0]
                        print (f"\n### **{year}**", file=ofp_ja)
                        print (f"\n### **{year}**", file=ofp_en)

                if 'languages' in data and 'jpn' in data['languages']:
                    tail_en += ' *(in Japanese)*'


                print (f"1. {authorstr_ja}, {titlestr_ja}, *{publicationstr_ja}*{tail}{link}", file=ofp_ja)
                print (f"1. {authorstr_en}, {titlestr_en}, *{publicationstr_en}*{tail}{tail_en}{link}", file=ofp_en)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        raise e
