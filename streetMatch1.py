import pandas as pd
import re

from address import Address

# Matches string to a database of streets


def streetMatcher(dataFrame):
    final = []
    mistakes = []
    #dataFrame = pd.read_pickle('ccities')
    #streetTable()

    #Get each row of dataframe with corrected cities
    for index, row in dataFrame.iterrows():

        street = row['Street']
        # Get valid addresses from city and street info.
        address = Address(street=street, city='PROVIDENCE')
        address.set_addr_matches(cutoff=80, limit=1)

        for addr, city, score in address.addr_matches:

            if city == 'N/A':
                mistakes.append({
                    'Street': addr,
                    'Drop_Reason': score,
                    'File_List': row['File_List'],
                    'Text': row['Text'],
                    })
            else:
                final.append({
                    'Address': addr,
                    'City': city,
                    'Conf._Score': score,
                    'Header': row['Header'],
                    'File_List': row['File_List'],
                    'Text': row['Text'],
                    'Company_Name': row['Company_Name']
                })

    final = pd.DataFrame(final)
    drops = pd.DataFrame(mistakes)
    drops.to_csv('drops_address.csv', sep = ',')

    return final