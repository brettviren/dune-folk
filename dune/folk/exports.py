#!/usr/bin/env python3
'''
Support for exporting to various formats.
'''

# export contacts, paste first line
gmail = dict(
    header = 'Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,E-mail 3 - Type,E-mail 3 - Value,E-mail 4 - Type,E-mail 4 - Value,IM 1 - Type,IM 1 - Service,IM 1 - Value,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Phone 4 - Type,Phone 4 - Value,Phone 5 - Type,Phone 5 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Organization 1 - Type,Organization 1 - Name,Organization 1 - Yomi Name,Organization 1 - Title,Organization 1 - Department,Organization 1 - Symbol,Organization 1 - Location,Organization 1 - Job Description,Website 1 - Type,Website 1 - Value',

    # map from gmail column name to folk format string
    keymap = {
        'Name':'{first-name} {last-name}',
        'Given Name':'{first-name}',
        'Additional Name':'{middle-name}',
        'Family Name':'{last-name}',
        'E-mail 1 - Type':'* Other',
        'E-mail 1 - Value':'{email}',
        'Organization 1 - Type':'Work',
        'Organization 1 - Name':'{primary-institution}',
        'Organization 1 - Location':'{primary-institution-country}',
        'Occupation':'{position}'
    },
)

outlook = dict(
    header = "First Name,Middle Name,Last Name,Title,Suffix,Initials,Web Page,Gender,Birthday,Anniversary,Location,Language,Internet Free Busy,Notes,E-mail Address,E-mail 2 Address,E-mail 3 Address,Primary Phone,Home Phone,Home Phone 2,Mobile Phone,Pager,Home Fax,Home Address,Home Street,Home Street 2,Home Street 3,Home Address PO Box,Home City,Home State,Home Postal Code,Home Country,Spouse,Children,Manager's Name,Assistant's Name,Referred By,Company Main Phone,Business Phone,Business Phone 2,Business Fax,Assistant's Phone,Company,Job Title,Department,Office Location,Organizational ID Number,Profession,Account,Business Address,Business Street,Business Street 2,Business Street 3,Business Address PO Box,Business City,Business State,Business Postal Code,Business Country,Other Phone,Other Fax,Other Address,Other Street,Other Street 2,Other Street 3,Other Address PO Box,Other City,Other State,Other Postal Code,Other Country,Callback,Car Phone,ISDN,Radio Phone,TTY/TDD Phone,Telex,User 1,User 2,User 3,User 4,Keywords,Mileage,Hobby,Billing Information,Directory Server,Sensitivity,Priority,Private,Categories",
    keymap = {
        'First Name':'{first-name}',
        'Middle Name':'{middle-name}',
        'Last Name':'{last-name}',
        'E-mail Address':'{email}',
        'Company':'{primary-institution}',
        'Business Country':'{primary-institution-country}',
        'Job Title':'{position}'
    }
)
known_csv = ["gmail","outlook"]
def csv(records, header, keymap):
    '''
    Convert DUNE folk records into canned contacts CSV formatted text.
    '''
    lines = [header]
    colnames = header.split(',')
    for rec in records:
        line=[]
        for cn in colnames:
            fform = keymap.get(cn, "")
            field = fform.format(**rec)
            line.append(field)
        lines.append(','.join(line))
    return '\n'.join(lines)



def formatter(records, format='"{first-name} {last-name} <{email}>"\n'):
    '''
    Format each record.
    '''
    lines = list()
    for rec in records:
        lines.append(format.format(**rec))
    return ''.join(lines)

