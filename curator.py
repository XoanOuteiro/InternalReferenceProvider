import re

class Curator():
    """
    Uses RegEx to parse strings and extract the value of any
    HTML atribute thats found matching the passed csv
    """

    csv_values = []


    def __init__(self, filepath : str):
        """
        Instances a curator that will parse text searching
        for the words in the given namelist
        """
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    word = line.strip() 
                    self.csv_values.append(word)

        except Exception as error:
            raise FileExistsError("[-] Namelist file not found.")
        
        
    def curate(self, text: str):
        """
        Returns a list containing tuples of tag name,
        attribute name, and value
        for each match found in the text
        """
        result = []  # Initialize an empty list to store tuples of tag name, attribute name, and value

        for attr_name in self.csv_values:  # Iterate through each attribute name in the CSV values list

            regex = fr'<(\w+)\s+[^<>]*{attr_name}=["\']([^"\']+)["\']'  # Construct a regular expression pattern to match the tag name, attribute name, and its value
            matches = re.finditer(regex, text)  # Find all matches of the pattern in the text

            for match in matches:  # Iterate through each match found
                tag_name = match.group(1)  # Extract the tag name from the match
                value = match.group(2)  # Extract the value of the attribute
                result.append((tag_name, attr_name, value))  # Append a tuple of tag name, attribute name, and value to the result list

        return result