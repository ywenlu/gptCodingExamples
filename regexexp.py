import re

def extract_birthday(text):
    """
    Extracts the date of birth from a given text in French format. The function uses a regular expression pattern to match the date of birth in the text. The date is returned in the format YYYY-mm-dd. If the date of birth is not found in the text, the function returns None.
    PROMPT: Please generate me a birthday generation function that contains regex that can extract date of birth of person in French, the format can be in text or number, return the extrected date in YYYY-mm-dd format
    
    Args:
        text (str): The text to extract the date of birth from.
    
    Returns:
        str: The date of birth in the format YYYY-mm-dd or None if the date of birth is not found in the text.
    
    """
    # regex pattern to match date of birth in French
    pattern = r"(?P<day>\d{1,2})\s*(?:er)?\s*(?P<month>janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|\d{1,2})\s*(?P<year>\d{4})"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        day = match.group("day")
        month = match.group("month")
        year = match.group("year")
        # convert month to number
        print(f"day: {day}, month: {month}, year: {year}")

        day = int(day)
      
        if month.isdigit():
            month = int(month)
        else:
            month = {
                "janvier": 1,
                "février": 2,
                "mars": 3,
                "avril": 4,
                "mai": 5,
                "juin": 6,
                "juillet": 7,
                "août": 8,
                "septembre": 9,
                "octobre": 10,
                "novembre": 11,
                "décembre": 12
            }[month.lower()]
        # return date in YYYY-mm-dd format
        return f"{year}-{month:02d}-{day:02d}"
    else:
        return None




def extract_address(text):
    """
    Extracts the address from a given text in French format. The function uses a regular expression pattern to match the address in the text. The address is returned as a string. If the address is not found in the text, the function returns None.
    PROMPT: generate the french address extraction regex that use common pattern of 
    1. verb, preprosition for example: "habité à"  
    2. followed by a number
    3. keywords such as "rue", "avenue", "bld" etc.  to get the address. 
    output the docstrings and code. 
    
    Args:
        text (str): The text to extract the address from.
    
    Returns:
        str: The address or None if the address is not found in the text.
    
    """
    # regex pattern to match address in French
    pattern = r"(?P<verb>habité|demeuré|vécu)\s*(?:à|au|aux|dans|sur|sous|devant|derrière|près de|loin de|à proximité de|au bord de|au pied de|au sommet de|au milieu de|au bout de|à l'angle de|à côté de|en face de|face à|vers)\s*(?P<address>(rue|avenue|bld|terrasse|place|boulvard)\s[\w\s\d,-]+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        address = match.group("address")
        # return address
        return address
    else:
        return None

def extract_name(text):
    """
    Extracts the name from a given text in French format. The function uses a regular expression pattern to match the name in the text. The name is returned as a string. If the name is not found in the text, the function returns None.
    PROMPT: generate the french name extraction regex that use common pattern of 
    1. french title such as "M.", "Mme", "Mlle"
    2. followed by a firstname
    3. followed by a lastname
    output the docstrings and code. 
    
    Args:
        text (str): The text to extract the name from.
    
    Returns:
        str: The name or None if the name is not found in the text.
    
    """
    # regex pattern to match name in French
    pattern = r"(?P<title>M\.|Mme|Mlle)\s*(?P<firstname>\w+)\s*(?P<lastname>\w+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        name = match.group("title") + " " + match.group("firstname") + " " + match.group("lastname")
        # return name
        return name
    else:
        return None





