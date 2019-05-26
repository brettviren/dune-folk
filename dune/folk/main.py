#!/usr/bin/env python3
'''
CLI for dorking with DUNE collaboration info
'''

import re
import csv
import click

from . import exports

@click.group()
def cli():
    pass


@cli.command("search")
@click.option("-o","--output", default="/dev/stdout",
              help="Give output file or stdout will be used")
@click.option("-t","--template", default="{first-name} {last-name} {email}",
              help="Provide output format template to print matches")
@click.option("-e","--export", default=None,
              type=click.Choice(exports.known_csv),
              help="Export data to a format of some application")
@click.argument("patterns", nargs=-1)
@click.argument("csvfile", nargs=1)
def search(template, output, export, patterns, csvfile):
    '''
    Search for an entry in the CSV file by keywords.

    Patterns is in form: "<key>=<regex>".  Key is a CSV column name.
    Column names aliased to lower-case when spaces replaced by "-" and
    additionally by first word lower cased.  Multiple patterns imply
    logical AND.  If no patterns are given, all records are matched.
    '''

    dat = csv.DictReader(open(csvfile))
    namemap = {n.lower().replace(' ','-'):n for n in dat.fieldnames}
    namemap.update({n.lower().split()[0]:n for n in dat.fieldnames})
    namemap.update({n:n for n in dat.fieldnames})

    lu = dict()
    for pat in patterns:
        key,reg = pat.split("=",1);
        lu[key] = re.compile(reg)
    if not lu:
        lu['first'] = re.compile('.*')

    records = list()
    for rec in dat:
        found = False

        for key,reg in lu.items():
            one = rec[namemap[key]]
            if not reg.match(one):
                continue
            found = True

        if not found:
            continue

        pdat = dict()
        for nk, nv in namemap.items():
            pdat[nk] = rec[nv]
        records.append(pdat)
    
    if export:
        if export in exports.known_csv:
            desc = getattr(exports, export)
            text = exports.csv(records, **desc)
    else:
        text = exports.formatter(records, template)

    open(output, 'w').write(text)

    
            
            
def main():
    cli(obj={})

    
