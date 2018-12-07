from rdflib import Graph
from rdflib.namespace import FOAF

def get_me(filepath):
    foaf = Graph()
    foaf.parse(filepath)
    res = foaf.query("""SELECT DISTINCT ?fname ?nickname ?lname ?email
                     WHERE {
                     ?me a foaf:Person .
                     ?me foaf:givenname ?fname .
                     ?me foaf:nick ?nickname .
                     ?me foaf:family_name ?lname .
                     ?me foaf:mbox ?email .
                     }
                     """, initNs={"foaf": FOAF})
    return list(res)[0]

