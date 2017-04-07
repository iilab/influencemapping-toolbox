import os
import yaml
import requests
from StringIO import StringIO
from pprint import pprint
from normality import slugify
import unicodecsv

DATA = os.path.join(os.path.dirname(__file__), '..', 'data')

SECTION = {
    'projects': 'https://docs.google.com/spreadsheets/d/1j2hl7TlGGoKmO5EVkibU1LASk9p1ncmimI7-26JFX1g/pub?gid=0&single=true&output=csv',  # noqa
    'tools': 'https://docs.google.com/spreadsheets/d/1j2hl7TlGGoKmO5EVkibU1LASk9p1ncmimI7-26JFX1g/pub?gid=1475648190&single=true&output=csv'  # noqa
}

RENAMES = {
    'home_page': 'home_url',
    'url': 'home_url',
    'keywords': 'tags',
    'does_the_project_have_a_twitter_account': 'twitter_account'
}

SPLIT_FIELDS = ['tags', 'partners', 'commissioners', 'data_export_formats', 'data_import_formats']


def dump_yaml(fh, data):
    data = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, indent=2, encoding='utf-8')
    fh.write(data)


for outdir, url in SECTION.items():
    res = requests.get(url)
    sio = StringIO(res.content)
    # with open(os.path.join(DATA, '%s.csv' % section), 'r') as fh:
    for row in unicodecsv.DictReader(sio):
        data = {}
        for k, v in row.items():
            v = v.strip()
            if not len(v):
                continue
            elif v.lower() == 'n/a':
                continue
            k = k.replace("'", '')
            nk = slugify(k, sep='_')
            nk = RENAMES.get(nk, nk)
            if nk in data:
                raise ValueError(nk, k)
            if v.lower() == 'yes':
                v = True
            elif v.lower() == 'no':
                v = False
            if nk in SPLIT_FIELDS:
                v = [x.strip() for x in v.split(',') if len(x.strip())]
            data[nk] = v
        urlslug = slugify(data.get('name'), sep='-')
        if urlslug is None or not len(urlslug):
            print [data.get('name'), urlslug]
            continue
        fileslug = slugify(data.get('name'), sep='_')
        # data['layout'] = outdir.replace('s', '')
        data['title'] = data.pop('name')
        outfile = os.path.join(os.path.dirname(__file__), '..',
                               '_%s' % outdir, '%s.md' % fileslug)
        with open(outfile, 'w') as fh:
            fh.write('---\n')
            # text = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, encoding='utf-8')
            # print len(text)
            dump_yaml(fh, {'title': data.pop('title', None)})
            # dump_yaml(fh, {'layout': data.pop('layout', None)})
            dump_yaml(fh, {'description': data.pop('description', '')})
            dump_yaml(fh, {'url': data.pop('url', '')})
            dump_yaml(fh, {'tags': data.pop('tags', [])})
            if len(data):
                dump_yaml(fh, data)
            fh.write('---\n')
