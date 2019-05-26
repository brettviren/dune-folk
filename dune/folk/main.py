#!/usr/bin/env python3
'''
CLI for dorking with DUNE collaboration info
'''

import re
import csv
import click

@click.group()
def cli():
    pass


@cli.command("search")
@click.option("-f","--format", default="{first-name} {last-name} {email}",
              help="Provide output format to print matches")
@click.argument("patterns", nargs=-1)
@click.argument("csvfile", nargs=1)
def search(format, patterns, csvfile):
    '''
    Search for an entry in the CSV file by keywords.

    Patterns is in form: "<key>=<regex>".  Key is a CSV column name.
    Column names aliased to lower-case when spaces replaced by "-" and
    additionally by first word lower cased.  Multiple patterns imply
    logical AND.
    '''
    dat = csv.DictReader(open(csvfile))
    namemap = {n.lower().replace(' ','-'):n for n in dat.fieldnames}
    namemap.update({n.lower().split()[0]:n for n in dat.fieldnames})
    namemap.update({n:n for n in dat.fieldnames})

    lu = dict()
    for pat in patterns:
        key,reg = pat.split("=",1);
        lu[key] = re.compile(reg)

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
        click.echo(format.format(**pdat))
    
            
            
def main():
    cli(obj={})

    
