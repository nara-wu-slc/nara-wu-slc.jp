#!/usr/bin/env python3

import sys
import os
import json
from pathlib import Path


myname_ja = ["須藤 克仁", "須藤克仁"]
myname_en = ["Katsuhito Sudoh"]

CATEGORIES = {
    'journal': {
        'slug': 'journals',
        'title_ja': '学術論文誌',
        'title_en': 'Journal Articles',
        'description_ja': '学術論文誌に掲載された研究業績を年別に掲載しています。',
        'description_en': 'Peer-reviewed journal articles listed by year.',
        'weight': 1,
    },
    'reviewed_conf': {
        'slug': 'reviewed-conferences',
        'title_ja': '査読つき国際会議・ワークショップ',
        'title_en': 'Peer-Reviewed Conference and Workshop Papers',
        'description_ja': '査読つき国際会議・ワークショップの研究業績を年別に掲載しています。',
        'description_en': 'Peer-reviewed international conference and workshop papers listed by year.',
        'weight': 2,
    },
    'invited_talk': {
        'slug': 'invited-talks',
        'title_ja': '招待講演等',
        'title_en': 'Invited Talks',
        'description_ja': '招待講演などの研究業績を年別に掲載しています。',
        'description_en': 'Invited talks and related presentations listed by year.',
        'weight': 3,
    },
    'unreviewed_conf': {
        'slug': 'unreviewed-conferences',
        'title_ja': '査読なし国際会議・ワークショップ',
        'title_en': 'Non-Peer-Reviewed Conference and Workshop Papers',
        'description_ja': '査読なし国際会議・ワークショップの研究業績を年別に掲載しています。',
        'description_en': 'Non-peer-reviewed international conference and workshop papers listed by year.',
        'weight': 4,
    },
    'domestic': {
        'slug': 'domestic-meetings',
        'title_ja': '全国大会・研究会等',
        'title_en': 'Domestic Conference and Research Meeting Papers',
        'description_ja': '国内の全国大会・研究会などの研究業績を年別に掲載しています。',
        'description_en': 'Domestic conference and research meeting papers listed by year.',
        'weight': 5,
    },
    'misc': {
        'slug': 'miscellaneous',
        'title_ja': 'その他',
        'title_en': 'Other Publications and Research Activities',
        'description_ja': 'その他の研究業績を年別に掲載しています。',
        'description_en': 'Other publications and research activities listed by year.',
        'weight': 6,
    },
}


def publication_date(obj):
    if 'publication_date' in obj:
        return tuple(map(int, obj['publication_date'].split("-")))
    else:
        return None


def main():
    script = Path(__file__).resolve()
    project_root = script.parent.parent
    outdir_ja = project_root / 'content' / 'ja' / 'research' / 'publications'
    outdir_en = project_root / 'content' / 'en' / 'research' / 'publications'
    outdir_ja.mkdir(parents=True, exist_ok=True)
    outdir_en.mkdir(parents=True, exist_ok=True)

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
                record_type = obj['insert']['type']
                if record_type == 'published_papers':
                    if data['published_paper_type'] == 'scientific_journal':
                        DATA['journal'].append(data)
                    elif data['published_paper_type'] == 'international_conference_proceedings':
                        if 'referee' in data and data['referee']:
                            DATA['reviewed_conf'].append(data)
                        else:
                            DATA['unreviewed_conf'].append(data)
                    else:
                        DATA['misc'].append(data)
                elif record_type == 'presentations' and data.get('invited'):
                    DATA['invited_talk'].append(data)
                elif record_type == 'misc':
                    if 'misc_type' in data and data['misc_type'] == 'summary_national_conference':
                        DATA['domestic'].append(data)
                    elif 'ja' in data['publication_name'] and ('大会' in data['publication_name']['ja'] or '研究会' in data['publication_name']['ja'] or '研究発表会' in data['publication_name']['ja']):
                        DATA['domestic'].append(data)
                    else:
                        DATA['misc'].append(data)
                elif record_type in ['misc', 'presentations']:
                    DATA['misc'].append(data)

    for category, datas in DATA.items():
        metadata = CATEGORIES[category]
        outfile_ja = outdir_ja / f"{metadata['slug']}.md"
        outfile_en = outdir_en / f"{metadata['slug']}.md"
        with (
            outfile_ja.open('wt', encoding='utf-8') as ofp_ja,
            outfile_en.open('wt', encoding='utf-8') as ofp_en,
        ):
            print('+++', file=ofp_ja)
            print(f"identifier = 'research_publications_{category}'", file=ofp_ja)
            print(f"title = '{metadata['title_ja']}'", file=ofp_ja)
            print(f"description = '{metadata['description_ja']}'", file=ofp_ja)
            print("type = 'docs'", file=ofp_ja)
            print("icon = 'fa-solid fa-file-lines'", file=ofp_ja)
            print("parent = 'research_publications'", file=ofp_ja)
            print(f"weight = {metadata['weight']}", file=ofp_ja)
            print('hide_summary = true', file=ofp_ja)
            print('+++', file=ofp_ja)

            print('+++', file=ofp_en)
            print(f"identifier = 'research_publications_{category}'", file=ofp_en)
            print(f"title = '{metadata['title_en']}'", file=ofp_en)
            print(f"description = '{metadata['description_en']}'", file=ofp_en)
            print("type = 'docs'", file=ofp_en)
            print("icon = 'fa-solid fa-file-lines'", file=ofp_en)
            print("parent = 'research_publications'", file=ofp_en)
            print(f"weight = {metadata['weight']}", file=ofp_en)
            print('hide_summary = true', file=ofp_en)
            print('+++', file=ofp_en)

            year = ''
            datas.sort(key=lambda x: publication_date(x) or (0, 0, 0), reverse=True)
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
                tail += f", No. {data['number']}" if 'number' in data else ""
                tail += f", pp. {data['starting_page']}–{data['ending_page']}" if 'starting_page' in data and 'ending_page' in data else ""

                if 'publication_date' in data:
                    date = data['publication_date'].split("-")
                    tail += f", {date[0]}"
                    if year != date[0]:
                        year = date[0]
                        print(f"\n## {year}", file=ofp_ja)
                        print(f"\n## {year}", file=ofp_en)

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
